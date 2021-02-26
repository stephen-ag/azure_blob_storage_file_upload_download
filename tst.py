import os

v= os.getcwd()
i= os.path.basename(__file__)
m= os.path.abspath(__file__)
print(os.path.dirname(__file__))

data=os.path.dirname(os.path.abspath(__file__))

print(v)
print(i)
print(m)
#print(t)
print(data)
