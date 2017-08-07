# functools.partial
重新定义签名
`myurlunquote = functools.partial(urlunquote, encoding='latin1')`
当调用 myurlunquote(args, *kargs)
相当于 urlunquote(args, *kargs, encoding='latin1')
# Beautiful Soup
一个可以从HTML或XML文件中提取数据的Python库
# lxml
lxml.html
# bottlenose
第三方adapi接口库
# click 
命令行
# itetools
生成器
itetools.imap
# contextlib
上下文管理
contextlib.closing
# gensim
Python framework for fast Vector Space Modelling
用于快速向量空间建模的Python框架
`from gensim.models.phrases import Phrases, Phraser`
`from gensim.utils import simple_preprocess, any2unicode`
# os
os.env.get()获取系统参数

#  \_\_future__ 
* unicode_literals
  默认unicode编码，字符串前不需要加u
* absolute_import
  绝对导入
* print_function
  打印函数
* division
  高精度除法
  //低精度
# operator
* attrgetter
  class b():........
  f = attrgetter('name', 'date'):: the call f(b) returns (b.name, b.date).

#python-dotenv

#alembic / migrate
Alembic 是 Sqlalchemy 的作者实现的一个数据库版本化管理工具，它可以对基于Sqlalchemy的Model与数据库之间的历史关系进行版本化的维护。
[参考blog](http://huangx.in/18/alembic-simple-tutorial)

#argparse
命令行选项与参数解析