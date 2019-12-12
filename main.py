import rtbManager
import adslot

if __name__ == '__main__':
    
    #初始化 依次三个参数 appkey appID deviceID
    rtbManagerInstace=rtbManager.rtbManager("lxro7k17u3asd8vj","al3l7unur521r3n3zutkpp7uf7tj87od","MLAT1A2019624001281") 
    
    #初始化广告位  ID  类型->IMG/VDO  数量
    adslot=adslot.adslot("25075828","IMG",4)
    
    #针对广告位发起请求，获取广告
    result=rtbManagerInstace.request(adslot)
    
    #广告结果返回
    print(result)

