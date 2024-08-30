import random
def generate_random(size):
    n = random.randint(1,1000)
    arr = []
    for i in range(size):
        arr.append(n)
        n += random.randint(1,1000)
    
    random.shuffle(arr)
    return arr

list100 = generate_random(100)
list1000 = generate_random(1000)
list5000 = generate_random(5000)