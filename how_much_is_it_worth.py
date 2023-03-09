from web3 import Web3
from get_balance import get_balance_eth_value, get_balance_erc20_value
import os

if os.path.exists(os.path.dirname(os.path.abspath(__file__))+"\\cmc_api_key.txt"):
    with open(os.path.dirname(os.path.abspath(__file__))+"\\cmc_api_key.txt", "r") as f:
        cmc_api_key = f.read().strip()
else:
    cmc_api_key = input("Enter your CoinMarketCap API key : ")

    with open(os.path.dirname(os.path.abspath(__file__))+"\\cmc_api_key.txt", "w") as f:
        f.write(cmc_api_key)

if os.path.exists(os.path.dirname(os.path.abspath(__file__))+"\\node_url_provider.txt"):
    with open(os.path.dirname(os.path.abspath(__file__))+"\\node_url_provider.txt", "r") as f:
        node_url_provider = f.read().strip()
else:
    node_url_provider = input("Enter your node provider url  : ")

    with open(os.path.dirname(os.path.abspath(__file__))+"\\node_url_provider.txt", "w") as f:
        f.write(node_url_provider)

i = True
while i is True :
    eth_wallet = input("Enter an ethereum adress : ")
    if Web3.isAddress(eth_wallet) is True :
        total_value = float(get_balance_erc20_value(eth_wallet, cmc_api_key, node_url_provider)) + float(get_balance_eth_value(eth_wallet, cmc_api_key, node_url_provider))
        print("The wallet is worth", float(total_value) , "$ ")
        print("----------------------------------------")
    else : print("Invalid adress")