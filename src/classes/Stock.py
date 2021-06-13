
class Stock():
    """
    Clase para manejo de acciones.
    Los precios historicos los almacena en un diccionario.
    Se considera el precio de cierre.
    """
    
    def __init__(self, name, path_data):
        self.name=name
        self.path_data=path_data+name
        self.prices_ = {}

        # se ejecuta al iniciar el objeto
        self.load_prices_()
        
    def load_prices_(self):
        """
        Método interno para cargar los precios por fecha.
        """
        
        try:
            prices = open(self.path_data,'r')
            
            k = 0
            for p in prices:
                k +=1

                # saltamos encabezado
                if k == 1:
                    continue
                
                cols = p.split(',')
                self.prices_[cols[0]] = float(cols[4])
                
        except:
            print(f'No encontramos la accion {self.name}')
        
        
    def price_per_date(self, date):
        """
        Recibe fecha en formato YYYY-mm-dd y retorna el precio de cierre de la accion, si existe.
        """
        if not date in self.prices_.keys():
            return -1 # no hay precio para tal dia
        
        return self.prices_.get(date)