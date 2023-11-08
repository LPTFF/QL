"""
密盒星球_V1.1

看视频得金币（目前可以无限刷）

手动完成金币任务并提现后再运行脚本(防黑)，请勿频繁运行脚本(否则风控)

入口 ：

抓包域名 https://jkyx-api.chiguavod.com/applet/system/type/getUserInfo取出sessionId参数
export mhxqCK=sessionId
多账号用'===='隔开 例 账号1====账号2
cron： 0 0 0/1 * * ?

仅供学习交流，请在下载后的24小时内完全删除 请勿将任何内容用于商业或非法目的，否则后果自负。
"""



monye = 0  # 提现开关 1开启  0关闭
realName = ""  # 支付宝提现姓名
aliAccount = ""  # 支付宝提现账号
#默认提现1r  务必完善参数

import time
import random
import os
import requests


accounts = os.getenv('mhxqCK')
print(requests.get("https://tinyurl.com/yndmt3ww").content.decode("utf-8"))
if accounts is None:
    print('你没有填入mhxqCK，咋运行？')
    exit()
else:
    accounts_list = os.environ.get('mhxqCK').split('====')
    num_of_accounts = len(accounts_list)
    print(f"获取到 {num_of_accounts} 个账号")
    for i, account in enumerate(accounts_list, start=1):
        values = account.split('@')
        sessionId = values[0]
        print(f"\n=======开始执行账号{i}=======")
        headers = {
            'sessionId': sessionId,
            'Content-Length': '0',
            'Host': 'jkyx-api.chiguavod.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.10.0'
        }
        url = 'https://jkyx-api.chiguavod.com/applet/mf/advertising/integral/info'
        response = requests.post(url, headers=headers).json()
        if response['code'] == 200:
            nickName = response['data']['nickName']
            integral = response['data']['integral']
            print(f'{nickName}--{integral}积分')
            print(f'{"-" * 15}准备执行看视频{"-" * 15}')
            for i in range(100):
                data = {"sign":"8bf5e82888955411714d43888efa4441","body":{"advertiserType":1,"advertising":2}}
                url = 'https://jkyx-api.chiguavod.com/applet/mf/advertising/integral/watch/video'
                response = requests.post(url, headers=headers, json=data).json()
                if response['code'] == 200:
                    integral = response['data']['integral']
                    residueIntegral = response['data']['residueIntegral']
                    print(f"第{i + 1}次看视频成功----获得{integral}金币")
                    t = random.randint(20, 28)
                    print(f"本次模拟看视频{t}s\n当前金币总余额:{residueIntegral}")
                    print(f'{"-" * 40}')
                    time.sleep(t)
                else:
                    print(f"{response}")
                    exit()

            if monye == 1:
                data = {
                    "aliAccount": aliAccount,
                    "amount": 1,
                    "cashType": 1,
                    "realName": realName
                }
                url = 'https://jkyx-api.chiguavod.com/applet/mf/advertising/integral/withdraw'

                response = requests.post(url, headers=headers, json=data).json()
                print(response)
            elif monye == 0:
                print(f"不执行提现")
        else:
            print(f"{response}")
            exit()
