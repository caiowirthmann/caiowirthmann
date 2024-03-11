lut = {
    3 : "fizz",
    5 : "buzz"
}

def fizzbuzz(start, end):
    for i in range(start, end):
        result = []
        for nums in lut:
            if i % nums == 0:
                result.append(lut[nums])
        if result != []:
            print ("".join(result))
        else:
            print (i)
    

fizzbuzz(1, 10000)