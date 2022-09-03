import os
from re import S
import sys
# you need to use the python pip to install the pacakge, because conda can not find the package
# python3 -m pip install dotenv
from bfxapi import Client, Order
from dotenv import load_dotenv

load_dotenv()
KEY=os.getenv("API_KEY")
SECRET=os.getenv("API_SECRET")
bfx = Client(

  API_KEY= KEY,
  API_SECRET=SECRET
)

@bfx.ws.on('authenticated')
async def submit_order(auth_message):
  await bfx.ws.submit_order('tBTCUSD', 19000, 0.01, Order.Type.EXCHANGE_MARKET)

bfx.ws.run()