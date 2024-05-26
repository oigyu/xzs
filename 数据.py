import requests

def get_phone_info(number):
    url = 'http://cx.shouji.360.cn/phonearea.php?number=' + str(number)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        print(data)
    else:
        print('Failed to get phone info')

# 测试函数
get_phone_info(13012345678)
get_phone_info(13800001111)
get_phone_info(18966778899)
get_phone_info(18670758559)
