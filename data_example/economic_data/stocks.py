from economic_data.config import fred, px, pd, plt

def economic_data():
    sp_search = fred.search('S&P', order_by='popularity')
    sp_search.head()
    
def get_data_from_fred():
    sp500 = fred.get_series(series_id='SP500')
    sp500.plot(figsize=(10, 5), title='S&P 500', lw=2)
    plt.show()