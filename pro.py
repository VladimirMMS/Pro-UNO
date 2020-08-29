class Deck:
    def __init__(self):
        self.color = []
        self.number = []
        self.ability = []
        self.ability_well = []
        self.decks = []



#Here is the creation of the card, the mazo is one honder heigth.
# there especial card, normal card  and well card.
    
    def create_card(self):
        #Here is the normal card.
        colors = ['Blue', 'Red', 'Yellow','Green']
        #In this list we save the color and the number of the decks.
        
        colors_argu = []
        number_argu = []
        
        #Creation of the card that includes the number zero.
        
        for color_0 in colors:
            self.color.append(color_0)
            for n in range(0, 10):
                self.number.append(n)
                colors_argu.append(color_0)
                number_argu.append(n)
                self.decks.append([color_0, n])#It save in the total decks
                
        #Creation of the card that includes the number one.
        for color_1 in colors:
            self.color.append(color_1)
            for n in range(1, 10):
                self.number.append(n)
                colors_argu.append(color_1)
                number_argu.append(n)
                self.decks.append([color_1, n])#It save in the total decks
        print(len(number_argu))
        return [colors_argu, number_argu]
        


#How his name say, it's the creation of the special card.
#these don't have number, just color and ability.

    def create_specialdeck(self):
        #Here we create the special cards-
        #below we can see their name and their ability stored in a list
        
        colors_spe = ['Blue', 'Red', 'Yellow','Green']
        abilities = ['Cancelation','Direction', 'sum_two']
        #This list is to store all the special cards created
        
        ability_special = []
        
        #The process the creation of the special card
        
        for color in colors_spe:
            self.color.append(color)
            for ability in abilities:
                self.ability.append(ability)
                ability_special.append([color, ability])
                self.decks.append([color, ability])#It save in the total decks

#I repeated the same above to create the exact
#number of the special card.

        for color in colors_spe:
            self.color.append(color)
            for ability in abilities:
                self.ability.append(ability)
                ability_special.append([color, ability])
                self.decks.append([color, ability])#It save in the total decks
        print(len(self.d))
        return ability_special


#Here are the will card, those just have ability.

    def create_willcard(self):
#this cards just have one position, because don't have number and colors.

        ability_willcard = ['change_of_color', 'change_of_color+4','change_of_color', 'change_of_color+4', 'change_of_color', 
        'change_of_color+4',' change_of_color', 'change_of_color+4']

#Here store all the will_cards

        ability_will = []
#The process of creation.
        for ability_w in ability_willcard:
            self.ability_well.append(ability_w)
            ability_will.append([ability_w])
            self.decks.append([ability_w])##It save in the total decks
        return ability_will

#OBJECT OF THE CARD THAT CREATED. 
deck_see = Deck()
num_color = deck_see.create_card()
creation = deck_see.create_specialdeck()
will = deck_see.create_willcard()
last_decks = deck_see


total = last_decks.decks
