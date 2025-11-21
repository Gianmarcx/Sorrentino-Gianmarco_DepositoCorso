class Dipendente:
    def __init__(self,nome,eta,ruolo,badge):
        self.__nome = nome
        self.__eta = eta
        self.__ruolo = ruolo
        self.__badge = badge
        
        
    def get__nome(self):
        return self.__nome
    
    def set__nome(self,nome):
        self.__nome = nome
        
    def get__eta(self):
        return self.__eta
    
    def set__eta(self, eta):
        self.__eta = eta

    def get__ruolo(self):
        return self.__ruolo

    def set__ruolo(self, ruolo):
            self.__ruolo = ruolo
    
    def get__badge(self):
        return self.__badge
    
    def set__badge(self, badge):
        self.__badge = badge

