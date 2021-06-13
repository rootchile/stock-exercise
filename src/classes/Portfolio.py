
from datetime import datetime, timedelta

class Portfolio():
    """
    Una coleccion de Stock
    """
    
    def __init__(self):
        self.stocks = []
        
    def add_stock(self,stock):
        
        if stock not in self.stocks:
            self.stocks.append(stock)
            return True
        return False
    
    def get_stocks(self):
        return self.stocks
    
    
    def calculate_profit(self, start, end):
            
        profit = 0
        init = 0
        for stock in self.stocks:
            init_price = self.start_price_(stock, start)
            end_price = self.end_price_(stock, end)
            profit += end_price-init_price
            init += init_price
        
        profit_ratio = 0    
        if init>0:
            profit_ratio = profit/init
            
        return profit, profit_ratio
    
    def calculate_annualized_return(self, start, end):
        
        periods = 365/(end-start).days
        profit, profit_ratio = self.calculate_profit(start,end)
        
        annualized_return = ((1+profit_ratio)**(periods))-1

        return annualized_return
        
        
    
    def start_price_(self, stock, start):
        """
        Busca precio más cercano a la fecha inicial
        """
        dates = [start + timedelta(days=x) for x in range(0, 100)]
        
        for date in dates:
            price = stock.price_per_date(date.strftime("%Y-%m-%d"))
            if price > 0:
                return price
        # No hay precio
        return -1
        
    def end_price_(self, stock, end):
        """
        Busca precio más cercano a la fecha termino
        """
        dates = [end + timedelta(days=-x) for x in range(0, 100)]
        
        for date in dates:
            price = stock.price_per_date(date.strftime("%Y-%m-%d"))
            if price > 0:
                return price
        # No hay precio
        return -1