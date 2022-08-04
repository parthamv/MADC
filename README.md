Title: Market Analysis of Data for Cryptocurrencies (MADC)

Website link: https://sabooshagun.github.io/madc/

Authors:

Shagun Saboo, Amritanj Ayush, Parthasarathy Murugesan, Shweta Mishra

Summary:

As the cryptocurrency market grows in popularity, so does the need to monitor price patterns to make prudent financial decisions. The general public's understanding of this market, as well as its sources, are currently limited and in general are scattered among various web sources. We intend to centralize all cryptocurrency pricing patterns and whereabouts in one place, making it more accessible to developers working on related products as well as normal retail investors trying to make better data-backed investment decisions. 

Taking the above in perspective, our program MADC will use API requests to collect data for all crypto currencies, visualize it, and then analyse and forecast price trends. To retrieve specific news regarding the input currency, we'll employ web scraping and natural language processing.

Design: 

With just a few lines of Python code, MADC allows you to stream and download cryptocurrency market information and news. Five classes have been established, with sub-functions defined underneath them to provide the package's intended functionality. 

The classes are defined as below - 
    
 1) Class Crypto-History: This class returns historic data (price) for desired Cryptocurrencies as a CSV file saved in the user's runtime directory. YFinance is            used to deliver data depending on the parameters provided by the user in the form of a time range and a crypto ticker. 
 
    • format_date: This method takes the start and end date from the user and converts it into seconds format and returns the same.
    
    • subdomain: This method takes the start and end date (seconds format and symbol of Crypto Currency input by user) and uses this to create the subdomain of the URL                  used for API Call. 
    
    • header_function: Creates header used for API call to yfinance for the historic price data. 
    
    • scrape_page: Sends request to yfinance with the url and header data and receives the data in html format which is parsed and converted to table format. 
    
 2) Class TopCrypto: This class provides price and volume statistics for the top cryptocurrencies on the global market, ranked by market capitalisation. The class           uses the CoinMarketCap API to get the most recent data and saves a CSV file with all the requested data in the user's runtime directory. 
 
    • __init__: Initializing parameters to retrieve data from CoinMarketCap API 
    
    • Topcoins: topcoins(limit) returns market capitalization-based pricing and volume information for the top cryptocurrencies on the global market. Parameter 'limit'                 is user-defined. Eg: limit = 10 returns data for Top 10 cryptocurrencies ranked by market-cap. 
    
 3) Class CryptoPredict: The CryptoPredict class is used to forecast the Crypto Currency pair specified by the user based on the future time frame set by the user.
 
    • __init__: Initializes the token value.
    
    • API: Returns API token. 
    
    • pricePredict: Predict the crypto currency pairs futuristic price based on the mentioned end date.
    
    • visualizePredict: Visualise the predicted price against the mentioned timeframe. 
    
 4) Class CryptoNews: This class lets developers access rich formatted articles from crypto news sources from all around the world. One may get the complete                collection of crypto news, as well as news exclusive to a coin, by submitting the crypto currency's symbol as the parameter 
 
    • crypto_news: This function allows one to fetch news related to crypto currency. They can fetch the entire bag of crypto news and can also fetch news specific to                    a coin. 
    • crypto_news_df: This function converts the list of dictionaries to a data frame.
    
 5) Class CryptoCurrent: When a user calls this class, it will return real-time data (price) for the 30 most popular Cryptocurrencies in the form of CSV file saved         at their runtime path. The class uses CoinDesk API to get the latest pricing information for the cryptocurrencies. Price data is returned in the format                (Datetime, Symbol, Open, High, Low, Close) 
 
    • EndUrl: Creates the second half or the URL using start date, end data & symbol (from CryptoMain fuction). Concatenates to base URL and return the URL along with       the second half. 
    
    • CryptoData: Pings the API using the URL created above, receives the dataset, converts into readable dataframe format. Also drop timestamp column which was              earlier in seconds format and replaces it with Datetime column which is easy to comprehend. 
    
    • CryptoMain: The main method which explains the flow of the class by calling above methods one after the other. First, provides the top 30 currencies, initializes       3 pandas dataframe and uses iteration to ping API and store dataset one after the other in coin_df which is thereafter pushed to raw_df.
    

Usage: 

This package's objective is to serve as a one-stop shop for all things crypto. It aims to offer the user with as much information as possible to equip them with statistics and forecasts so that they can confidently envision where the market is headed, develop business strategies, and profit without much difficulty. The data that the user requests is publicly available on the internet; the package compiles it and delivers it to the end user in a legible format, so that they can decide how to use it to achieve their defined goals. There are multiple ways this handy package can be utilized, a few of them can be: 

• As a data source while creating a website to show captivating EDAs regarding price trend and providing investment suggestions to the users using the predictive price our package will suggest. 

• To create custom functions to handle each update, save the data in one of the supported backends, or just use the data to create a live trading application or algorithm trading bots. 

The possibilities of how the user intends to use this package are limitless and depend on the user’s objectives.

Discussion: 

In comparison to other developer packages now available on the web, the package performs effectively. Other packages, such as crypto-notify and cryptocompare, merely retrieve data from the internet, whereas ours can collect data for all crypto currencies, visualize it, and then analyse and forecast price trends. Other packages have limited capabilities, and it's usually 2-3 packages imported together that can equal our package's potential. 

With that in mind, every project has room for improvement, and our package is no exception. Quantitative Machine Learning Algorithms built with neural networks and decision trees, might be used by our CryptoPredict function to analyse the market's possible movements. The retrieved news can be programmed to fill a dashboard to present the news elegantly, and there may be several other interesting visualizations that can be added to our package.



For downloading the packages required use the following command: pip install -r requirements.txt



