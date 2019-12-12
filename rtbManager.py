import requests
import adslot
import time
import json
from hashlib import md5

#rtb广告管理
class rtbManager:

     #初始化
     def __init__(self,appid, appkey,deviceid):
      self.appid = appid
      self.appkey =appkey
      self.deviceid=deviceid
    
     #发起请求
     def request(self,adslot):
         """
         针对广告位发起请求
         """
        

         payloadjson=self.payload(adslot)
        

         
         
         timestamp=int(time.time())

         sgins=self.sign(payloadjson,timestamp)
        
         url="http://api6.pingxiaobao.com/rtb/subscribe.shtml?appid={0}&sequence={1}&timestamp={2}&uuid={3}&version=1.3&sign={4}".format(self.appid,timestamp,timestamp,self.deviceid,sgins)
       
         result=requests.post(url,data={'payload':payloadjson})

         response=json.loads(result.text)

         print(response)

         return response

     #payload
     def payload(self,adslot):
         
         dict = {'device-uuid': self.deviceid, 'slot-id': adslot.slotid,'quantity':adslot.quantity,'type':adslot.adslottype}
         payloadjson = json.dumps(dict)
         print(payloadjson)
         return payloadjson

     # 签名计算
     def sign(self,payload,timestamp):
         
         signstr="appid={0}&appkey={1}&payload={2}&sequence={3}&timestamp={4}&uuid={5}&version={6}".format(self.appid,self.appkey,payload,timestamp,timestamp,self.deviceid,"1.3")
        
         return self.encrypt_md5(signstr) 

     def encrypt_md5(self,str):
         # 创建md5对象
         new_md5 = md5()
         # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
         new_md5.update(str.encode(encoding='utf-8'))
        # 加密
         return new_md5.hexdigest()
        
    

      
