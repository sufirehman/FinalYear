import pandas as pd
from binance import Client
from lib2to3.pgen2.token import NEWLINE
PUBLIC_KEY = 'WhihdXQmvY9QAObIELyVGAI3h1nvJZDYg1B68H7n0MHn0bISKXMwHozMcxMbaJ0Z'
PRIVATE_KEY = '2auNidRhbGrAG06UWK0MPcPYJtBj9fMFKpAWJsyjTACJLHHIdOHVbsLj8MZopJJ4'
client = Client(PUBLIC_KEY, PRIVATE_KEY)
tickers = client.get_all_tickers()
df = pd.DataFrame()
for coins in tickers:
    print()
    historical_data = client.get_historical_klines(coins["symbol"], Client.KLINE_INTERVAL_1DAY, '7 July 2022')
    coin_df = pd.DataFrame(historical_data)
    df.append(coin_df)
df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']
df['Open Time'] = pd.to_datetime(df['Open Time']/1000, unit='s')
df['Close Time'] = pd.to_datetime(df['Close Time']/1000, unit='s')
numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Quote Asset Volume', 'TB Base Volume', 'TB Quote Volume']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, axis=1)
df["Change"] = ((df["High"]-df["Low"])/df["Low"]).apply(lambda x: x*100)
print(df)
