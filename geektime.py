import base64
import datetime
import hashlib
import hmac
import json
import time

import requests

# URL paramaters configuration
base_url = "https://api.bitfinex.com/"
endpoint = "v2/auth/r/wallets"
url = base_url + endpoint

apiKey = 'Qqm88VbzvveuscHA7GcLBr4ll7vlq6tGMSAmCu74RBc'
apiSecret = 'lupyHwQqVF01Nkx21On94l5kAiXYrkW6f1uRU0ebAyz'.encode()

# nonce

t = datetime.datetime.now()
# t = str(int(time.mktime(t)))
# print(t)
nonce = str(int(time.mktime(t.timetuple())*1000))
print(nonce)
# sig
# endpoint = "v2/auth/r/wallets"
payload = "/api/" + endpoint + nonce
signature = payload.encode()
sig= hmac.new(signature, apiSecret, hashlib.sha384).hexdigest()
print("the hashed sig is" + sig)


request_headers = {
    'Content-Type': 'application/json',
    'bfx-nonce': nonce,
    'bfx-apikey': apiKey,
    'bfx-signature': sig
}



response = requests.post(url,
                         headers=request_headers)

# new_order = response.json()
print(response)




