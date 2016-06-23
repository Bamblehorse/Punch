class Menu(object):
    """Menu Object"""
    def create(self, title, options):
        """Create a Menu"""
        self.title = upper(title)
        self.options = options
        
        print(title, options)