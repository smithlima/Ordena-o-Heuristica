import sys
import timeit


def heap(list1):
        n = len(list1)
        i = len(list1)//2
        while True:
                if i>0:
                        i-=1
                        t = list1[i]
                else:
                        n-=1
                        if n == 0:
                                return
                        t = list1[n]
                        list1[n] = list1[0]
                parent = i
                child = i*2 +1;
                while child < n:
                        if child +1 < n and list1[child + 1] > list1[child]:
                                child += 1
                        if(list1[child] > t):
                                list1[parent] = list1[child]
                                parent = child
                                child = parent*2 + 1
                        else:
                                break
                list1[parent] = t
#######################################################################

def countSort(list):

        def key(index, min_v):
                if (min_v >= 0):
                        return index
                else:
                        return index - min_v

        min_v = min(list)
        max_v = max(list)

        if min_v > 0:
                count_list = [0]*(max_v+1)
        else:
                count_list = [0]*(max_v - min_v + 1)

        for x in list:
                count_list[key(x, min_v)] += 1

        for each in range(1, len(count_list)):
                count_list[each] += count_list[each-1]

        output = [0]*(len(list))
        for each in list:
                k = key(each, min_v)
                count_list[k] -= 1
                output[count_list[k]] = each

        return output
        
########################################################################
def map(x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
#########################################################################
def bucketSort(list):
        n = len(list)
        max_v = max(list)
        min_v = min(list)
        bucket_range = 1000
        bucket = [[]]* n

        for x in range(n):
                
                index = int(map(list[x], min_v, max_v, 0, n-1))
                bucket[index] = bucket[index] + [list[x]]

        for x in range(n):
                bucket[x].sort()
        list = []
        for i in range(n):
                for j in bucket[i]:
                        list.append(j)
        return list
    
########################################################################

########################################################################
def main(argv):
        
        size = int(input())
        list1 =[]
        for i in range(size):
                list1.append(int(input()))
        minimo = min(list1)
        maximo = max(list1)
        aux = [] 
        aux2 =[]
        aux3 =[]        
        
        for i, aux1 in enumerate(list1):
                if(aux1 < 0):
                        aux.append(aux1)
                elif (aux1 <= 9999):
                        aux2.append(aux1)
                else:
                        aux3.append(aux1)
        
        timeIn = timeit.default_timer()
        AUX  = []
        AUX2 = []
        AUX3 = []
        if(len(aux)!=0):
                AUX=countSort(aux)
        if(len(aux2)!=0):
                if((max(aux2)-min(aux2))< len(aux2)):
                        AUX2=bucketSort(aux2)
        else:
                AUX2=heap(aux2)
        if(len(aux3)!=0):
                if((max(aux3)-min(aux3))< len(aux3)):
                        AUX3=bucketSort(aux3)
                else:
                        heap(aux3)
                        AUX3 = aux3
        junto=[]
        junto = AUX+AUX2+AUX3
        timeOut = timeit.default_timer()
        for i in junto:
                print(i)
        
if __name__ == "__main__":

        main(sys.argv)

