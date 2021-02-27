from Cat import Cat
from Dog import Dog

class InformDogCat():
  
    __instance = None

    def __new__(cls, check):
        if InformDogCat.__instance is None:
            InformDogCat.__instance = object.__new__(cls)
            InformDogCat.__instance.__check= check
        return InformDogCat.__instance


    def check(type):
         
        if type == '1':
            typeCatDod  = Cat()
            typeCatDod.value()
            description  =typeCatDod.type
            s.append (description) 
            print(description) 
        elif type == '2':
             typeCatDod = Dog()
             typeCatDod.value()
             description = typeCatDod.type
             s.append (description) 
             print(description) 
        elif type == 'histórico':
             print(s) 
s = []



if __name__ == "__main__":
   num = [] 

   information = input("informe 1, 2, ou histórico: ")
   while information != "":
    
    type=InformDogCat.check(information)
    information = input("informe 1, 2, ou histórico: ")
   
   print("")