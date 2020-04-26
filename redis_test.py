import redis

#定义地址和端口
host = 'localhost'
port = 6379

#建立redis连接
r = redis.Redis(host=host,port=port)

# 列表操作
r.lpush('sunjunyu',1)

# 打印列表长度
print(r.llen('sunjunyu'))

# #声明一个值
# r.set('test','text')

# #取值
# code = r.get('test')

# #转码
# code = code.decode('utf-8')

# print(code)