def Condition(lst):
    """
    Checks the boundary conditions that all entries are below 100.
    """
    flag=True
    if (lst[0] not in range(0, 101)):
        flag=False
    if (lst[1] not in range(-1, 2)):
        flag=False
    if (len(lst)==3):
        if (lst[2] not in range(0, 101)):
            flag=False
    return flag


def Mod_of_Difference(a, b):
    """
    Gives the Magnitude of Difference between the 2 inputs.
    """
    if (a<b):
        return b-a 
    return a-b


def Floors_To_Travel(lift, floor):
    """
    Tells the number of floors the lift has to travel
    before reaching the desired floor.
    """
    if (lift[1]==floor[1]) and (floor[0] in range(lift[0], lift[2], lift[1])):      #checks the condition that is the floor on the way where the lift is going.
        return Mod_of_Difference(floor[0], lift[0])
    elif (lift[1]==0):                                                              #checks the condition if lift is stationary.
        return Mod_of_Difference(floor[0], lift[0])
    else:
        return Mod_of_Difference(lift[2], floor[0]) + Mod_of_Difference(lift[2], lift[0])
    

l1= [int(x) for x in input().split(" ")]
l2= [int(x) for x in input().split(" ")]
l3= [int(x) for x in input().split(" ")]
floor = [int(x) for x in input().split(" ")]

if (Condition(l1) and Condition(l2) and Condition(l3) and Condition(floor)):
    Closest_lift = 1
    lft1, lft2, lft3 = Floors_To_Travel(l1, floor), Floors_To_Travel(l2, floor), Floors_To_Travel(l3, floor)  #Number of floors to travel
    if (lft1>lft2):
        Closest_lift = 2
        lft1 = lft2
    if (lft1>lft3):
        Closest_lift = 3
    print(Closest_lift)
else:
    print("0")