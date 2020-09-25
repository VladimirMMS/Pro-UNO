from card import Card 

colors = ['Blue', 'Red', 'Yellow','Green']
abilitys = ['Cancelation', 'Direction', 'Sum_two']
will_abilitys = ['change_of_color', 'change_of_color+4']

class Deck():
    def __init__(self):
        self.decks = []
        self.decks_compi = []



    def create_cards(self):
        
        for number in range(0,10):
            for color in colors:
                self.decks.append(Card(color = color, number = number, ability = ''))
               
            
        for number in range(1,10):
            for color in colors:
                self.decks.append(Card(color = color, number = number, ability = ''))
        
        for card in self.decks:
            self.decks_compi.append([card.color, card.number])

    def create_specialcards(self):
        
        for color in colors:
            for ability in abilitys:
                self.decks.append(Card(color = color, number = '', ability = ability))

        for color in colors:
            for ability in abilitys:
                self.decks.append(Card(color = color, number = '', ability = ability))
               
        
        for card in range(76,100):
            self.decks_compi.append([self.decks[card].color, self.decks[card].ability])
        
        for will_ability in will_abilitys:
            for ran_will in range(0,4):
                self.decks.append(Card(color = '', number = '', ability = will_ability))
               
        
        for will_ran in range(100, 108):
            self.decks_compi.append([self.decks[will_ran].ability])
        