# magicMethod(param) adında bir metod yazın.Bu ele bir metod olsun ki argument olaraq verilən param
# arraydirsə onun içindəki bütün elementləri ekrana çap elesin
# obyektdirsə onun properylerini ekrana cap etsin
# rəqəmdirsə kvadratını ekrana çap etsin
# stringdirsə cüt yerdə duran hərfləri böyük hərfə çevirsin

# 1

def magicMethod(param):
  for x in param:
    print(x)

param = ["Əli", "Vəli", "Mehman"]

magicMethod(param)

#

# 2
class Animal(object):
    def __init__(self):
        self.eyes = 2
        self.name = 'Dog'
        self.color= 'Spotted'
        self.legs= 4
        self.age  = 10
        self.kids = 0
 
 
animal = Animal()
animal.tail = 1
 
temp = vars(animal)
for item in temp:
    print(item, ':', temp[item])


# 


# 3
def magicMethod(param):
  for x in param:
    print(x**2)

param = [1,2,3,4]

magicMethod(param)
# 




# 4
def magicMethod(param):
  for s in param:
    print()

param = set([1, 3, 5 ,7,9,11])
s = "salam aleykum"
print("".join(c.upper() if i in param else c for i, c in enumerate(s)))


magicMethod(param)
# 