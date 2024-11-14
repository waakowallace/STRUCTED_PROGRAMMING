#Arsenal's result
arsenal_result = input("Arsenal's result (win, draw, lose")
 #Manchester City's result
city_result = input("Manchester City's result (win, draw, lose): ")

# Calculate points for each team
if arsenal_result == "win":
    arsenal_points = 86 + 3
elif arsenal_result == "draw":
    arsenal_points = 86 + 1
else:
    arsenal_points = 86

if city_result == "win":
    city_points = 88 + 3
elif city_result == "draw":
    city_points = 88 + 1
else:
    city_points = 88
#finding the winner
if city_points > arsenal_points:
    print("Manchester City will be crowned champions")
elif arsenal_points > city_points:
    print("Arsenal will be crowned champions")
else:
    print("It's a tie! Both teams have the same points")


    



