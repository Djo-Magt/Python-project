from datetime import date, timedelta
from pprint import pprint
import yfinance as yf

def get_rates(symbols, days=30):
    end_date = date.today()
    starter = end_date - timedelta(days=days)
    
    #import des données via module sous format "panda"
    data = yf.download(symbols,  start=f"{starter}", end=f"{end_date}")
    
    #tranformation des données pour avoir les date en index
    data_to_dict = data['Adj Close'].to_dict(orient='index')
    #transformation des dates
    formatted_data = {key.strftime('%Y-%m-%d'): value for key, value in data_to_dict.items()}

    all_rates = {symbol:[] for symbol in symbols}
    all_days = sorted(formatted_data.keys())
    
    for each_day in all_days:
        [all_rates[symbol].append(rate) for symbol, rate in formatted_data.get(each_day).items()]
        
    return all_days, all_rates



if __name__ == '__main__':
    _ , rates = get_rates(symbols = ['IBM', 'AAPL'])
    pprint(_)
    pprint(rates.keys())
    pprint(type(rates.keys()))
