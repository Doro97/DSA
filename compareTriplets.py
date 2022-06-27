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
    # a=[]
    # b[3]=[]
    # for index,value in enumerate(a):
    #     a_element=a[index]
    
    # for i, val in enumerate(b):
    #     b_element= b[i]
    
    # while (a_element > b_element):
    #     print (comparison_scores)

    for (a_element,b_element) in zip (a,b):
        comparison_scores=[]
        comparison_scores.append(1)
           
        if (a_element > b_element):
            score=[]            
            for i in comparison_scores:                 
                score.append(i)
                print(score)
                # print(comparison_scores)
        elif (a_element < b_element):
            b_score=[]
            for j in comparison_scores:
                b_score.append(j)
                # print(score)
        else:
            pass



        
    # if (a_element > b_element):
    #     print(a_element)
    #     # print (score.append(comparison_scores))
    # elif (a_element < b_element):
    #     print(b_element)
    #     # print (score.append(comparison_scores))
    # else:
    #     return 0
            # a_ele=a[index]
            # b_ele=b[i]
            # print (a_ele,b_ele)
            # print (a[index],b[i])

# compareTriplets([5,6,7],[3,6,10])
# compareTriplets([1,2,3],[3,2,1])
compareTriplets([17, 28, 30],[99 ,16 ,8])