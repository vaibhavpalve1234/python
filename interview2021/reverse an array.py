"""
i/n =  1 2 3  4 5 6
o/p= 6 5 4 3 2 1


"""

#   timecomplexity = o(n)


def reverSeanArray(a ,l ,r):
    while l < r:     
        a[l],a[r] = a[r] ,a[l]
        l+=1
        r-=1
    return a
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(reverSeanArray(array, 0, len(array)-1 ))



#timecomplixity o(n)

def reverse(a, one, last):
    if one >= last:
        return 
    a[one],a[last]=a[last],a[one]
    reverse(a, one+1, last-1)
    
if __name__ == "__main__":
    array = [1,2,3,4]
    reverse(array,0,len(array)-1)
    print(array)


#timecomplixity o(n)
def revers(array):
    return array[::-1]
if __name__ == "__main__":
    a=[1,2,3,4,5]
    print(revers(a))
    print(a)
