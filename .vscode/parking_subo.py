import requests
import json

url='http://api.kcg.gov.tw/api/service/get/897e552a-2887-4f6f-a6ee-709f7fbe0ee3'
r=requests.get(url)
r.recodin='utf-8'
js=json.loads(r.text)
# print(js)
park=js['data'] #抓出所有park的value值
# for item in list:
#     print(item)
# print(len(park))
# print(park[0]['行政區'])


dist=input('請輸入查詢的區域 :')
print('查詢 {} 臨時停車所'.format(dist))

# for i in range(0,len(park)):
#      if (park[i]['行政區'])==dist:
#         # print(park[i]['臨時停車處所'])
#         print('地點: {}、小型停車位: {}、地址: {}'.format(park[i]['臨時停車處所'],park[i]['可提供小型車停車位'],park[i]['地址']))
# print('')
# print('查詢結束')      

for item in park:
    if item['行政區']==dist:
        print('地點: {}、小型停車位: {}、地址: {}'\
            .format(item['臨時停車處所'],item['可提供小型車停車位'],item['地址']))
print('')
print('查詢結束')      