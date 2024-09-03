import random
def generate_random(size):
    arr = []
    for i in range(size):
        n = random.randint(1,100000)
        arr.append(n)
    
    random.shuffle(arr)
    return arr

list10 = generate_random(10)
list100 = generate_random(100)
list1000 = generate_random(1000)
list10000 = generate_random(10000)