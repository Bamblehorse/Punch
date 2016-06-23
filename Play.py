# Functions

def Intro(action):
    print('Intro', action)

def Fight(action):
    print('fight menu', action)

def pick(menu_name ,action):
    
    """Process Menu choice to run relevant function"""
    print(menu_name)
    #pick_dic[menu_name]

    
#Classes

class Menu(object):
    
    def __init__(self, name, title, options):
        """Create a Menu"""
        self.name = name
        self.title = title
        self.options = options
    def start(self):
        """Display Menu"""
        options = self.options
        title = self.title
        menu_item = 1
        number = 1
        # Display Menu
        print(title,'\n')
        for option in options:           
            print('{0}. {1}'.format(number, option))
            number += 1
        # Take user input
        number -= 1 # Number of options
        while True:
            try:
                menu_item = int(input('\nType a number between 1 and {0}, then press ENTER: '.format(number) ) )
                if number >= menu_item > 0:
                    menu_item -= 1 # Correct for list starting at 0
                    print('You selected option {0}, {1}.\n'.format(menu_item + 1, options[menu_item]) )
                    print('menu name is', self.name)
                    pick(self.name, options[menu_item])
                    break
                else:
                    print('\nThat is not on the menu... Please try again...\n')
                    self.start()
                    break
            except (ValueError, IndexError):
                print('\nThat is not on the menu... Please try again...\n')
                self.start()
                break
        
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


    
#MENUS
Intro_Menu = Menu('intro', 'PUNCH - Pick an option', ['New Game', 'Load Game', 'Exit'])
Fight_Menu = Menu('fight', 'What do you want to do?', ['Punch', 'Run', 'Items', 'Stats'])

# GAME STARTS HERE
Intro_Menu.start()


Fight_Menu.start()
J = Being('Jon', 1, 100, ['Sword', 'Shield', 'Hat'], 10000)


J.stats()



