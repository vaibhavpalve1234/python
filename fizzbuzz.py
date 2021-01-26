def fizzbuzz(n):
    c3 = 0
    c5 = 0
    for i in range(1,n):
        c3+=1
        c5+=1
        d = ""
        if(c3 == 3):
            d+="fizz"
            c3 = 0
            print(d)
        if(c5 == 5):
            d += "buzz"
            c5 = 0
            print(d)
        if (d == ""):
            print(i)

if __name__ == "__main__":
    fizzbuzz(50)