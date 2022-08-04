# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 12:05:42 2022

@author: Shweta
"""
from dateutil.relativedelta import relativedelta
from datetime import datetime
import requests, pandas


class Cryptocurrent:
    
    """
	Class Cryptocurrent will return the real time data (price) of top 30
    Cryptocurrencies user when user invokes this class in the form of CSV 
    file saved in their runtime path.
    
	"""
    
    def EndUrl(symbol, st_date, end_date):
        
        """
    	Creates the second half or the URL using start date, end data &
        symbol (from CryptoMain fuction). Concatenates to base URL and 
        return the URL along with the second half.
        
    	"""
        EndU='/v2/price/values/'+ symbol +'?start_date=' + st_date.strftime("%Y-%m-%dT%H:%M") + '&end_date=' + end_date.strftime("%Y-%m-%dT%H:%M") +'&ohlc=true'
        base_url = 'https://production.api.coindesk.com'
        url = base_url + EndU
        return EndU , url
    
    def CryptoData(url,end_date):
        
        """
    	Pings the API using the URL created abaove, receives the dataset,
        converts into readable dataframe format. Also drop timestamp
        column which was earlier in seconds format and replaces it with
        Datetime column which is easy to comprehend.
        
    	"""
        
        df = pandas.DataFrame(index=[0])
        temp_data_json = requests.get(url)
        temp_data = temp_data_json.json()
        df = pandas.DataFrame(temp_data['data']['entries'])
        df.columns = ['Timestamp', 'Open', 'High', 'Low', 'Close']
        df = df.drop(['Timestamp'], axis=1)
        df['Datetime'] = [end_date - relativedelta(minutes=len(df)-i) for i in range(0, len(df))]
        return df
        
    def CryptoMain(st_date,end_date):
        
        """
        Params: start date & end date
        
    	The main method which explains the flow of the class by calling 
        above methods one after the other. Firt, provides the top 30 currencies,
        initializes 3 pandas dataframe and uses iteration to ping API and store
        dataset one after the other in coin_df which is thereafetr pushed to raw_df.
        
        Returns: sorted data in CSV file in run time path.
        
    	"""
        
        coindesk30_list =['BTC', 'ETH','XRP','LUNA','SOL','ADA', 'USDT', 'SHIB','DOGE', 'XLM', 'DOT', 'UNI', 'LINK', 'USDC', 'BCH', 'LTC', 'GRT', 'ETC', 'FIL', 'AAVE', 'ALGO','AVAX','ATOM','EOS','MATIC','MANA','ALGO','DOT','ICP','UST']
        raw_df = pandas.DataFrame()
        coin_df = pandas.DataFrame()
        l = pandas.DataFrame() 
        for coin in coindesk30_list:  
            x,y=Cryptocurrent.EndUrl(coin,st_date,end_date)
            l=Cryptocurrent.CryptoData(y,end_date)
            l['Symbol'] = coin
            coin_df = coin_df.append(l)
        raw_df = raw_df.append(coin_df)
        raw_df = raw_df[['Datetime','Symbol','Open', 'High', 'Low', 'Close']].reset_index(drop=True)
        raw_df.sort_values(by=['Open'], inplace=True, ascending=False)
        raw_df.to_csv('CurrentCryptoPrice.csv', index=False)
        print("The file has been saved to your runtime path.")

                
                
        
                
            
         
    
    
    
