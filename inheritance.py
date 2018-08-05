class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name: "+self.last_name)
        print("Eye Color: "+self.eye_color)
    

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child ocnstructor class")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toy = number_of_toys

    def show_info(self):
        print("Last name: "+self.last_name)
        print("Eye Color: "+self.eye_color)
        print("Number of toys: "+str(self.number_of_toy))
        
    

Paparizou = Parent("Tony","gray")        
print()
Paparizaki = Child("Lena","blue",14)        
Paparizaki.show_info()
