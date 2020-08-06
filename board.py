from pro import total


class Board:
    def __init__(self):
        self.deck_table = []
    
    def cart_of_table(self):
        card_table = total.pop(0)
        t_b.append(card_table)
    def Table(self):
        print ("""                    _____________________________________________                  
                    |                                            |  
                    |                                            |
                    |                                            |
                    |                                            |
                    |                                            |
                    |                {}                 |
                    |                                            |
                    |                                            |
                    |                                            |
                    |                                            |
                    |                                            | 
                    |____________________________________________|
                                                                """.format(self.deck_table[0]))
        
    
PlayerList = []

def input_player():
    check = '234'
    inputopcion = input("Entre numero de player:")
    if len(inputopcion) != 1:
        print("NO es valida")
    while inputopcion not in check:
        print("NO es valida")
        inputopcion = input("Entre numero de player:")
    return int(inputopcion)

def creator_of_player():
    verify_entre = input_player()
    for v_p in range(verify_entre):
        input_name = input("Entre nombre player{}:".format(v_p + 1))
        if len(input_name) == 0 or len(input_name) > 20:
            print("El nombre no es valido, vuelve a internar")
            input_name = input("Entre nombre player{}:".format(v_p + 1))
        PlayerList.append(input_name)
    return PlayerList

input_player()
creator_of_player()
    
    

Ult_board = Board()
t_b = Ult_board.deck_table
Ult_board.cart_of_table()
tabla = Ult_board.Table()
ups_down = t_b[::-1]
t_b = ups_down


