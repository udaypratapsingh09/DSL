n = int(input("Number of students "))
scores = []

for i in range(n):
    marks = int(input("Enter student marks"))
    scores.append(marks)

def find_highest(scores):
    highest = scores[0]
    for i in scores:
        if i>highest:
            highest = i

    return highest

def find_lowest(scores):
    lowest = scores[0]
    for i in scores:
        if i<lowest:
            lowest = i

    return lowest

def find_average(scores):
    total = 0
    for i in scores:
        total+=i
    
    return total/len(scores)

def find_pass_fail_absent(scores):
    students = {"pass":0,"fail":0,"absent":0}
    for i in scores:
        if i == 0:
            students["absent"]+=1
        elif i <40:
            students["fail"]+=1
        else:
            students["pass"]+=1

    return students

def find_mode(scores):
    frequency = {}
    mode = scores[0]
    highest_frequency=0
    for i in scores:
        if i not in frequency:
            frequency[i]=0
        frequency[i]+=1
        if frequency[i]>highest_frequency:
            highest_frequency = frequency[i]
            mode = i
    
    print(frequency)
    return i

# Average of the class
print("Average: ",find_average(scores))

# Highest and lowest
print("Highest: ",find_highest(scores))
print("Lowest: ",find_lowest(scores))

# Absent
result = find_pass_fail_absent(scores)
print("Absent: ",result["absent"])
# Pass % and Fail %
print("Pass %: ",round(result["pass"]/n*100,2),"%")
print("Fail %: ",round(result["fail"]/n*100,2),"%")
# Marks with highest frequency
print("Marks with highest frequency: ",find_mode(scores))