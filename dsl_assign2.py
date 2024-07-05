def intersection(list1,list2):
    intersect_list = []
    for i in list2:
        if i in list1:
            intersect_list.append(i)
    
    return intersect_list

def union(list1,list2):
    union_list = list1.copy()
    for i in list2:
        if i not in list1:
            union_list.append(i)

    return union_list

def difference(list1,list2):
    difference_list = []
    for i in list1:
        if i not in list2:
            difference_list.append(i)

    return difference_list

n = int(input("No of students "))

students = [i for i in range(1,n+1)]

cricket = eval(input("Students who play cricket "))
badminton = eval(input("Students who play badminton "))
football = eval(input("Students who play football "))

print("\nANSWERS\n")

# 1. list of students who play cricket and badminton
ans1 = intersection(cricket,badminton)
print("students who play cricket and badminton")
print(ans1)

# 2. list of students who play either cricket or badminton but not both
ans2 = difference(union(cricket,badminton),intersection(cricket,badminton))
print("students who play either cricket or badminton but not both")
print(ans2)

# 3. No of students who play neither cricket nor badminton
ans3 = difference(difference(students,cricket),badminton)
print("No of students who play neither cricket nor badminton")
print(len(ans3))

# 4. No of students who play cricket and football but not badminton
ans4 = difference(intersection(cricket,football),badminton)
print("No of students who play cricket and football but not badminton")
print(len(ans4))

# 5. No of students who do not play any game
ans5 = difference(difference(difference(students,cricket),badminton),football)
print("No of students who do not play any game")
print(len(ans5))

# 6. List of students who play at least one game
ans6 = union(union(cricket,badminton),football)
print("students who play at least one game")
print(ans6)

# 7. List of students who play all the games
ans7 = intersection(intersection(cricket,badminton),football)
print("students who play all the games")
print(ans7)