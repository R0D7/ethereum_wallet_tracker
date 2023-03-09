# Ethereum Wallet Tracker
The Ethereum Wallet Tracker is a Python program that allows you to retrieve the value of an Ethereum wallet in US dollars by simply entering the wallet's address. This program makes use of the CoinMarketCap API to fetch the current price of Ethereum and ERC20 tokens and web3 package to get the balance of any wallet.

## Features
* Retrieve the balance of an Ethereum wallet in US dollars
* Support for ERC20 tokens _(Currently, the program only tracks the top 35 ERC20 tokens in terms of the highest circulating market capitalization of march 2023. This means that only these tokens will be included in the calculation of the wallet's total value.)_
* Automatically fetches the current price of Ethereum and ERC20 tokens from the CoinMarketCap API

## Prerequisites
To use the Ethereum Wallet Tracker, you need the following:

* Python 3.x
* web3 library
* requests library
* eth-utils library
* CoinMarketCap API (You can get one for free by visiting https://pro.coinmarketcap.com/)
* Node provider URL (You can get one for free by visiting https://www.infura.io/)

## Installation
1. Clone the repository
```
git clone https://github.com/R0D7/ethereum_wallet_tracker.git
```
2. Install the required libraries using pip
```
pip install web3 requests eth-utils
```

## Usage

1.You must enter your CoinMarketCap API the first time you run the file (You can change it later by editing it in the file cmc_api_key.txt)
```
Enter your CoinMarketCap API key : xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx
```
2. You must enter your node provider url the first time you run the file (You can change it later by editing it in the file node_url_provider.txt)
```
Enter your node provider url : https://mainnet.infura.io/v3/XxxxXXXxxxxXxx
```
3. Enter the Ethereum wallet address you want to track.
```
Enter an ethereum adress : 0x47ac0Fb4F2D84898e4D9E7b4DaB3C24507a6D503
```
4. The program will output the total value of the wallet in US dollars
```
The wallet is worth 170640110.58 $
```
