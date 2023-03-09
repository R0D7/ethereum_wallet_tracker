from web3 import Web3
import json
from eth_utils.address import to_checksum_address
from get_price import get_erc_price_, get_eth_price_

def get_balance_eth_value(wallet_eth, cmc_api_key, node_url_provider):
    web3 = Web3(Web3.HTTPProvider(node_url_provider))
    balance_wei = float((web3.eth.get_balance(wallet_eth)))
    balance_ether = float(web3.fromWei(balance_wei, 'ether'))
    balance_ether_value = balance_ether * get_eth_price_(cmc_api_key)
    print( "ETH :", balance_ether_value, "$")
    return float(balance_ether_value)

def get_balance_erc20_value(wallet_eth, cmc_api_key, node_url_provider):
    
    total_value_erc20 = 0
    web3 = Web3(Web3.HTTPProvider(node_url_provider))
    print(web3.isConnected())

    abi = json.loads('[ { "constant": true, "inputs": [], "name": "name", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "type": "function" }, { "constant": true, "inputs": [], "name": "decimals", "outputs": [ { "name": "", "type": "uint8" } ], "payable": false, "type": "function" }, { "constant": true, "inputs": [ { "name": "_owner", "type": "address" } ], "name": "balanceOf", "outputs": [ { "name": "balance", "type": "uint256" } ], "payable": false, "type": "function" }, { "constant": true, "inputs": [], "name": "symbol", "outputs": [ { "name": "", "type": "string" } ], "payable": false, "type": "function" } ]')
    with open('contract_adress_data.txt', 'r') as contract_adress_data:
        erc20_adress_list = json.load(contract_adress_data)

    for i in erc20_adress_list :
        contract = web3.eth.contract(address=to_checksum_address(i), abi=abi)
        symbol_token = contract.functions.symbol().call()
        balance_token = contract.functions.balanceOf(wallet_eth).call()
        if  balance_token == 0 :
            print(symbol_token, ": 0 $")
            continue
        else : 
            
            price_token =  get_erc_price_(symbol_token.upper(), cmc_api_key)
            print(symbol_token, ":", balance_token * price_token , "$")
            total_value_erc20 += balance_token * price_token
    return total_value_erc20