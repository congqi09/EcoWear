from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from datetime import timedelta


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')

        firstname = extra_fields.pop('firstname', None)
        lastname = extra_fields.pop('lastname', None)

        if email:
            email = self.normalize_email(email)

        user = self.model(username=username, email=email, firstname=firstname, lastname=lastname, **extra_fields)
        # user.set_password(password)  # This method handles password hashing
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('userGroup', 'admin')

        if extra_fields.get('userGroup') != 'admin':
            raise ValueError('Superuser must have userGroup of admin')

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=33, unique=True)
    firstname = models.CharField(max_length=33, blank=True, null=True)
    lastname = models.CharField(max_length=33, blank=True, null=True)
    email = models.EmailField(max_length=33, unique=True)
    password = models.CharField(max_length=128)
    address = models.CharField(max_length=99, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profilePicture = models.CharField(max_length=255, blank=True, null=True)
    userGroup = models.CharField(max_length=10, choices=[('admin', 'admin'), ('user', 'user')])
    userRating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    registerDate = models.DateField(auto_now_add=True)
    lastLoginDate = models.DateField(auto_now=True)

    # Override groups and user_permissions fields to set related_name
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="mypage_user_set",
        related_query_name="mypage_user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="mypage_user_set",
        related_query_name="mypage_user",
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyUserManager()

    def __str__(self):
        return self.username


class Item(models.Model):
    itemid = models.AutoField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=33)
    description = models.CharField(max_length=255, blank=True, null=True)
    categoryid = models.IntegerField(db_column='categoryId', blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(max_length=33, blank=True, null=True)
    brand = models.CharField(max_length=33, blank=True, null=True)
    itemcondition = models.CharField(db_column='itemCondition', max_length=15, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(max_length=255, blank=True, null=True)
    List_time = models.DateTimeField(default=timezone.now)
    currentTime = models.DateTimeField(default=timezone.now)

    def is_bidding_active(self):
        return self.currentTime < self.List_time + timedelta(days=5)


    class Meta:
        db_table = 'Item'


class Auction(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='auctions')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auctions_seller')
    status = models.CharField(max_length=15)
    startprice = models.DecimalField(max_digits=10, decimal_places=2)
    # currentbid = models.ForeignKey('Bid', on_delete=models.CASCADE, related_name='auctions', blank=True, null=True)
    buynowprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    addtime = models.DateTimeField(default=timezone.now)
    endtime = models.DateField(default=timezone.now() + timedelta(days=5))

    def currentbid(self):
        return Bid.objects.filter(item = self.item).order_by('-amount').first()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='favorited_by')
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')  # Prevents duplicate favorites

    def __str__(self):
        return f"{self.user.username} favorite {self.item.title}"
    

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    amount = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="bids")
    bidtime = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.user.username} bid on {self.item.title} for {self.amount}."
    
    def status(self):
    # Check if the bidding period is still active
        if self.item.is_bidding_active():
            return "Pending"
        else:
            # Determine if this bid is the highest for the item
            highest_bid = self.item.bids.order_by('-amount').first()
            if self == highest_bid:
                return "Success"
            else:
                return "Failed"

    class Meta:
        ordering = ['-amount']

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField(max_length=255)
    time_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver} sent on {self.time_sent.strftime("%Y-%m-%d %H:%M:%S")}'
    
    class Meta:
         managed = True
