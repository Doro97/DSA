def compareTriplets(a,b):
    # Write your code here
    # pseudocode
    # @parameters a[3],b[3]
    # Return: a list with comparison points 
    # where the first element is alice's score and the second is bob's    
    # Tests:
    # a=[1,2,3]
    # b=[4,5,3]
    # intialize a list for comparison points
    # compare elements on given indexes for each list
    # if a[i] > b[i]=Alice gets 1 point
    # if a[i] < b[i]=Bob gets 1 point
    # if a[i] = b[i]=neither gets a point
    # indexes of each element =a.index(i)


    valueList=[value for value in zip(a,b)]
    
    # for i in valueList:
    # print (valueList[0])
    j=0
    while j <= 2:
        score=[]
        a_res = []
        b_res=[]

        if (valueList[j][0] > valueList[j][1]) :
            score.append(1)
            # print(a_res)
        elif(valueList[j][0] < valueList[j][1]) :
            score.append(1)
        else:
            score.append(0)
        print(score)
        j += 1
            


# compareTriplets([5,6,7],[3,6,10])
# compareTriplets([1,2,3],[3,2,1])
compareTriplets([17, 28, 30],[99 ,16 ,8])