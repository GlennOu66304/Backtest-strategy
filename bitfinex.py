import os
from re import S
import sys
# you need to use the python pip to install the pacakge, because conda can not find the package
# python3 -m pip install dotenv
from bfxapi import Client, Order
from dotenv import load_dotenv
# Using .env Files for Environment Variables in Python Applications
# https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
load_dotenv()
# KEY=os.getenv("API_KEY")
# SECRET=os.getenv("API_SECRET")
bfx = Client(

#   API_KEY= os.getenv("API_KEY"),
#   API_SECRET=os.getenv("API_SECRET")
  API_KEY='xxxxxx',
  API_SECRET='xxxx'
)

# @bfx.ws.on('authenticated')
# async def submit_order(auth_message):
#   await bfx.ws.submit_order('tBTCUSD', 19990, 0.4, Order.Type.EXCHANGE_MARKET)

# @bfx.ws.on('new_trade')
# def log_trade(trade):
#   print ("New trade: {}".format(trade))

# @bfx.ws.on('connected')
# def start():
#   bfx.ws.subscribe('trades', 'tBTCUSD')

# @bfx.ws.on('order_confirmed')
# async def on_complete(order):
#  print ("Order confirmed")
#  print (order)

# Notification ERROR: action: disabled
# https://www.reddit.com/r/bitfinex/comments/lq21e6/notification_error_action_disabled/
@bfx.ws.once('authenticated')
async def on_auth(auth_message):
 await bfx.ws.submit_order('tTESTBTC:TESTUSDT', 19990, 0.5, Order.Type.EXCHANGE_LIMIT)

bfx.ws.run()