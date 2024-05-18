class Friends:
    # constructor for the class 
    def __init__(self, name, age, gender, fav_color):
        self.name = name
        self.age = age
        self.gender = gender
        self.fav_color = fav_color
    
    # getters - returns the variables
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_gender(self):
        return self.gender
    
    def get_fav_color(self):
        return self.fav_color
    
    # setters - used to modify the variables
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_fav_color(self, fav_color):
        self.name = fav_color

        