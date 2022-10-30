from web3 import Web3, HTTPProvider

connection = Web3(HTTPProvider('https://mainnet.infura.io/v3/f2b9751eb1fe4a4f968f02653842d1b8'))

from_account = 'maniac.eth'
to_account = '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'

data = '0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675'

tx = {
    'type': '0x2',
    'from': from_account,
    'to': to_account,
    'value': '0x9184e72a'
}

print ("Latest Ethereum balance", connection.eth.call(tx, "latest"))
print(type(connection.eth.get_balance('0xce8A9a40bd846dC8f27DDA35dC8630f461FA0b1a')))