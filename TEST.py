import json
import base64
payload = {
   "request": "/v2/auth/w/order/submit",
   "symbol": "btcusd",
   "amount": "1",
   "price": "1999.00",
   "side": "buy",
   "type": "exchange limit",
   "options": ["maker-or-cancel"]
}
print(payload)
encoded_payload = json.dumps(payload).encode()
print(encoded_payload)
b64 = base64.b64encode(encoded_payload)
print(b64)
# import os
# print(os.getcwd())
# 1. python array and index

# imgs=["car","bicycle","boat"]
# for img in imgs:
#     id = imgs.index(img)+1
   
#     print(img,id)
# print(imgs)

# 2.extract word from a url

# url = "https://img1.doubanio.com/view/photo/m/public/p2251762458.webp"
# res = url.split("/")
# name = res[7]
# name2 = name.split(".")
# print((name2[0]))

# 3, Decide the frequency of for loop
# for i in range(0,10,2):
#     print(i)

