import requests
import json

city_name=input('Input City name:\n')
with open(r'C:\Users\DELL\Python stuffs\city_list.json', encoding="utf-8") as f:
  data = json.load(f)

for dic in data:
    for val in dic.keys():
        if dic['name']==city_name:
           ID =dic['id']

            
params={"APIKEY":"ec5a67af8f14a58ca723644a939217fc",
    "id": ID }
url2="http://api.openweathermap.org/data/2.5/forecast?&appid={APIKEY}"
response=requests.get(url2,params=params)

req=response.json()

x=req['city']['coord']['lat']
print(x)
print(req['city'])
xx=req['list']
new_list=[]
new_list2=[]
new_list3=[]
new_list4=[]
for key in xx:
    new_list.append(key)

y=new_list[1]['weather']
for i in y:
    zz=i

print(zz['description'])

z=new_list2[2]['weather']
for i in z:
    zz=i

print(zz['description'])
