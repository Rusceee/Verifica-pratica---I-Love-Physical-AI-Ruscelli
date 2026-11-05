if __name__ == "__main__":
    def registra_robot(robot_prodotti: list[Robot], robot:Robot):
        for x in robot_prodotti:
            if(x.codice==robot.codice):
                raise ValueError
        list.append(robot)
    def cerca_robot(robot_prodotti: list[Robot], codice:str):
        for x in robot_prodotti
            if(x.codice==codice):
                return x
        return None
    def riepilogo_robot(nome_azienda:str , robot_prodotti: list[Robot]):
        for x in robot_prodotti:
            print(x.modello)
            print(x.stato)
            print(x.pesoComponenti)