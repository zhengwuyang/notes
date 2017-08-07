# 初始化postgresql
`initdb /usr/local/var/postgres`
上面指定 "/usr/local/var/postgres" 为 PostgreSQL 的配置数据存放目录
# 启动sql
`pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start`
# 停止sql
`pg_ctl -D /usr/local/var/postgres stop -s -m fast`
# 创建一个 PostgreSQL 用户
`createuser username -P`
# 创建数据库
`createdb dbname -O username -E UTF8 -e`


`sudo su - postgres` linux切换至postgres用户
`psql -U <username> -d <dbname> -h <host> -p <port>`
`create user <username>`
`\password <username>;` 修改密码
`create db <dbname> owner <username>`
`GRANT ALL PRIVILEGES ON DATABASE <dbname> to <username>;`给权限