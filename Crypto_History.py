# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 11:21:44 2022

@author: Shweta - 5110 - Project - Day 1
"""
from datetime import datetime
import time, requests, pandas, lxml
from lxml import html

class CryptoHistory:
    """
    Class CryptoHistory will return the historic data (price) of desired 
    Cryptocurrencies for the time span requested by user in the form of CSV 
    file saved at their runtime path.
    
	"""
    def format_date(date_datetime):
        
        """
    	This method takes the start and end date from the user and converts 
        it into seconds format and returns the same.
        
    	"""
        date_timetuple = date_datetime.timetuple()
        date_mktime = time.mktime(date_timetuple)
        date_int = int(date_mktime)
        date_str = str(date_int)
        return date_str
    
    def subdomain(symbol, start, end, filter='history'):
        
        """
    	This method takes the start and end date (seconds format) and
        symbol(Crypto Currency input by user) and uses this to create the subdomain
        of the URL used for API Call.
        
        Returns - subdomain URL
    	"""
        subdoma="/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter={3}&frequency=1d"
        subdomain = subdoma.format(symbol, start, end, filter)
        return subdomain
         

    def header_function(subdomain):
        """
    	Creates header used for API call to yfinance for the historic price data.
        
        Returns - hdrs (header details)
    	"""
        hdrs =  {"authority": "finance.yahoo.com",
                  "method": "GET",
                  "path": subdomain, #path key assigned as subdomain
                  "scheme": "https",
                  "accept": "text/html",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "en-US,en;q=0.9",
                  "cache-control": "no-cache",
                  "cookie": "Cookie:identifier",
                  "dnt": "1",
                  "pragma": "no-cache",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-user": "?1",
                  "upgrade-insecure-requests": "1",
                  "user-agent": "Chrome/5.0 (Windows NT 11.0; Win64)"}
        return hdrs
    
    def scrape_page(url, header):
        """
    	Sends request to yfinance with the url and header data and receives the 
        data in html format which is parsed and converted to table format.
        
        Returns - dataframe of the requested info.
    	"""
        pan = requests.get(url,headers=header)
        element_html = html.fromstring(pan.content)
        table = element_html.xpath('//table')
        table_tree = lxml.etree.tostring(table[0], method='xml')
        panda = pandas.read_html(table_tree)
        return panda
         




