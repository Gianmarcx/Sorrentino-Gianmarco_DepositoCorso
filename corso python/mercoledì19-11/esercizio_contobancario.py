class ContoBancario:
    def __init__(self, titolare,saldo=50000.00):
        self.__titolare = "Gianmarco"
        self.__saldo = 50000.00
        self.set_titolare(titolare)
        self.set_saldo(saldo)
        
        
    def set_titolare(self, titolare):
        self.__titolare = titolare

    def get_titolare(self):
        return self.__titolare
    
    def deposita(self, importo):
            if importo > 0:
                print("Inserire importo: ")
                self.__saldo += importo
            
            else: 
                print("Importo non valido!" )
                
    def preleva(self,importo):
        importo = print("Inserire importo: ")
        if importo > 0:
            if importo <= self.__saldo:
                self.__saldo -= importo
                print("Prelievo effettuato. Il tuo saldo ora è: {self.__saldo.2f}")
            else:
                print("Saldo insufficiente!")
        else:
            print("Importo non valido!")
             
        