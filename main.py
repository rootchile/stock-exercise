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

    
    print("-"*20,"Fintual Test","-"*20)
    
    regex_date = '\d{4}-\d{2}-\d{2}'
    date_start_flag = False
    date_end_flag = False
    
    while not date_start_flag:
        date_start = input('Fecha Inicial [aaaa-mm-dd]:')
        
        if not re.match(regex_date, date_start):
            print('\nUps, fecha mal ingresada, prueba de nuevo =(. Ejemplo: 2021-01-01')
        else:
            date_start_flag = True
    
    while not date_end_flag:
        date_end = input('Fecha Término [aaaa-mm-dd]:')
    
        if not re.match(regex_date, date_end):
            print('\nUps, fecha mal ingresada, prueba de nuevo =(. Ejemplo: 2021-01-01')
        else:
            date_end_flag = True
            

    start = datetime.strptime(date_start, '%Y-%m-%d')
    end = datetime.strptime(date_end, '%Y-%m-%d')
        
    if start > end:
        print('Fecha inicio no puede ser mayor a fecha termino')
        exit()
    
    
    profit, profit_ratio = portafolio.calculate_profit(start, end)
    annualized_return = portafolio.calculate_annualized_return(start, end)
    print("="*40)
    print(f'Profit: USD {round(profit,2)} \nReturn {round(profit_ratio*100,2)}% \nAnnualized: {round(annualized_return*100,2)}%')    
    print("="*40)
    
    
    