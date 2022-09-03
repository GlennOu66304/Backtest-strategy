// const CryptoJS = require('crypto-js') // Standard JavaScript cryptography library
// const fetch = require('node-fetch') // "Fetch" HTTP req library

import fetch from 'node-fetch'
import hmacSHA384 from 'crypto-js/hmac-sha384.js';
const apiKey = 'xxxxx' // const apiKey = 'paste key here'
const apiSecret = 'xxxxxx' // const apiSecret = 'paste secret here'

const apiPath = 'v2/auth/r/wallets'// Example path

const nonce = (Date.now() * 1000).toString() // Standard nonce generator. Timestamp * 1000
console.log(nonce)
const body = {
} // Field you may change depending on endpoint

let signature = `/api/${apiPath}${nonce}${JSON.stringify(body)}` 
console.log("the signature is" + signature)
// Consists of the complete url, nonce, and request body

const sig = hmacSHA384(signature, apiSecret).toString() 
// The authentication signature is hashed using the private key
console.log("the hashed sig is" + sig)
fetch(`https://api.bitfinex.com/${apiPath}`, {
  method: 'POST',
  body: JSON.stringify(body),
  headers: {
    'Content-Type': 'application/json',
    'bfx-nonce': nonce,
    'bfx-apikey': apiKey,
    'bfx-signature': sig
  }
})
.then(res => res.json())
.then(json => console.log(json)) //Logs the response body
.catch(err => {
    console.log(err)
 })