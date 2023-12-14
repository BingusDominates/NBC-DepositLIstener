####################
# LOADING PACKAGES #
####################
from web3 import Web3

import time
from datetime import datetime
from os import environ as env
from dotenv import load_dotenv
import requests
import winsound
import json

from colorama import Fore, Style

import pandas as pd

assert load_dotenv()

print('=======================================================================================')
print('              ************                GM                   ************            ')
print('=======================================================================================')
print()

#######################
# DECLARING CONSTANTS #
#######################

## YOUR SETTINGS ARE READ HERE

KEY_PRICE_THRESHOLD = float(env.get('KEY_PRICE_THRESHOLD'))
THRESHOLD = float(env.get('TRANSFER_THRESHOLD'))
IGNORE_SUS = bool(int(env.get('IGNORE_SUS')))

with open("./criteria.json") as f:
    gr_settings = json.load(f)

target_amounts=[]
for group in gr_settings.keys():
     target_amounts.append(gr_settings[group]['transfer_amount'])
THRESHOLD=min(target_amounts)

#-----------------------------------------------------------

alert_active = False
alert_block_counter = 0

BASE_PORTAL_ADDRESS = env.get('BASE_PORTAL_ADDRESS').lower()
BASE_BRIDGE_ADDRESS = env.get('BASE_BRIDGE_ADDRESS').lower()

BASESCAN_API_KEY = env.get('BASESCAN_API_KEY')
ETHERSCAN_API_KEY = env.get('ETHERSCAN_API_KEY')

FT_DATABASE = env.get('FRIEND_DATABASE')
DEPO_FT_DB = env.get('DEPO_FT_DB')

ADDRESS_BOOK = env.get('ADDRESS_BOOK')

eth_rpc_url = 'https://eth.public-rpc.com'
eth_rpc_url1 = 'https://rpc.ankr.com/eth'
base_rpc_url = 'https://mainnet.base.org/'

### Initializing web3... gm
eth_mainnet = Web3(Web3.HTTPProvider(eth_rpc_url))
eth_mainnet1 = Web3(Web3.HTTPProvider(eth_rpc_url1))
base = Web3(Web3.HTTPProvider(base_rpc_url))

ft_contract = env.get('FRIEND_TECH_SHARES_CONTRACT')
ft_contract_abi = env.get('FRIEND_TECH_SHARES_CONTRACT_ABI')
ft_ctr = base.eth.contract(abi=ft_contract_abi, address=ft_contract)

### LOAD DATABASES ###

dep_ft_db = pd.read_csv(DEPO_FT_DB)

# Label library
with open(ADDRESS_BOOK, 'r') as ab:
    address_book_mainnet = json.load(ab)
addresses_list = [a.lower() for a in address_book_mainnet.keys()]
