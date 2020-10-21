import matplotlib.pyplot as plt

maze = []
walls = []
Coordinates = []
new_x=[]
new_y=[]

with open(r"C:\Users\racha\OneDrive\Desktop\maze.txt", 'r') as f:
    line = f.readlines() #reading the lines in the file
    
    for element in line:
        if element == 'True\n': 
            walls.append(0) 
        elif element == "False\n":
            walls.append(1)
        if len(walls) == 51:
            maze.append(walls)
            walls = []
    
#starting point
def Startpoint_input():
    for i in range(0,2):
        number = float(input("Enter your coordinates: "))
        if number<50 and number>0:       
            Coordinates.append(number)
        else:
            print ('Please re-enter your coordinates.')
            Coordinates.clear()
            Startpoint_input() #rerun loop function
            break
Startpoint_input()

#Checking for walls
def Startpoint_Coords():
    x = Coordinates[0] 
    y = Coordinates[1]
    print(x,y)
    #determining of value of coord
    List1 = maze[int(y)]
    List2 = List1[int(x)]
    if List2 == 1:
        new_x.append(x+0.5)
        new_y.append(y+0.5)
    else:
        print("Coordinate is a wall, please re-enter your coordinate")
        Coordinates.clear()
        Startpoint_input()
        Startpoint_Coords()
Startpoint_Coords()

#visualising maze
plt.style.use('grayscale')
plt.pcolormesh(maze)
plt.axes().set_aspect('equal') #set the x and y axes to the same scale
#plt.xticks([]) # remove the tick marks by setting to an empty list
#plt.yticks([]) # remove the tick marks by setting to an empty list

#plotting points
endpoint = plt.plot(47.5,1.5,'ro')
startpoint = plt.plot(new_x[0],new_y[0],'go')

plt.show()

