"""fruits=["mango","apple ","jambula","pumpkin"]
 #use loops 
 
for fruit in fruits:
    print(fruit)

print(help(fruits))    
#checking size 
print(len(fruits)) 
print("stone" in fruits )
print(type(fruits))
 
 
 
 #duplication is allowed
fruits[0]="pinapple"
#inrate
#for fruit in fruits:
    #print(fruit)
    
    
#if u want to add an objject use append
fruits.append("lemon")
print(fruits)


#remove
fruits.remove("mango")
print(fruits)
 #cuckmsize of a list 
coursework=[34.4,45,23,9,10.0]
print(len(coursework))
print(fruits[3])
print(fruits[2])
print(fruits[1])
print(fruits[0])
 
fruits = ["mango", "apple", "jambula", "pumpkin"]
fruit = 0
while fruit<len (fruits):
  print(fruits[fruit])
  fruit+= 1
  #MUTABLE
L=[1,2,3]
L[2]=5
print(L)



##FLOW DIVISION 
APPLES=12
PEOPLE=4
DIVISION =APPLES//PEOPLE
print(DIVISION)
print(8//2)
print(-8//2)
"""
# FINDING THE NUMBER OF ELEMENTS 
number=[2,3,4,5,6,7]
 # using a for loop 

total=0
sum=0
for n in number:
    total+=n
    sum+=1
#avarage
avarage=total/sum
print('AVARAGE IS ',avarage)
