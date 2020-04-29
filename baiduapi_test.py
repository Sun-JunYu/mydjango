import requests
import base64
import urllib

# 获取token
res = requests.get('https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Vnyv8BCYOGg1iHPBX6stcH6k&client_secret=hZpbw8riRjIf5USG0kzF5gNEGlqadIKB')

token = res.json()['access_token']

# 开始智能识图

# 接口地址
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token='+ token

# 定义头部信息
myheaders = {'Content-Type':'application/x-www-form-urlencoded'}

# 操作图片
# 读取图片
myimg = open('./code.png','rb')
temp_img = myimg.read()
myimg.close()

# 进行base64编码
temp_data = {'image':base64.b64encode(temp_img)}

# 对图片地址进行urlencode操作
temp_data = urllib.parse.urlencode(temp_data)

# 请求视图接口
res = requests.post(url=url,data=temp_data,headers=myheaders)

code = res.json()['words_result'][0]['words']

code = str(code).replace(' ','')

print(code)