classname = ["john","gilbert","emma","gabriella"]
name=0
while name <len(classname):
    print(classname[name])
    name+=1




#no2
districts=["mukono","byegere","kampala","lira","kimpa","fortpotal","uma","jango","arua","sonde"]
districts.append("masaka")
districts.append("bukunja")
districts.append("hoyima")
print(districts)

#dispalying the size
print(len(districts))
for w in districts:
    print(w)
#removing the index
districts.remove("mukono")



#using the while loop
district = 0
while district < (districts):
    print(districts[district])
    district+=1
