#4x4的格子，有-8到-1，1到8，总共16个数字，填入幻方，使行，列，对角线，相加都等于0

import numpy as np


def check(maze):
    for hang in maze:
        if 0!=np.sum(hang):
            return False

    temp = maze[0]+maze[1]+maze[2]+maze[3]
    for i in range(4):
        if 0!=temp[0,i]:
            return False
    if maze[0,0]+maze[1,1]+maze[2,2]+maze[3,3]!=0:
        return False
    if maze[0,3]+maze[1,2]+maze[2,1]+maze[3,0]!=0:
        return False
    return True

###########################################

#全部都是0，应该是可以通过验证的。
if(0):
    ttt=np.zeros((4,4),dtype=np.int32)
    print(check(ttt))
    exit(0)

#手动构造一个根据标准4阶幻方改的版本，也是通过了的。
if(0):
    ttt=np.matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    ttt2=np.zeros((4,4),dtype=np.int32)
    for i in range(4):
        for ii in range(4):
            ttt2[i,ii] = ttt[3-i,3-ii]
    #print(ttt)
    #print(ttt2)
    flag = np.matrix([[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]],dtype=np.bool)
    for i in range(4):
        for ii in range(4):
            if flag[i,ii]:
                ttt[i,ii]=ttt2[i,ii]
    #这个地方就是标准的1到16的4阶幻方

    for i in range(4):
        for ii in range(4):
            if ttt[i,ii]<=8:
                ttt[i,ii]=ttt[i,ii]-1
    ttt=ttt-8
    #这儿得到的是我手动构造的版本。是ok的。
    print(ttt)
    print(check(ttt))

    exit(0)

###########################################

#但是考虑到一些性能方面的问题，最终决定还是换个写法。

#把一个1d的数组当成4x4的来显示。没做正确性检验。
def show(arr):
    for i in range(4):
        print(arr[i*4:i*4+4])




def smallCheck(arr):
    for i in range(4):
        if np.sum(arr[i::4])!=0:
            return False

    if np.sum(arr[0::5])!=0:
        return False
    if np.sum(arr[3:13:3])!=0:
        return False

    return True


if(0):
    theNumber = 4
    def smallCheck2(arr):
        for i in range(4):
            if np.sum(arr[i::4])!=theNumber:
                return False

        if np.sum(arr[0::5])!=theNumber:
            return False
        if np.sum(arr[3:13:3])!=theNumber:
            return False

        return True


if(0):
    tt = np.array([x for x in range(16)])
    tt2 = np.array([15-x for x in range(16)])
    ttFlag = np.array([0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0])
    for i in range (len(ttFlag)):
        if ttFlag[i]:
            tt[i] = tt2[i]

    for i in range(16):
        if tt[i]<8:
            tt[i]=tt[i]-1
    tt=tt-7

    print(tt)

    print(smallCheck(tt))
    with open("output.txt",'a') as f:
        f.write(str(tt))


    #ttt = np.zeros((16),dtype = np.int32)

    exit(0)


#其中的一个版本。
if(0):
    arr=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],dtype=np.int32)

    fullRange = np.array([-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8])
    #gen the 1st row（行）
    for i00 in np.array([-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5]):
    
        for i01 in fullRange:
            if i01!=i00:
                for i02 in fullRange:
                    #print("Searching:  "+str(i00)+" , "+str(i01)+" , "+str(i02))
                    if i02!=i00 and i02!=i01:
                        i03=-(i00+i01+i02)
                        # upper right > upper left
                        if i03 > i00 and i03 != i01 and i03 != i02 and i03>=-8 and i03<=8 and i03!=0:

                            __range_12 = []
                            for aaa in fullRange:
                                if aaa!=i00 and aaa!=i01 and aaa!=i02 and aaa!=i03:
                                    __range_12.append(aaa)
                            range_12 = np.array(__range_12)
                            range_12.sort()

                            for i10 in range_12:
                                #print("Searching:  "+str(i00)+" , "+str(i01)+" , "+str(i02)+" , "+str(i03)+" , "+str(i10))
                                for i11 in range_12:
                                    if i11!=i10 :
                                        for i12 in range_12:
                                            if i12!=i10 and i12!=i11 :
                                                i13=-(i10+i11+i12)
                                                if i13 !=i10 and i13 !=i11 and i13 !=i12 and i13>=-8 and i13<=8 and i13!=0:
                                                    print("Searching:  "+str(i00)+" , "+str(i01)+" , "+str(i02)+" , "+str(i03)+" , "+str(i10)+" , "+str(i11)+" , "+str(i12)+" , "+str(i13))

                                                    __range_8 = []
                                                    for bbb in range_12:
                                                        if bbb!=i10 and bbb!=i10 and bbb!=i10 and bbb!=i10:
                                                            __range_8.append(bbb)
                                                    range_8 = np.array(__range_8)
                                                    range_8.sort()

                                                    for i20 in range_8:
                                                        for i21 in range_8:
                                                            if i21 != i20:
                                                                for i22 in range_8:
                                                                    if i22!=i20 and i22!=i21:
                                                                        i23 = -(i20+i21+i22)
                                                                        if i23 !=i20 and i23 !=i21 and i23 !=i22 and i23>=-8 and i23 <=8 and i23 !=0:
                                                                        
                                                                            __range_4 = []
                                                                            for ccc in range_8:
                                                                                if ccc !=i20 and ccc !=i21 and ccc !=i22 and ccc !=i23:
                                                                                    __range_4.append(ccc)
                                                                            range_4 = np.array(__range_4)

                                                                            # down left > upper right > upper left
                                                                            for i30 in range_4:
                                                                                if i30 >i03:
                                                                                    for i31 in range_4:
                                                                                        if i31 != i30:
                                                                                            for i32 in range_4:
                                                                                                if i32 != i30 and i32 != i31:
                                                                                                    #down right > upper left
                                                                                                    for i33 in range_4:
                                                                                                        if i33 != i30 and i33 != i31 and i33 != i32 and i33>i00:
                                                                                                            arr[0]=i00
                                                                                                            arr[1]=i01
                                                                                                            arr[2]=i02
                                                                                                            arr[3]=i03
                                                                                                            arr[4]=i10	
                                                                                                            arr[5]=i11
                                                                                                            arr[6] =i12
                                                                                                            arr[7]=i13
                                                                                                            arr[8] = i20
                                                                                                            arr[9]=i21
                                                                                                            arr[10]=i22
                                                                                                            arr[11]=i23
                                                                                                            arr[12] = i30
                                                                                                            arr[13] = i31
                                                                                                            arr[14] = i32
                                                                                                            arr[15]=i33
                                                                                                            result = smallCheck(arr)
                                                                                                            if result:
                                                                                                                show(arr)
                                                                                                                with open("output.txt",'a') as f:
                                                                                                                    f.write(str(arr))
                                                                                                                    f.write('\n')
                        




                        
#还是觉得性能不行。于是换一个思路
#实际测试结果是性能很好。但是结果是不是正确的就没有花时间去验证了
fullRange = np.array([-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8])


def stage_2(i00,i01,i02,i03):
    #简单标记一下这一步是干嘛。v表示已经有了。o表示这一步要做的事情。_表示不管
    #  v  v  v  v
    #  _  _  o  _
    #  _  o  _  _
    #  o  _  _  _
    rangeArr_12 = []
    for i in fullRange:
        if i !=i00 and i !=i01 and i!=i02 and i!=i03:
            rangeArr_12.append(i)
    rangeArr_12 = np.array(rangeArr_12)
    for i12 in rangeArr_12:
        for i21 in rangeArr_12:
            if i21!=i12:
                for i30 in rangeArr_12:
                    if -(i03+i12+i21)==i30 and i30!=i12 and i30 != i21 and i30<i03:# down left>upper right (> upper left)
                        print("Searching: (0,0~3) = "+str(i00)+" , "+str(i01)+" , "+str(i02)+" , "+str(i03)+" , (1~3,2~0) : "+str(i12)+" , "+str(i21)+" , "+str(i30))

                        #  v  v  v  v
                        #  _  _  v  _
                        #  _  v  _  _
                        #  v  o  o  o
                        rangeArr_9=[]
                        for i in rangeArr_12:
                            if i !=i12 and i != i21 and i!= i30:
                                rangeArr_9.append(i)
                        rangeArr_9 = np.array(rangeArr_9)
                        for i31 in rangeArr_9:
                            for i32 in rangeArr_9:
                                if i32 !=i31:
                                    for i33 in rangeArr_9:
                                        if -(i30+i31+i32)==i33 and i33 !=i31 and i33!=i32 and i33>i00:#down right>up left
                                            #  v  v  v  v
                                            #  _  o  v  _
                                            #  _  v  _  _
                                            #  v  v  v  v
                                            #这一步的最长的判断是后面一步的判断，但是可以提前，所以就拿上来了。
                                            for i11 in rangeArr_9:
                                                sum_i02_i12_i32= i02+i12+i32
                                                if -(i01+i21+i31)==i11 and (i00+i11+i33)== sum_i02_i12_i32 and i11!=i31 and i11 !=i32 and i11 !=i33 :
                                                    #  v  v  v  v
                                                    #  _  v  v  _
                                                    #  _  v  o  _
                                                    #  v  v  v  v
                                                    for i22 in rangeArr_9:
                                                        #这个地方就只用检查一条线的情况了。
                                                        if -(sum_i02_i12_i32)==i22 and i22 !=i31 and i22 !=i32 and i22 !=i33 and i22 !=i11:
                                                            #  v  v  v  v
                                                            #  o  v  v  _
                                                            #  o  v  v  _
                                                            #  v  v  v  v
                                                            rangeArr_4=[]
                                                            for i in rangeArr_9:
                                                                if i !=i12 and i != i21 and i!= i30:
                                                                    rangeArr_4.append(i)
                                                            rangeArr_4 = np.array(rangeArr_4)
                                                            for i10 in rangeArr_4:
                                                                for i20 in rangeArr_4:
                                                                    if -(i00+i10+i30)==i20 and i20!=i10:
                                                                        #  v  v  v  v
                                                                        #  v  v  v  o
                                                                        #  v  v  v  o
                                                                        #  v  v  v  v
                                                                        for i13 in rangeArr_4:
                                                                            sum_i20_i21_i22 = i20+i21+i22#类似前面有一个地方，提前检测
                                                                            if i13!=i10 and i13!=i20 and -(i10+i11+i12)==i13 and i03+i13+i33==sum_i20_i21_i22:
                                                                                for i23 in rangeArr_4:
                                                                                    if (-sum_i20_i21_i22)==i23 and i23 !=i10 and i23 !=i20 and i23 != i13 :
                                                                                        result = [[i00,i01,i02,i03],[i10,i11,i12,i13],[i20,i21,i22,i23],[i30,i31,i32,i33]]
                                                                                        print(result)
                                                                                        with open("output.txt",'a') as f:
                                                                                            f.write(str(result[0])+'\n'+str(result[1])+'\n'+str(result[2])+'\n'+str(result[3])+'\n\n')
                                                    











###############################

#stage_1
for i00 in np.array([-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5]):
    for i01 in fullRange:
        if i01!=i00:
            for i02 in fullRange:
                #print("Searching:  "+str(i00)+" , "+str(i01)+" , "+str(i02))
                if i02!=i00 and i02!=i01:
                    i03=-(i00+i01+i02)
                    # upper right > upper left
                    if i03 > i00 and i03 != i01 and i03 != i02 and i03>=-8 and i03<=8 and i03!=0:
                        stage_2(i00,i01,i02,i03)





exit(0)
