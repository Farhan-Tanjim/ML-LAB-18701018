import math
  
def classifyAPoint(points,p,k,choice):
  
    distance=[]
    for group in points:
        for feature in points[group]:
            if(choice == 1):
                dist = math.sqrt((feature[0]-p[0])**2 +(feature[1]-p[1])**2)
            else:
                dist = abs(feature[0] - p[0]) + abs(feature[1] - p[1])

            distance.append((dist, group))
            #distance.append((euclidean_distance,group))
  
    distance = sorted(distance)[:k]
  
    freq1 = 0 
    freq2 = 0 
  
    for d in distance:
        if d[1] == 0:
            freq1 += 1
        elif d[1] == 1:
            freq2 += 1
  
    return 0 if freq1>freq2 else 1
  
def main():
    
    points = {0:[(158,58),(158,59),(158,63),(160,59),(160,60),(163,60),(163,61)],
              1:[(160,64),(163,64),(165,61),(165,62),(165,65),(168,62),(168,63),(168,66),(170,63),(170,64),(170,68)]}
  
    t = 3

    while(t!=0):
        print("\n")
        k = int(input("Enter value of k: "))
        h = int(input("Enter height: "))
        w = int(input("Enter weight: "))

        choice = int(input('''
        which function do you want to get the solution form?
        Enter 1 -> Euclidien formula
        Enter 2 -> manhatten formula
        
        '''
        ))

        p = (h,w)

        r = classifyAPoint(points,p,k,choice)

        if r == 0 :

            print("Mr.Perfect T-Shirt size is M")
        elif r == 1 :
            print("Mr.Perfect T-Shirt size is L")
        
        t = t - 1
main()