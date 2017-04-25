# load()
### joinedload()

# .one_or_none()/.first()/.one()

# .distinct()
同SQL.distinct,用于返回唯一不同的值
# .any()

# relationship
一对一
一对多
多对多

# from **sqlalchemy.ext.declarative** import 
* @as_declarative
```
  @as_declarative()
  class Base(object):
```
* @declared_attr
```
  class UserProductSalesTrend(object):

    @declared_attr
    def __tablename__(cls):
      return 'amz_{market}_user_product_sales_trend'.format(market=cls.market)
  
    id = Column(Integer, primary_key=True)
```

#scoped_session()/session()
`Session = PromiseProxy(lambda: sessionmaker(engine))`
`session = PromiseProxy(lambda: scoped_session(sessionmaker(engine)))`
使用scoped_session()之后获得的session，如果不执行session.remove(),所获得的session都是同一个session