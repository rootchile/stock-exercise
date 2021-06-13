import os
import re
from dotenv import load_dotenv
load_dotenv()

from src.classes.Portfolio import Portfolio
from src.classes.Stock import Stock

from datetime import datetime

if __name__ == '__main__':
    
    path = os.environ['PATH_DATA']
    
    # Acciones de ejemplo
    # Amazon, Globant
    amzn = Stock(name='AMZN',path_data=path)
    glob = Stock(name='GLOB',path_data=path)
    
    ## Generamos portafolio
    
    portafolio = Portfolio()
    
    # stocks port
    portafolio.add_stock(amzn)
    portafolio.add_stock(glob)
    
    
    start = datetime.strptime('2020-06-20', '%Y-%m-%d')
    end = datetime.strptime('2021-06-12', '%Y-%m-%d')
    profit, profit_ratio = portafolio.calculate_profit(start, end)
    annualized_return = portafolio.calculate_annualized_return(start, end)

    print(f'profit: {profit} \n return {profit_ratio} \n annualized: {annualized_return}')    
    exit()