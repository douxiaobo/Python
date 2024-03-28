import ssl
from http.client import HTTPSConnection
import json
import urllib.parse

# context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# context.check_hostname = False
# context.verify_mode = ssl.CERT_NONE
# conn = HTTPSConnection("https://fanyi.baidu.com", context=context)

# context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
# context.minimum_version=ssl.TLSVersion.TLSv1_2  # 示例：设置最低支持 TLSv1.2
# conn = HTTPSConnection("fanyi.baidu.com", context=context)

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
# 禁用证书验证（仅限调试和测试）
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
conn = HTTPSConnection("fanyi.baidu.com", context=context)

querword = input('请输入要翻译的词：')

payload = json.dumps({"kw": querword}).encode('utf-8')
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'BAIDUID=8DC9F1CF6226539B8F14D1B7ADDBC417:FG=1; BAIDUID_BFESS=8DC9F1CF6226539B8F14D1B7ADDBC417:FG=1'
}
conn.request("POST", "/sug", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

# dict_obj = json.loads(data.decode("utf-8"))
# if len(dict_obj['data']):
#     print('翻译结果：',dict_obj['data'][0]['v'])
# else:
#     print('没有找到翻译结果')

response_content = conn.getresponse().read().decode('utf-8')
response_dict = json.loads(response_content)

if 'errno' in response_dict and response_dict['errno'] == 0:
    # 成功响应，此时可以尝试访问 'data' 键
    if 'data' in response_dict:
        dict_obj = response_dict['data']
        # 进行后续数据处理
else:
    # 处理错误情况，打印错误信息或采取其他行动
    print(f"请求失败，错误码：{response_dict['errno']}, 错误信息：{response_dict['errmsg']}")
   
   