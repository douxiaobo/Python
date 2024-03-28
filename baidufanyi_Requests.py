import requests
import json

if __name__=="__main__":
    url = "https://fanyi.baidu.com/sug"
    # headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    querword=input("请输入要翻译的词:")
    payload={'kw':querword}
    response=requests.post(url,headers=headers,data=payload)
    print(response.text)
    dict_obj=json.loads(response.text)
    if len(dict_obj['data']):
        res1=dict_obj['data'][0]['v']
        print('翻译出的内容为：',res1)
    else:
        print('没有找到翻译结果')