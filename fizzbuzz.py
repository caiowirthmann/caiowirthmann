import time


lut = {
    3 : "fizz",
    5 : "buzz"
}

def fizzbuzz(start, end):
    start_time = time.time()
    
    for i in range(start, end):
        result = []
        for nums in lut:
            if i % nums == 0:
                result.append(lut[nums])
        if result != []:
            print ("".join(result))
        else:
            print (i)
    
    end_time = time.time()
    print (f'Tempo de execução = {end_time - start_time}')
    

fizzbuzz(1, 10000)
