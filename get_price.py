from requests import Request, Session
import json

def get_eth_price_(cmc_api_key):
    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    parameters = {
        "slug":"ethereum",
        "convert" : "USD"
    }
    headers = {
        "Acceps":"application/json",
        "X-CMC_PRO_API_KEY": cmc_api_key
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)

    price_eth = json.loads(response.text)['data']['1027']['quote']["USD"]["price"]
    return price_eth

def get_erc_price_(token_symbol, cmc_api_key):
    url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    parameters = {
        "symbol": token_symbol,
        "convert" : "USD"
    }
    headers = {
        "Acceps":"application/json",
        "X-CMC_PRO_API_KEY": cmc_api_key
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)

    price_erc = json.loads(response.text)['data'][token_symbol][0]['quote']['USD']['price']
    return price_erc