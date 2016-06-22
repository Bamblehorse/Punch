class Menu(object):
    
    def __init__(self, name, options):
        """Create a Menu"""
        self.name = name
        self.options = options
        
    def display(self):
        number = 1
        print(self.name,'\n')
        for option in self.options:           
            print('{0}. {1}'.format(number, option))
            number += 1

M = Menu('Options', ['Punch', 'Run', 'flip', 2,3,4,5,6,7,8])
M.display()