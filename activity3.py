class Parrot:
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
Blu=Parrot('Blu','4')
Rio=Parrot('Rio','5')

#class variables
print("Blu is a "+Blu.species)
print("Rio is a "+Rio.species)

#instance variables
print(Blu.name +" is "+Blu.age+" years old")
print(Rio.name +" is "+Rio.age+" years old")