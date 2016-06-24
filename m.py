#Characters
nl = '\n'

#Menu Lists
fight_menu_list = ['what do you want to do?', 'Punch', 'Run', 'Items', 'Stats']

intro_menu_list = ['punch - pick an option', 'New Game', 'Load Game', 'Hiscores', 'Exit']

def manage(menu_id, option_number):
    """Sort Menu input"""
    menu_list = 0
    if menu_id == 'f': # Fight
        menu_list = fight_menu_list
        option = (menu_list[option_number])
        if option == 'Punch':
            fight(option)
        elif option == 'Run':
            print("You run away like a coward.")
        elif option == 'Items':
            player.items()
        elif option == 'Stats':
            player.stats()
        
        
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
    
    def __init__(self, name, strength, hitpoints, items, gold):
        """Create a Being and pass its attributes as arguments"""
        self.name = name
        self.str = strength
        self.hp = hitpoints
        self.items = items # List
        self.gold = gold
        
    def stats(self):
        print('Name: {0}\nStrength: {1}\nHitpoints: {2}\nItems: {3}\nGold: {4}'.format(self.name, self.str, self.hp, self.items, self.gold) )
        
    def items(self):
        for item in items:
            print(item)

def intro(option):
    """Start Game"""

            
def fight(weapon):
    """Start a fight"""
    pass

# GAME STARTS HERE
intro_menu = Menu()
intro_menu.run(intro_menu_list, 'i')
    
fight_menu = Menu()
fight_menu.run(fight_menu_list, 'f')

 





