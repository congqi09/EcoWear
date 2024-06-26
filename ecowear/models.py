# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Auction(models.Model):
    auctionid = models.IntegerField(db_column='auctionId', primary_key=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.
    sellerid = models.IntegerField(db_column='sellerId')  # Field name made lowercase.
    buyerid = models.IntegerField(db_column='buyerId', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=15)
    startprice = models.DecimalField(db_column='startPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currentbid = models.DecimalField(db_column='currentBid', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    buynowprice = models.DecimalField(db_column='buyNowPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    postdate = models.DateField(db_column='postDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Auction'


class Bid(models.Model):
    bidid = models.IntegerField(db_column='bidId', primary_key=True)  # Field name made lowercase.
    auctionid = models.IntegerField(db_column='auctionId')  # Field name made lowercase.
    bidderid = models.IntegerField(db_column='bidderId')  # Field name made lowercase.
    bidamount = models.DecimalField(db_column='bidAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bidtime = models.DateField(db_column='bidTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bid'


class Category(models.Model):
    categoryid = models.IntegerField(db_column='categoryId')  # Field name made lowercase.
    name = models.CharField(max_length=33, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Category'


class Favoritelist(models.Model):
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FavoriteList'


class Item(models.Model):
    itemid = models.IntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=33)
    description = models.CharField(max_length=255, blank=True, null=True)
    categoryid = models.IntegerField(db_column='categoryId', blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(max_length=33, blank=True, null=True)
    brand = models.CharField(max_length=33, blank=True, null=True)
    itemcondition = models.CharField(db_column='itemCondition', max_length=15, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Item'


class Message(models.Model):
    messageid = models.IntegerField(db_column='messageId', primary_key=True)  # Field name made lowercase.
    senderid = models.IntegerField(db_column='senderId')  # Field name made lowercase.
    receiverid = models.IntegerField(db_column='receiverId')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=255, blank=True, null=True)
    timesent = models.DateField(db_column='timeSent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Message'


class Review(models.Model):
    reviewid = models.IntegerField(db_column='reviewId', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    transactionid = models.IntegerField(db_column='transactionId')  # Field name made lowercase.
    rating = models.IntegerField()
    comment = models.CharField(max_length=255, blank=True, null=True)
    reviewdate = models.DateField(db_column='reviewDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Review'


class Shipping(models.Model):
    shippingid = models.IntegerField(db_column='shippingId', primary_key=True)  # Field name made lowercase.
    transactionid = models.IntegerField(db_column='transactionId')  # Field name made lowercase.
    trackingnumber = models.CharField(db_column='trackingNumber', max_length=33, blank=True, null=True)  # Field name made lowercase.
    shippingdate = models.DateField(db_column='shippingDate', blank=True, null=True)  # Field name made lowercase.
    estimateddelivery = models.DateField(db_column='estimatedDelivery', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shipping'


class Transaction(models.Model):
    transactionid = models.IntegerField(db_column='transactionId', primary_key=True)  # Field name made lowercase.
    transactiondate = models.DateField(db_column='transactionDate')  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.
    buyerid = models.IntegerField(db_column='buyerId')  # Field name made lowercase.
    sellerid = models.IntegerField(db_column='sellerId')  # Field name made lowercase.
    type = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Transaction'


class User(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=33)
    firstname = models.CharField(db_column='firstName', max_length=33, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=33, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=33, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=99, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profilepicture = models.CharField(db_column='profilePicture', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usergroup = models.CharField(db_column='userGroup', max_length=5, blank=True, null=True)  # Field name made lowercase.
    userrating = models.DecimalField(db_column='userRating', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    registerdate = models.DateField(db_column='registerDate', blank=True, null=True)  # Field name made lowercase.
    lastlogindate = models.DateField(db_column='lastLoginDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('MypageUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MypageUser(models.Model):
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(unique=True, max_length=33)
    firstname = models.CharField(max_length=33, blank=True, null=True)
    lastname = models.CharField(max_length=33, blank=True, null=True)
    email = models.CharField(unique=True, max_length=33)
    password = models.CharField(max_length=128)
    address = models.CharField(max_length=99, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profilepicture = models.CharField(db_column='profilePicture', max_length=255, blank=True, null=True)  # Field name made lowercase.
    usergroup = models.CharField(db_column='userGroup', max_length=10)  # Field name made lowercase.
    userrating = models.DecimalField(db_column='userRating', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    registerdate = models.DateField(db_column='registerDate')  # Field name made lowercase.
    lastlogindate = models.DateField(db_column='lastLoginDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mypage_user'


class MypageUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(MypageUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mypage_user_groups'
        unique_together = (('user', 'group'),)


class MypageUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(MypageUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mypage_user_user_permissions'
        unique_together = (('user', 'permission'),)


class UsersUser(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(unique=True, max_length=33)
    firstname = models.CharField(db_column='firstName', max_length=33)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=33)  # Field name made lowercase.
    email = models.CharField(max_length=33)
    password = models.CharField(max_length=33)
    address = models.CharField(max_length=99)
    phone = models.CharField(max_length=15)
    profilepicture = models.CharField(db_column='profilePicture', max_length=255)  # Field name made lowercase.
    usergroup = models.CharField(db_column='userGroup', max_length=5)  # Field name made lowercase.
    userrating = models.DecimalField(db_column='userRating', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    registerdate = models.DateField(db_column='registerDate', blank=True, null=True)  # Field name made lowercase.
    lastlogindate = models.DateField(db_column='lastLoginDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_user'
