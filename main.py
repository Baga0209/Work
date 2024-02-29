

class Product:
    def __init__(self, title = '', calorific=1, cost=1):
        if calorific<0 or cost<0:
             raise ValueError('Значение атрибутов calorific и cost может быть только положительным')
        else:
            self.title = title
            self.calorific = calorific
            self.cost = cost      
            
class Ingredient():
    def __init__(self, product, weight=0):
        if weight<0:
             raise ValueError('Значение атрибута weight может быть только положительным')
        else:
            self.weight = weight
            self.product = product
            
    def add_product(self):
        append.self.product(Product(self))
    
    def get_calorific(self, weight, calorific):
        self.weight = weight
        self.calorific = calorific
        return self.weight/100*self.calorific
    
    def get_cost(self):
        self.weight/100*self.cost 
        return self.weight/100*self.cost
    
class Pizza():
    def __init__(self, title = '', ingredients = []):
        self.title = title
        self.ingredients = ingredients
        
    def add_ingredients(self):
        append.self.ingredients(Ingredient(self))
        
    def get_calorific(self, calorific):
        summa_1 = 0
        for i in self.calorific:
            summa_1 += self.calorific
        return summa_1 
    
    def get_cost(self, cost):
        summa_2 = 0
        for i in self.cost:
            summa_2 += self.cost
        return summa_2