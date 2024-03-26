## 模块规划

```
登陆 （注册、登陆、改密码）                 KECHEN
首页 浏览 （购物展示，搜索，收藏，竞标）     WENXIN
我的竞标 （变更状态，评论）                 CONGQI
在售商品（item，auction，管理 - 变更状态）  CONGQI
Profile、Message                          CHANGYU
统计页面
```

## Start to Develop

1. create a virtual env (only first time):
    
    `python -m virtualenv devenv`

2. enter the virtual env: 

    win `devenv\scripts\activate`, mac `source dbenv/bin/activates`

3. install dependencies (only first time):

    `pip install Django mysqlclient mysql-connector-python PyMySQL python-dotenv`

4. create new app

    `python manage.py startapp [appname]`

5. run server

    `python manage.py runserver`