number=[15,42,73,29,91,50]
 #intialize a variable 
big_nmb=number[0]
for num in number[15:]:
    if num>big_nmb:
     big_nmb=num
     print(big_nmb)