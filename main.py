if __name__ == "__main__":
    def registra_robot(robot_prodotti: list[Robot], robot:Robot):
        for x in robot_prodotti:
            if(x.codice==robot.codice):
                raise ValueError
        list.append(robot)