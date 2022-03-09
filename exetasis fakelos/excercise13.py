import requests

hex_list=[]
decimals=[]
count=0

x = requests.get('https://drand.cloudflare.com/public/latest')
data_x = x.json()
randomness = data_x["randomness"]
# print(randomness)

y = requests.get('https://api.opap.gr/draws/v3.0/1100/last-result-and-active')
data_y = y.json()
kino_numbers = data_y["last"]["winningNumbers"]["list"]
print(set(kino_numbers))

for i in range(0,len(randomness),2):
    a=randomness[i]+randomness[i+1]
    hex_list.append(a)
print(set(hex_list))

for i in range(len(hex_list)):
    b=int(hex_list[i],16)%80
    decimals.append(b)
decimals=set(decimals)
print(decimals)

for i in decimals:
    for j in range(len(kino_numbers)):
        if kino_numbers[j]==i:
            count+=1
print("Common numbers are",count)
