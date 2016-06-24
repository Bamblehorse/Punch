import random, sys, time

#Characters
nl = '\n'

#Menu Lists
fight_menu_list = ['what do you want to do?', 'Fight', 'Run', 'Items', 'Stats']

intro_menu_list = ['punch - pick an option', 'New Game', 'Load Game', 'Hiscores', 'Exit']

def manage(menu_id, option_number):
    """Sort Menu input"""
    menu_list = 0
    if menu_id == 'f': # Fight
        menu_list = fight_menu_list
        option = (menu_list[option_number])
        if option == 'Fight':
            fight()
        elif option == 'Run':
            print('\nYou run away like a coward.\n')
        elif option == 'Items':
            player.item_list()
            fight_menu.run(fight_menu_list, 'f')
        elif option == 'Stats':
            player.stats()
            fight_menu.run(fight_menu_list, 'f')
        
        
    elif menu_id == 'i': #Intro
        menu_list = intro_menu_list
        option = (menu_list[option_number])
        intro(option)
        
    else:
        print('Unknown Menu Id')

class Menu(object):
    """Menu Object"""
    def run(self, options, id):
        """Create a Menu"""
        self.name = id
        self.title = ( options[0].upper() ) # Uppercase title
        self.options = options[1:]          # Remove title          
        self.amount = len(self.options)
        self.display()
    
    def number_input(self, min, max):
        """Get an integer from the user"""
        prompt = nl + 'Enter a number <1-{0}>, then press ENTER:'.format(max)
        while True:
            try:
                user_data = int( input(prompt) ) # Try and convert input to integer
                if min <= user_data <= max:      # Check between min and max
                    print('You chose:', user_data)
                    manage(self.name, user_data)
                    return user_data             # Break display while loop
                    break
                else:
                    print('That number is out of range.')
                    self.display()
                    break
            except(ValueError, IndexError):
                print('Please enter a number.')
                self.display()
                break
        
    def display(self):
        """Display a Menu"""
        self.choice = 0
        while self.choice == 0:
            option_number = 1
            print(nl + self.title + nl*2)   #nl = New line escape character
            for option in self.options:
                print(option_number, '-', option)
                option_number += 1
            self.choice = self.number_input(1, self.amount) # Get integer input

class Being(object):
    
    def __init__(self, name, strength, hitpoints, gold, items):
        """Create a Being and pass its attributes as arguments"""
        self.name = name
        self.str = strength
        self.hp = hitpoints
        self.gold = gold
        self.items = items # List
        
    def stats(self):
        """Print out stats of Being"""
        print('\n--STATS--\n\nName: {0}\nStrength: {1}\nHitpoints: {2}\nGold: {3}\nItems: {4}\n'.format(self.name, self.str, self.hp, self.gold, self.items) )
        time.sleep(1)
        
    def item_list(self):
        """Print out items of Being"""
        print('\nYou search your bag and pockets and find:\n')
        for item in self.items:
            print('-', item)
        print(nl)
        time.sleep(1)

#'New Game', 'Load Game', 'Hiscores', 'Exit']            
def intro(option):
    """Start Game"""
    if option == 'New Game':
        print('Initializing game...')
        time.sleep(1)
        while True:
            intro_name = str( input('Choose a name(6-12 characters), then press ENTER:') )
            if 12 >= len(intro_name) >= 6:
                print( '\nHello {0}'.format(intro_name) )
                player.name = intro_name
                print('\nA figure approaches... Looks like he wants to fight...')
                fight_menu.run(fight_menu_list, 'f')
                break
            else:
                print('Please choose a name between 6 and 12 characters long.')
    if option == 'Load Game':
        print('\nFunction not available yet')
        intro_menu.run(intro_menu_list, 'i')
    if option == 'Hiscores':
        print('\nNo hiscores yet. Be the first to top them!')
        intro_menu.run(intro_menu_list, 'i')
    if option == 'Exit':
        sys.exit()

           
def fight():
    """Start a fight"""
    multiplier = random.randint(1,10)
    
    print(player.name, '-', 'HP:', player.hp)
    print(man.name, '-', 'HP:', man.hp)
    
    

# Menus    
intro_menu = Menu()
fight_menu = Menu()
# Beings
player = Being('', 2, 100, 1000, ['a map', 'matches', 'spare socks'])
man = Being('', 1, 100, 100, ['rag'])
# GAME STARTS HERE
intro_menu.run(intro_menu_list, 'i')

 





