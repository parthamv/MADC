
import yfinance as yf
import pandas as pd

class Crypto_News:
    def crypto_news(self,crypto_name):
        return yf.Ticker(crypto_name).news
    def crypto_news_df(self,crypto_name):
        dfItem = pd.DataFrame.from_records(self.crypto_news(crypto_name))
        dfItem.drop(['uuid', 'publisher','providerPublishTime','type'], axis = 1)
        return dfItem

