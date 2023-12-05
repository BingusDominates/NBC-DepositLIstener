####################
# Loading packages #
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
# Declaring constants #
#######################

## Your settings are read here

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