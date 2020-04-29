import redis

#定义地址和端口
host = 'localhost'
port = 6379

#建立redis连接
r = redis.Redis(host=host,port=port)

# 列表操作
r.lpush('sunjunyu',1)

# 过期时间
r.expire('sunjunyu',30)

# 打印过期时间
print(r.ttl('sunjunyu'))

# 打印列表长度
print(r.llen('sunjunyu'))

if r.llen('sunjunyu') > 5:
    print('您的帐户被锁定了')

# #声明一个值
# r.set('test','text')

# #取值
# code = r.get('test')

# #转码
# code = code.decode('utf-8')

# print(code)