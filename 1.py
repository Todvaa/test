import json

import requests
import pandas as pd
from pylab import *

base_link = "https://api.binance.com"
path_link = "/api/v3/klines"
url = base_link + path_link
param = {'symbol': 'BTCUSDC', 'interval': '1d', 'limit': 1000}

quotes = requests.get(url, params=param)
data = ''
dec_data = json.loads(quotes.text)
