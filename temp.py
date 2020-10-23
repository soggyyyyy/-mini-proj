import matplotlib.pyplot as plt

maze = []
walls = []
Start =[]
end = [47,1]

with open(r"C:\Users\racha\OneDrive\Desktop\maze.txt", 'r') as f:
    line = f.readlines() #reading the lines in the file
    
    for element in line:
        if element == 'True\n': 
            walls.append(1) 
        elif element == "False\n":
            walls.append(0)
        if len(walls) == 51:
            maze.append(walls)
            walls = []

#starting point
def Startpoint_input():
    for i in range(0,2):
        number = float(input("Enter your coordinates: "))
        if number<50 and number>0:       
            Start.append(int(number))
        else:
            print ('Out of bounds, please re-enter your coordinates.')
            Start.clear()
            Startpoint_input() #rerun loop function
            break
Startpoint_input()

#Checking for walls
def Startpoint_Coords():
    #determining of value of coord
    List1 = maze[Start[0]]
    List2 = List1[Start[1]]
    if List2 == 1:
        print("Coordinate is a wall, please re-enter your coordinate")
        Start.clear()
        Startpoint_input()
        Startpoint_Coords()
Startpoint_Coords()

#Creating a 0 matrix
p = []
for i in range(len(maze)):
    p.append([])
    for j in range(len(maze[i])):
        p[-1].append(0)
        
p[Start[1]][Start[0]] = 1

def steps(k):
    for y in range(len(p)):
        for x in range(len(p[y])):
            if p[y][x] == k:
                if y>0 and maze[y-1][x] == 0 and p[y-1][x] == 0:
                    p[y-1][x] = k+1
                if x>0 and maze[y][x-1] == 0 and p[y][x-1] == 0:
                    p[y][x-1] = k+1
                if y<(len(p)-1) and maze[y+1][x] == 0 and p[y+1][x] == 0: 
                    p[y+1][x] = k+1
                if x<len(p[y])-1 and maze[y][x+1] == 0 and p[y][x+1] == 0:
                    p[y][x+1] = k+1

k=1
while p[end[1]][end[0]] == 0:
    steps(k)
    k += 1

path_taken = []
def path():
    y,x = end[1],end[0]
    k = p[y][x]

    while k > 1:
        if y > 0 and p[y-1][x] == k-1:
            x,y = x,y-1
            path_taken.append((x,y))
            k-=1
        elif x > 0 and p[y][x-1] == k-1:
            x,y = x-1,y
            path_taken.append((x,y))
            k-=1
        elif y<len(maze)-1 and p[y+1][x] == k-1:
            x,y = x,y+1
            path_taken.append((x,y))
            k-=1
        elif x < len(maze[y]) - 1 and p[y][x+1] == k-1:
            x,y = x+1,y
            path_taken.append((x,y))
            k -= 1
path()

#add path taken into maze[]
for a in range(len(path_taken)):
    maze[path_taken[a][1]][path_taken[a][0]]=2
    
#visualising maze
plt.pcolormesh(maze)
plt.axes().set_aspect('equal') #set the x and y axes to the same scale
plt.xticks([]) # remove the tick marks by setting to an empty list
plt.yticks([]) # remove the tick marks by setting to an empty list

#plotting points
endpoint = plt.plot(end[0]+0.5,end[1]+0.5,'ro')
startpoint = plt.plot(Start[0]+0.5,Start[1]+0.5,'go')

plt.show()
