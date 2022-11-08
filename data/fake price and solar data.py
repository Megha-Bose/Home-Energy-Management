import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

def price_and_solar_parser(start_date, freq='15T'):
    date_list = pd.date_range(start=start_date+' 00:00:00', end=start_date+' 23:45:00', freq=freq)
    date_list_size = len(date_list)
    length = np.random.randint(int(0.7*date_list_size), date_list_size)

    x = np.linspace(-length,length)
    y = -0.5*(x)**2+0.05*x

    # Fake price data
    x_prc = np.linspace(-length, length, num=date_list_size)
    y_prc = -0.5*(x_prc)**2+0.05*x_prc
    y_prc += (max(abs(y_prc))+5000) 
    price_data = y_prc/1000

    # Fake solar data
    ar = list(y + max(abs(y)))
    zer1 = [0]*int((0.3*date_list_size))
    zer2 = [0]*(date_list_size - (len(zer1) + len(y)))
    solar = zer1 + ar + zer2

    data = pd.DataFrame()
    data['datetime'] = date_list
    data['price'] = price_data
    data['solar_output'] = solar
    return data