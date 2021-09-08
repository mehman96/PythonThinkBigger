# exploreObject(obj) adında bir metod yazın. Bu metod argument olaraq verilən istənilən obyektin bütün xüsusiyyətlərini
# hansı property-ləri olduğunu və onların value-sunu
# hansı metodlarının olduğunu və nə return etdiyini

class Person:
 def _init_(self, name, surname, age):
       self.name = name
       self.surname = surname
       self.age = age
     
 def exploreObject(obj):
    for property, value in vars(obj).items():
       print(property, ":", value) 
       method_list = [method for method in dir(Person) if method.startswith('__') is False]       
    print (method_list)

personn = Person("Mehman", "Mirzeyev", 20)

exploreObject(personn)



