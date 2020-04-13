class Deck:
    def __init__(self):
        self.color = []
        self.number = []
        self.ability = []
        self.ability_well = []
        self.decks = []



# class card_Table:
#     def __init__(self):
#         self.decks = []
        
    
    def creation_of_card(self):
        colors = ['Blue', 'Red', 'Yellow','Green']
        colors_argu = []
        number_argu = []
        for color_0 in colors:
            self.color.append(color_0)
            for n in range(0,10):
                self.number.append(n)
                colors_argu.append(color_0)
                number_argu.append(n)
                self.decks.append([color_0, n])
        for color_1 in colors:
            self.color.append(color_1)
            for n in range(1,10):
                self.number.append(n)
                colors_argu.append(color_1)
                number_argu.append(n)
                self.decks.append([color_1, n])
        return [colors_argu,number_argu]
        
    def creation_of_special_deck(self):
        colors_spe = ['Blue', 'Red', 'Yellow','Green']
        abilities = ['Cancelation','Direction', 'sum_tow']
        ability_special = []
        for color in colors_spe:
            self.color.append(color)
            for ability in abilities:
                self.ability.append(ability)
                ability_special.append([color,ability])
                self.decks.append([color,ability])
        for color in colors_spe:
            self.color.append(color)
            for ability in abilities:
                self.ability.append(ability)
                ability_special.append([color,ability])
                self.decks.append([color,ability])
        return ability_special
    def creation_of_willcard(self):
        ability_willcard = ['change_of_color', 'change_of_color+4','change_of_color', 'change_of_color+4','change_of_color', 
                                'change_of_color+4','change_of_color', 'change_of_color+4']
        ability_will = []
        for ability_w in ability_willcard:
            self.ability_well.append(ability_w)
            ability_will.append([ability_w])
            self.decks.append([ability_w])
        return ability_will
    
Deck_see= Deck()
num_color = Deck_see.creation_of_card()
creation = Deck_see.creation_of_special_deck()
will = Deck_see.creation_of_willcard()
total = Deck_see
print(total)



cumcolor = []
for p in range(0,len(num_color[0])):
    st = ""
    st += str(num_color[0][p])
    st +=  " " + str(num_color[1][p])
    cumcolor.append(st)
    st = ""













# class Deck_special:
#     def __init__(self,ability,color):
#         self.color = color
#         self.ability = ability

# class Table_s:
#     deck_spe = []



    


# mesa_s = Table_s()
# mesa_s.creation_of_special_deck()
# for deck_s in mesa_s.deck_spe:
#     print(deck_s.ability, deck_s.color)
    
# class Deck_willcard:
#     def __init__(self,ability):
#         self.ability = ability

# class Table_w:
#     def __init__(self):
#         self.deck_will = []
    


# mesa_w = Table_w()
# mesa_w.creation_of_willcard()
# for deck_w in mesa_w.deck_will:
#     print(deck_w.ability)







