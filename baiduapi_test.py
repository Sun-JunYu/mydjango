import requests

# 获取token 
res = requests.get('https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?grant_type=client_credentials&client_id=Vnyv8BCYOGg1iHPBX6stcH6k&client_secret=hZpbw8riRjIf5USG0kzF5gNEGlqadIKB')

print(res.json())

token = res.json()['access_token']

print(token)