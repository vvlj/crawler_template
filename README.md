# crawler_template
精简爬虫模板，分为两部分：爬虫、数据库。



### 目录结构

​	除了core部分，其余部分可根据不同的需求进行修改。

+ crawler
  + core  爬虫组件，不需要改动
  + \__init__.py     主调函数
  + spiders.py    编写**解析**规则
  + pipeline.py    编写数据**存储**规则     
  + setting.py    常用设置
+ db_tools
  + \__init__.py
  + base_table.py  数据库表操作
+ setting.py 配置文件

