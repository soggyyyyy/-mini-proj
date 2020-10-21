import matplotlib.pyplot as plt

maze = []
walls = []
Coordinates = []

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
for i in range(0,10):
    number = float(input("Enter your coordinates: "))
    if number<51 and number>0:       
        Coordinates.append(number)
    if len(Coordinates)==2:
        break

print(Coordinates)
x = Coordinates[0]
y = Coordinates[1]

plt.style.use('grayscale')
plt.pcolormesh(maze)
plt.axes().set_aspect('equal') #set the x and y axes to the same scale
#plt.xticks([]) # remove the tick marks by setting to an empty list
#plt.yticks([]) # remove the tick marks by setting to an empty list

#specify location of points
endpoint = plt.plot(47.5,1.5,'ro')
startpoint = plt.plot (x,y,'go')

plt.show()

