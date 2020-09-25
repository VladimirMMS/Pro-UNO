from card import Card 

colors = ['Blue', 'Red', 'Yellow','Green']
abilitys = ['Cancelation', 'Direction', 'Sum_two']
will_abilitys = ['change_of_color', 'change_of_color+4']

class Deck():
    def __init__(self):
        self.decks = []
        self.decks_compi = []



    def create_cards(self):
        
        color_argument = []
        number_argument = []
        
        for number in range(0,10):
            for color in colors:
                self.decks.append(Card(color = color, number = number, ability = ''))
                color_argument.append(Card(color = color, number ='', ability = ''))
                number_argument.append(Card(color = '', number =number, ability = ''))
            
        for number in range(1,10):
            for color in colors:
                self.decks.append(Card(color = color, number = number, ability = ''))
                color_argument.append(Card(color = color, number ='', ability = ''))
                number_argument.append(Card(color = '', number =number, ability = ''))
        
        for ran in range(len(color_argument)):
            self.decks_compi.append([color_argument[ran].color, number_argument[ran].number])

    def create_specialcards(self):
        
        color_argument = []
        ability_argument = []
        will_argument = []
        
        for color in colors:
            for ability in abilitys:
                self.decks.append(Card(color = color, number = '', ability = ability))
                color_argument.append(Card(color = color, number = '', ability = ''))
                ability_argument.append(Card(color = '', number = '', ability = ability))
        
        for color in colors:
            for ability in abilitys:
                self.decks.append(Card(color = color, number = '', ability = ability))
                color_argument.append(Card(color = color, number = '', ability = ''))
                ability_argument.append(Card(color = '', number = '', ability = ability ))
        
        
        for ran in range(len(color_argument)):
            self.decks_compi.append([color_argument[ran].color, ability_argument[ran].ability])
        
        for will_ability in will_abilitys:
            for ran_will in range(0,4):
                self.decks.append(Card(color = '', number = '', ability = will_ability))
                will_argument.append(Card(color = '', number = '', ability = will_ability))
        
        for will_ran in range(len(will_argument)):
            self.decks_compi.append([will_argument[will_ran].ability])
        

card = Deck()
normal_creation = card.create_cards()
special_creation = card.create_specialcards()
total_card = card.decks_compi
