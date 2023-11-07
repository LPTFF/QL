"""
阅读走不走我的邀请都行,能用我的本就是给面子我了
这是我的WXPUSER_TOKEN,你可以直接拿来用
export WXPUSER_TOKEN="AT_aYF2532tqjrD4dX90OrJsuiflscRureX"
微信打开链接:https://wxpusher.zjiecode.com/wxuser/?type=1&id=50341#/follow
关注wxpuser app 订阅公众号就能获取你的uid
export WXPUSER_UID="UID_xxxxx"
||||||
微信阅读:小阅阅

邀请链接:https://ot26017.a197.top:10261/yunonline/v1/auth/31cf5cf7e3f49fd7ce1738ac295dcc4f?codeurl=ot26017.a197.top:10261&codeuserid=2&time=1698839542

抓 cookie: ysmuid=xxxxx;   只要xxxxxx
export xyycks='xxxxxxxx@xxxxxxxx'
export multi_xyy='true'  # 并发开关，可以不填
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!【cookie不用你裁剪之类的,你就直接复制粘贴就行了】！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
第一步配置文件填写:export WXPUSER_TOKEN="AT_aYF2532tqjrD4dX90OrJsuiflscRureX"
第二部配置文件填写:export WXPUSER_UID="你的uid"  # 多号就export WXPUSER_UID="你的uid1@你的uid2@...."  uid获取方式看上面!!!!!!
第三步配置文件填写:export xyycks='xxxxxxxx@xxxxxxxx'
配置文件填写并发 : export multi_xyy='true'  # 并发开关，可以不填

黑号50金币,白的100

你不想用我的WXPUSER_TOKEN,这是你的自行注册的教程
如果你是让别人代挂的,你可以让代挂的给你扫一下wxpuser的码,再把uid发送给他就行
必要推送:WXPUSER  前往网站https://wxpusher.zjiecode.com/docs/#/?id=%e6%b3%a8%e5%86%8c%e5%b9%b6%e4%b8%94%e5%88%9b%e5%bb%ba%e5%ba%94%e7%94%a8
查看注册推送教程
以下推送变量
export WXPUSER_TOKEN='AT_XXXXXA...'
export WXPUSER_TOPICID='1111111'   # 这个可以不填,不推荐这个
export WXPUSER_UID='UID_xxxxx@UID_XXXX' WXPUSER_TOPICID和WXPUSER_UID二选一即可 WXPUSER_UID要和cookie数量一致,WXPUSER_UID可以重复填
比如我2个微信阅读只想推送给一个微信 那就export WXPUSER_UID='UID_123456@UID_123456'
前者群发，后者单推个人，推荐后者

new Env('小阅阅-异步并发')
cron 40 9-21/2 * * *
"""


import asyncio
import aiohttp
from typing import Optional, Dict 
from urllib.parse import urlparse, parse_qs,quote
import time,random,json,re
import os


class template:
    def __init__(self, check_url:str, index:int, wxpuser_token:str, topicid:str, wxpuser_uid:str) -> None:
        self.aol = check_url
        self.index = index
        self.wxpuser_token = wxpuser_token
        self.topicid=topicid
        self.wxpuser_uid = wxpuser_uid
        self.sessions = aiohttp.ClientSession()

    
    async def close(self):
        await self.sessions.close()

    async def request(self, url, method='get', data=None, add_headers: Optional[Dict[str, str]] = None, headers=None, dtype='json', max_retries=3):
        host = urlparse(url).netloc
        _default_headers = {
            'Host': host,
            "Connection": "keep-alive",
            # "Upgrade-Insecure-Requests":"1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090719) XWEB/8391 Flue",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh",
            "cookie":f"{self.cookie}"
        }
        # retries = 0
        # while retries < max_retries:
        try:
            request_headers = headers or _default_headers
            if add_headers:
                request_headers.update(add_headers)
            async with getattr(self.sessions, method)(url, headers=request_headers, data=data) as response:
                if response.status == 200:
                    if dtype == 'json':
                        return await response.json()
                    else:
                        return await response.text()
                else:
                    print(f"[用户{self.index}]:请求失败状态码：{response.status}")
                    # 可以选择休眠一段时间再重试，以避免频繁请求
                    await asyncio.sleep(random.randint(3,5))  # 休眠1秒钟
        except Exception as e:
            print(f"[用户{self.index}]:请求出现错误：{e}")
            await asyncio.sleep(random.randint(3,5))  # 休眠1秒钟
        # retries += 1
        # print(f"无法完成请求，已达到最大重试次数 ({max_retries})")
        # return None    

    async def wxpuser(self,title,url):
        content = '''
            <!DOCTYPE html>
            <html lang="zh-CN">
                <head>
                    <meta charset="UTF-8">
                    <title>TITLE</title>
                    <style type=text/css>
                        body {
                            background-image: linear-gradient(120deg, #fdfbfb 0%, #a5d0e5 100%);
                            background-size: 300%;
                            animation: bgAnimation 6s linear infinite;
                        }
                        @keyframes bgAnimation {
                            0% {
                                background-position: 0% 50%;
                            }
                        
                            50% {
                                background-position: 100% 50%;
                            }
                        
                            100% {
                                background-position: 0% 50%;
                            }
                        }
                        .title {
                            text-align: center;
                            font-size: 25px;
                            display: block;
                        }
                        .button {
                            background-image: linear-gradient(to right, #77A1D3 0%, #79CBCA 51%, #77A1D3 100%);
                            text-align: center;
                            transition: 0.5s;
                            background-size: 200% auto;
                            border-radius: 10px;
                            width: 50%;
                            margin: 25px auto;
                        }
                        .button a {
                            padding: 15px 45px;
                            display: block;
                            text-decoration: none;
                            color: white;
                        }
                        .tips {
                            text-align: center;
                            margin: auto;
                            padding: 10px 0px;
                            box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
                        }
                    </style>
                </head>
                <body>
                    <div class="title">用户a小阅阅,务必在一分半钟内点击阅读</div>
                    <div class='button'><a href="self.aol/redirect?user=uuu&value=0&timestamp=tsone&wxurl=link">点击阅读检测文章</a></div>
                    <div class="tips">
                        <p>如果错过时间未能阅读, 会导致当天收益下降或者没有收益</p>
                        <p>请留意消息推送时间点依照你的定时计划</p>
                    </div><br>
                </body>
            </html>
        '''
        content = content.replace('用户a',f'用户{self.index}').replace('self.aol',self.aol).replace('uuu',self.cookie).replace('link',url).replace('tsone',str(int(time.time())))
        data = {
            "appToken": self.wxpuser_token,
            "content": content,
            "summary": title,
            "contentType": 2,
        }
        if self.topicid is not None:
            data["topicIds"] = [int(self.topicid)]
        if self.wxpuser_uid is not None:
            data["uids"] = [self.wxpuser_uid]
        # print(content)

        wxpuser_url = 'http://wxpusher.zjiecode.com/api/send/message'
        res = await self.request(wxpuser_url,'post',data=json.dumps(data), headers={"Content-Type":"application/json"})
        if res['success'] == True:
            print(f"[用户{self.index}][通知]: 检测发送成功！")
        else:
            print(f"[用户{self.index}][通知]: 发送失败！！！！！")
    
    async def init_chekc_dict(self):
        print(f"[用户{self.index}][init]: 初始化阅读后台检测状态")
        url = self.aol + f'/check_dict?user={self.cookie}&value=0'
        res = await self.request(url)
        if not res:
            print(f"[用户{self.index}][错误]: 索取字典出现错误{res}一定是服务器的问题,休息5秒")
            await asyncio.sleep(5)
            await self.init_chekc_dict()
        if res['status'] == 200:
            self.check_data = dict(res['check_dict'])
            print(f"[用户{self.index}][init]: 初始化状态成功")
            return True
        if res['status'] == 207:
            print(f"[用户{self.index}][init]: {res['warning']}")
            return False
    
    async def get_read_state(self, max_retry=3):
        url = self.aol + f'/read/state?user={self.cookie}&value=0'
        try:
            async with aiohttp.ClientSession() as client:
                async with client.get(url) as res:
                    if res.status ==200:
                        res1 = await res.json()
                        if res1['status'] == True:
                            return True
                        else:
                            if res1['status'] == '-1' and max_retry>0:
                                await asyncio.sleep(5)
                                await self.get_read_state(max_retry-1)
                            return False
                    else:
                        return False
        except Exception as e:
            print(f"捕获到请求状态异常:{e}")
            if max_retry == 0:
                return False
            await asyncio.sleep(3)
            await self.get_read_state(max_retry-1)

    async def get_params(self):
        url = 'https://ot26017.a197.top:10261/yunonline/v1/auth/31cf5cf7e3f49fd7ce1738ac295dcc4f?codeurl=ot26017.a197.top:10261&codeuserid=2&time=1698839542'
        host = urlparse(url).netloc
        headers = {
            "Host":host,
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 MMWEBID/2651 MicroMessenger/8.0.40.2420(0x28002851) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding":"gzip, deflate",
            "X-Requested-With":"com.tencent.mm",
            "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding":"gzip, deflate",
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, allow_redirects=False) as response:
                res = await response.text()
                pattern = r'href="([^"]+)"'
                match = re.search(pattern, res)
                if match:
                    link = match.group(1)
                    # print(link)
                    host = urlparse(link).netloc
                    self.url = 'http://'+host
                    # print(self.url)
                else:
                    print(f"[用户{self.index}]:未找到主链接")

    async def init_read(self):
        ''
        url = self.url +'/?cate=0'
        res = await self.request(url, dtype='text')
        if res is None:
            print(f"[用户{self.index}][init]: 初始化请求获取失败")
            return
        # print(res)
        pattern = r'href="([^"]+)"[^>]*>提现</a>'
        matches = re.findall(pattern, res)
        if matches:
            self.exchange_url = matches[0]
            # print(f"提现 {self.exchange_url} ")
        pattern =  r'// var unionid="([^"]+)"'
        match = re.search(pattern, res)    
        if match:
            self.unionid = match.group(1)
        else:
            print("No unionid found")
            return 
    
    async def account(self):
        add_header = {'Accept':'application/json, text/javascript, */*; q=0.01'}
        ts = int(time.time()*1000)
        url = self.url + f'/yunonline/v1/gold?time={ts}&unionid={self.unionid}'
        # print(url)
        res = await self.request(url, add_headers=add_header, dtype='text')
        if res is None:
            print(f"[用户{self.index}][错误]: 获取剩余文章出错了")
            return 
        res = json.loads(res)
        if res['errcode'] == 0:
            print(f"[用户{self.index}][信息]: 金币 {res['data']['day_gold']}, 剩余文章{res['data']['remain_read']}")
            if res['data']['remain_read'] >0:
                print(f"[用户{self.index}][信息]: 获取第1篇文章url")
                await asyncio.sleep(3)
                urla = await self.start()
                await self.request(urla,dtype='text')
                host = urlparse(urla).netloc
                query_parameters = parse_qs(urlparse(urla).query)
                uk = query_parameters.get('uk', [])[0] if query_parameters.get('uk') else None
                if uk:
                    for i in range(1,res['data']['remain_read']+1):
                        print(f"[用户{self.index}][阅读]: 第{i}篇文章,休息5秒起步")
                        await asyncio.sleep(random.randint(5,7))
                        await self.do_read_task(host, uk=uk)
                        if self.cont == False:
                            break
                        await asyncio.sleep(1)
                else:
                    print(f"[用户{self.index}]: 没有发现可用的uk")
            else:
                print(f"[用户{self.index}]: 今天没有可阅读的文章了")
        else:
            print(f"[用户{self.index}]: 出错了:{res}")
    
    async def start(self):
        url = self.url+'/yunonline/v1/wtmpdomain'
        data = f'unionid={self.unionid}'
        add_headers = {"Content-Lenght": str(len(data)),"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Origin":"http://1695469567.snak.top","Referer":"http://1695469567.snak.top/"}
        res = await self.request(url, 'post', data=data, add_headers=add_headers, dtype='text')
        if res is None:
            print(f"[用户{self.index}][文章]: url加载不了")
            return
        res = json.loads(res)
        if res['errcode'] == 0:
            print(f"[用户{self.index}][文章]: url加载成功")
            return res['data']['domain']
        else:
            return None
    
    async def do_read_task(self, origin, uk):
        url = f'https://nsr.zsf2023e458.cloud/yunonline/v1/do_read?uk={uk}'
        add_header= {'origin': f'https://{origin}','accept':'application/json, text/javascript, */*; q=0.01','sec-fetch-site':'cross-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty'}
        res = await self.request(url,add_headers=add_header, dtype='text')
        if res:
            res = json.loads(res)
            if res['errcode'] == 0:
                link_url = res['data']['link']
                await asyncio.sleep(random.randint(1,3))
                await self.jump(url=link_url,uk=uk,origin=origin)
            else:
                print(f"[用户{self.index}][阅读]: {res['msg']}")
                if res['errcode'] == 407:
                    self.cont = False
        else:
            print(f"[用户{self.index}][错误]: 请求阅读出现差错,休息5秒")
            await asyncio.sleep(random.randint(5,6))
            await self.do_read_task(origin,uk)

            
    
    async def jump(self,url, uk,origin):
        url = url+'?/'
        host = urlparse(url).netloc
        headers = {
            "Host":host,
            "Connection":"keep-alive",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Linux; Android 13; M2012K11AC Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 MMWEBID/2651 MicroMessenger/8.0.40.2420(0x28002851) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding":"gzip, deflate",
            "X-Requested-With":"com.tencent.mm",
            "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding":"gzip, deflate",
            'Cookie': self.cookie
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, allow_redirects=False) as response:
                    location = response.headers.get('Location')
                    if await self.varification(location):
                        ts = random.randint(7, 14)
                        print(f"[用户{self.index}][等待]: 休息{ts}秒")
                        await asyncio.sleep(ts)
                        await self.complete_task(uk, ts, origin)

    async def varification(self,url):
        parsed_url = urlparse(url)
        # print(url)
        query_parameters = parse_qs(parsed_url.query)
        if 'chksm' in query_parameters:
            print(f"[用户{self.index}][文章]: ⩥⩥⩥⩥⩥出现检测文章了！！！！")
            encoded_url = quote(url)
            await self.wxpuser(f"小阅阅[用户{self.index}]检测,请90秒内点击阅读",encoded_url)
            print(f"[用户{self.index}][等待]: 请手动前往wxpuser点击阅读")
            start_time = int(time.time())
            while True:
                if await self.get_read_state():
                    print(f"[用户{self.index}][阅读]: 已手动阅读,休息3秒")
                    await asyncio.sleep(3)
                    return True
                if int(time.time()) - start_time > 90:
                    print(f"[用户{self.index}][警告]: 超时未阅读，终止本次阅读")
                    self.cont = False
                    return False
                await asyncio.sleep(1)
        else:
            print(f"[用户{self.index}][文章]: 没有检测")
            return True
        # if '__biz' in query_parameters:
        #     biz_value = query_parameters['__biz'][0]
        #     print(f"[用户{self.index}]: {biz_value}")
        #     if biz_value in self.check_data:
        #         print(f"[用户{self.index}][文章]: 出现检测{self.check_data[biz_value][0]}公众号！")
        #         encoded_url = quote(url)
        #         await self.wxpuser(f"小阅阅[用户{self.index}]检测,请90秒内点击阅读",encoded_url)
        #         print(f"[用户{self.index}][等待]: 请手动前往wxpuser点击阅读")
        #         start_time = int(time.time())
        #         while True:
        #             if await self.get_read_state():
        #                 print(f"[用户{self.index}][阅读]: 已手动阅读,休息3秒")
        #                 await asyncio.sleep(3)
        #                 return True
        #             if int(time.time()) - start_time > 90:
        #                 print(f"[用户{self.index}][警告]: 超时未阅读，终止本次阅读")
        #                 self.cont = False
        #                 return False
        #             await asyncio.sleep(1)
        #     else:
        #         print(f"[用户{self.index}][文章]: 没有检测")
        #         return True
        # else:
        #     print(f"[用户{self.index}][文章]:__biz parameter not found in the URL")
        #     return True
        
    async def complete_task(self,uk,ts, origin):
        tsp = int(time.time())
        add_header= {'origin': f'https://{origin}','accept':'application/json, text/javascript, */*; q=0.01','sec-fetch-site':'cross-site'}
        url = f'https://nsr.zsf2023e458.cloud/yunonline/v1/get_read_gold?uk={uk}&time={ts}&timestamp={tsp}000'
        res = await self.request(url,add_headers=add_header,dtype='text')
        if res is None:
            print(f"[用户{self.index}]: 请求领取阅读币失败{res}")
            return
        res = json.loads(res)
        if res['errcode'] == 0:
            print(f"[用户{self.index}][奖励]: {res['msg']}, +{res['data']['gold']}币,今天阅读数:{res['data']['day_read']},剩余{res['data']['remain_read']}")
            if res['data']['gold'] == 0:
                self.cont = False
        else:
            # print(res)
            print(f"[用户{self.index}]: 领取阅读币失败原因是{res['msg']}")
            if res['errcode'] == 407:
                self.cont = False
    
    async def user_gold(self):
        add_header = {'Accept':'application/json, text/javascript, */*; q=0.01','cookie':self.cookie,'Referer':'http://1695469567.snak.top/?cate=0'}
        ts = int(time.time()*1000)
        url = self.url + f'/yunonline/v1/gold?unionid={self.unionid}&time={ts}'
        res = await self.request(url, add_headers=add_header,dtype='text')
        if res is None:
            print(f"[用户{self.index}]: 没有获取到提现所需要的内容{res}")
            return
        res = json.loads(res)
        if res['errcode'] == 0:
            current_gold = res['data']['last_gold']
            print(f"[用户{self.index}][余额]: {current_gold}金币")
            tag = 6000
            if int(current_gold) >= tag:
                gold = int(int(current_gold)/1000)*1000
                unionid,request_id = await self.exchange()
                if unionid and request_id:
                    # print(unionid,request_id)
                    await self.with_draw(unionid=unionid,request_id=request_id,gold=gold)
                else:
                    print(f"[用户{self.index}]: 没有获取到提现的参数，待修复")
            else:
                print(f"[用户{self.index}][余额]: {current_gold} < {tag} ,不满足条件")
        else:
            print(f"[用户{self.index}]: 出现一些问题")

    async def exchange(self):
        host = urlparse(self.exchange_url).netloc
        add_headers = {"Referer":f'http://{host}/?cate=0'}
        res = await self.request(self.exchange_url, add_headers=add_headers,dtype='text')
        if res is None:
            print(f"[用户{self.index}][用户]: 获取unionid, snid出错")
            return None,None
        pattern_unionid = r'var unionid = \'(.*?)\';'
        pattern_request_id = r'var request_id = "(.*?)";'
        match_unionid = re.search(pattern_unionid, res, re.DOTALL)
        match_request_id = re.search(pattern_request_id, res, re.DOTALL)
        # print(match_request_id,match_unionid)
        if match_unionid:
            unionid_value = match_unionid.group(1)
        else:
            unionid_value = None
        if match_request_id:
            request_id_value = match_request_id.group(1)
        else:
            request_id_value = None
        if unionid_value and request_id_value:
            return unionid_value,request_id_value
        else:
            return None,None
        
    async def with_draw(self, unionid, request_id, gold):
        host = urlparse(self.exchange_url).netloc
        url1 = f"http://{host}/yunonline/v1/user_gold"
        host = urlparse(self.exchange_url).netloc
        data1 = f"unionid={unionid}&request_id={request_id}&gold={gold}"
        add_headers = {"Content-Lenght": str(len(data1)),"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Origin":f"http://{host}","Referer":self.exchange_url,'X-Requested-With': 'XMLHttpRequest'}
        res = await self.request(url1,'post',data=data1,add_headers=add_headers,dtype='text')
        if res is None:
            print(f"[用户{self.index}]: 请求提现出错{res}")
            return
        res = json.loads(res)
        if res['errcode'] == 0:
            print(f"[用户{self.index}][提现]: {res['data']['money']}元")
            url2 = self.url+'/yunonline/v1/withdraw'
            data2 = f"unionid={unionid}&signid={request_id}&ua=2&ptype=0&paccount=&pname="
            {"Content-Lenght": str(len(data2)),"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Origin":f"http://{host}","Referer":self.exchange_url}
            res1 = await self.request(url2,'post', data=data2,add_headers=add_headers,dtype='text')
            if not res1:
                print(f"[用户{self.index}]: 请求提现出错{res1}")
                return
            res1 = json.loads(res1)
            if res1['errcode'] == 0:
                print(f"[用户{self.index}][提现]: {res1['msg']}")
            else:
                print(f"[用户{self.index}][提现]: 失败,原因{res1['msg']}")
        else:
            print(f"[用户{self.index}]: 未知错误{res}")

    async def run(self, ck:str, sleep_time=None):
        if sleep_time:
            print(f"[用户{self.index}][等待]: 随机休息{sleep_time}秒,避免并发响应过多反应不过来")
            await asyncio.sleep(sleep_time)
        print(f"[用户{self.index}][开始]===========第{self.index}个的账号===========")
        self.cont = True
        self.cookie = f'ysmuid={ck}'
        if await self.init_chekc_dict():
            await self.get_params()
            await self.init_read()
            await self.account()
            await self.user_gold()
        await self.close()
        print(f"[用户{self.index}][结束]============第{self.index}个账号===========")

async def test_api(url):
    print("开始测试检测服务可用性")
    api_url = url + '/read/announcement'
    try:
        async with aiohttp.ClientSession() as client:
            async with client.get(api_url) as res:
                if res.status ==200:
                    result = await res.json()
                    print(f"[公告]:{result['messages']}")
                    return True
                else:
                    return False
    except Exception as e:
        print(f"出错了,稍后再来:{e}")
    

async def check_env():
    wxpuser_token = os.getenv("WXPUSER_TOKEN")
    topicid = os.getenv("WXPUSER_TOPICID")
    wxpuser_uid = os.getenv("WXPUSER_UID")
    cks = os.getenv('xyycks')
    if cks is None:
        print("小悦悦ck为空,请去抓包格式:cookie:'ysmuid=xxxxx.....'只要xxxxx 多账户请用@分割")
        print("cookie填写,export xyycks='xxxxxx'")
        exit()
    correct_data = []
    for index ,ck in enumerate(cks.split("@")):
        # 也许这里可以添加你的变量检测是否合规
        # Here you can write some code.
        if 'ysmuid=' in ck:
            print(f"账号[{index+1}]:请手动去除cookie里面的ysmuid=")
        else:
            correct_data.append(ck)
    if wxpuser_token is None:
        print("wxpuser的apptoken为空,前往官网注册创建一个app,复制应用token和微信关注wxpuser公众号获取uid")
        print("获取完请在配置文件填写:export WXPUSER_TOKEN=AT_aYF2.....\nexport WXPUSER_UID=UID_....")
        exit()
    if topicid is None and wxpuser_uid is None:
        print("wxpuser的topicid和WXPUSER_UID都为空,请至少填写其中一个")
        exit()
    return wxpuser_token, topicid, wxpuser_uid.split('@'), correct_data

async def main():
    apptoken, topicid, wx_uids, cks_list = await check_env()
    # 检查是否存在环境变量 multi
    api_url = 'http://110.41.145.200:8088'
    if await test_api(api_url):
        print(f"[测试]:{api_url}服务当前可用")
    else:
        print(f"[测试]:{api_url}服务当前不可用,可能服务器断电、断网了,稍后再来吧")
        exit()
    mapping = dict(zip(cks_list, wx_uids))
    random_sleep_list = [i * random.randint(30, 45) for i in range(len(cks_list))]
    from random import shuffle
    shuffle(cks_list)
    wx_uids = [mapping[item] for item in cks_list]
    use_concurrency = os.environ.get('multi_xyy', 'false').lower() == 'true'
    tasks = []
    for index, ck in enumerate(cks_list):
        abc = template(api_url, index+1, apptoken, topicid, wx_uids[index])
        task = abc.run(ck, random_sleep_list[index])
        tasks.append(task)
    if use_concurrency:  # 如果是true 那么就执行并发
        await asyncio.gather(*tasks)  # 并发执行任务
    else:  # 如果是false 那么就串行执行
        for task in tasks:
            await task  

if __name__ == '__main__':
    asyncio.run(main())