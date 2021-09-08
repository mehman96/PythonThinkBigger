class Base(object):
    def __init__(self,name,prop1,prop2):
        self.name=name
        self.prop1=prop1
        self.__prop2=prop2



a1=Base("something1", "","")
a2=Base("something2","","" )

print(a1.name,a1.prop1)
print(a2.name,a2.prop2)