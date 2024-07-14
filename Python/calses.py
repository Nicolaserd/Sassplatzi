class Person:
    def _init_(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"hola, mi nombre es {self.name} y tengo {self.age}")

person1 = Person("nicolas",27) 

person1.greet()