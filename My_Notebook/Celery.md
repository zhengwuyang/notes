Celery 是一个由 Python 编写的简单、灵活、可靠的用来处理大量信息的分布式系统,它同时提供操作和维护分布式系统所需的工具。

Celery 专注于实时任务处理，支持任务调度。

说白了，它是一个分布式队列的管理工具，我们可以用 Celery 提供的接口快速实现并管理一个分布式的任务队列。

# broker--worker--result 
brokers 中文意思为中间人，在这里就是指任务队列本身，Celery 扮演生产者和消费者的角色，brokers 就是生产者和消费者存放/拿取产品的地方(队列)

常见的 brokers 有 rabbitmq、redis、Zookeeper 等