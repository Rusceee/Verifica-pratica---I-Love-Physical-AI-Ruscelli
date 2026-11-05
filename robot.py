class Robot:
    def __init__(self, codice: str, modello: str, applicazione: str, peso_massimo_componenti_kg: float, stato: str) -> None:
        this.codice=codice
        this.modello=modello
        this.applicazione=applicazione
        this.peso_massimo_componenti_kg=peso_massimo_componenti_kg
        this.stato=stato
        this.componenti = []
    
    def cercaComponente(self, codiceComponente:str):
        for x in this.componenti:
            if(x.codice == codiceComponente):
                return x
        return
    def pesoComponenti(self):
        a = 0
        for x in this.componenti:
            a = a+x.peso_kg
        return a
    def aggiungi_componente(self, componente:Componente)
        this.componenti.append(componente)
    
    def rimuovi_componente(self, codice:str):
        a=0
        for x in this.componenti:
            
            if(x.codice==codice)
                componenti.remove(a)
            a++
        return None 
            