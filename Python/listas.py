# es una lista
a =[1,2,3,4,5,6]
# slice [:]
b = a [:]
print(a)
print(b)
# espacio de memoria  es diferente 
print(id(a))
print(id(b))
# agregar 
a.append(7)
print(a)
print(b)
to_do = ["hacer comida", "no dejarla quemar", "respirar","muy importante"]
print(to_do)
string_num = [1,2,3,"cuatro"]
mix = [[1,"dos"],True,False]
print("primer elemento",mix[0][0])
print("slicing",mix[0:2])
