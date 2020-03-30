#一个3x3的格子，有1到9，9个数字，填进去，不重复，使得，行，列，2条对角线上，两边的数字加起来减去中间的，都等于5.



import numpy as np

if(0):
    maze = np.matrix([[1,2,3],[11,22,33],[111,222,333]])
                                                                    
    temp = maze[0]+maze[2]-maze[1]
    print(temp)

    for item in temp:
        print(item)
        print(item[0,0])
    exit(0)


def check(maze):
    for hang in maze:
        if (hang[0,0]+hang[0,2]-hang[0,1]) !=5:
            return False
    temp = maze[0]+maze[2]-maze[1]
    for item in temp:
        if 5!=item[0,0] or 5!=item[0,1] or 5!=item[0,2]:
            return False
    if maze[0,0]+maze[2,2]-maze[1,1]!=5:
        return False
    if maze[2,0]+maze[0,2]-maze[1,1]!=5:
        return False
    return True

###########################################

for a in range (1,9):
    print(a)

for ul in range(1,7):
    for u in range(1,10):
        if ul!=u:
            print("now searching : "+str(ul)+" - "+str(u))
            for ur in range(ul,8):
                if ur!=ul and ur!=u:
                    for l in range(1,10):
                        if l!=ul and l!=u and l!=ur:                            
                            for mid in range(1,10):
                                if mid!=ul and mid!=u and mid!=ur and mid!=l:
                                    for r in range(1,10):
                                        if r!=ul and r!=u and r!=ur and r!=l and r!=mid:
                                            for dl in range(ur,10):
                                                if dl!=ul and dl!=u and dl!=ur and dl!=l and dl!=mid and dl!=r:
                                                    for d in range(1,10):
                                                        if d!=ul and d!=u and d!=ur and d!=l and d!=mid and d!=r and d!=dl:
                                                            for dr in range(ur,10):
                                                                if dr!=ul and dr!=u and dr!= ur and dr!= l and dr!= mid and dr!= r and dr!= dl and dr!= d:
                                                                    theMaze = np.matrix([[ul,u,ur],[l,mid,r],[dl,d,dr]])
                                                                    result = check(theMaze)
                                                                    if result :
                                                                        print(theMaze)
















if(0):
    mat = np.matrix('1 2 3;4 5 6;7 8 9')
    print(mat)
    temp = mat[0]+mat[2]#-mat[1]
    print(temp)














