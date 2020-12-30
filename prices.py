#!/usr/bin/python

from web3 import Web3

PIP_UNIV2DAIETH = "0x87ecBd742cEB40928E6cDE77B2f0b5CFa3342A09"
pip_block = 11474424

# HTTPProvider:
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

#print(w3.isConnected())
#print(w3.eth.getBlock('latest'))

# Reading storage
# https://medium.com/coinmonks/a-practical-walkthrough-smart-contract-storage-d3383360ea1b

last_price = 0
last_time = 0
latest_block = w3.eth.getBlock('latest').number

print("timestamp,cur,nxt")

while (pip_block < latest_block):
    price_cur = w3.eth.getStorageAt(PIP_UNIV2DAIETH, 6, pip_block)
    if price_cur != last_price:
        price_nxt = w3.eth.getStorageAt(PIP_UNIV2DAIETH, 7, pip_block)
        #print(price_cur[16:])
        last_time = pip_block
        last_price = price_cur
        #print(f"{last_time}: {int.from_bytes(last_price[16:], byteorder='big')} (cur)")
        #print(f"          {int.from_bytes(price_nxt[16:], byteorder='big')} (nxt)")

        # CSV
        print(f"{last_time},{int.from_bytes(last_price[16:], byteorder='big')},{int.from_bytes(price_nxt[16:], byteorder='big')}")
    pip_block = pip_block + 5
