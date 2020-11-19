# Gets the average from a list of numbers
def average(lst): 
    return sum(lst) / len(lst)

# Gets the grade according to student's obtained percentage 
def grade(scores):
    if scores >= 70 and scores <= 100:
        return 'Excellent to outstanding'
    elif scores >= 60 and scores <= 69:
        return 'Good to very good'
    elif scores >= 50 and scores <= 59:
        return 'Satisfying'
    elif scores >= 40 and scores <= 49:
        return 'Sufficient'
    else:
        return 'Unsatisfactory'

# Get the index of a particular item in a 2D array
def get_num_in_matrix(matrix, needle):
    matrix_dim = len(matrix[0])
    item_index = 0
    for row in matrix:
        for i in row:
            if i == needle:
                break
            item_index += 1
        if i == needle:
            break
    return int(item_index / matrix_dim)

# Get minimum based on a particular key
def minee(arr, key):
    minIndex = 0
    mini = arr[minIndex].split(" ")[key]
    data = arr[minIndex]
    for i in range(1, len(arr)):
        j = arr[i].split(" ")[key]
        if j < mini:
            mini = j
            data = arr[i]
            minIndex = i
    return minIndex, data

# Get sorted array based on first/last names
def sort_names(arr, key):
    farr = []
    for i in range(len(arr)):
        _, gotmin = minee(arr[i:len(arr)], key)
        temp = arr[i]
        arr[i] = arr[_]
        arr[_] = temp
        farr.append(gotmin)
    return farr

# Get min, max values from an array
def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

module_name = input("Enter the name of the module: ")
module_code = input("Enter the module code: ")
num_assignment = 0
try:
    num_assignment = int(input("Enter the number of assignments: "))
except:
    print("Entered incorrect input, please try again")
    try:
        num_assignment = int(input("Enter the number of assignments: "))
    except:
        print("Entered incorrect input, come back again!")

assignment_weights = []

for i in range(num_assignment):
    w = 0
    try:
        w = int(input(f"Enter the weight of assignment number {i+1}\n"))
        assignment_weights.append(w)
    except:
        print("Entered incorrect input, please try again")
        try:
            w = int(input(f"Enter the weight of assignment number {i+1}\n"))
            assignment_weights.append(w)
        except:
            print("Entered incorrect input, come back again!")

num_students = int(input("Enter the number of students: "))
first_names = []
last_names = []
ids = []
scores = []

for i in range(num_students):
    print(f"===[Details of student {i+1}]===")
    first_names.append(input(f"Enter the first name of student number {i+1}: "))
    last_names.append(input(f"Enter the last name of student number {i+1}: "))
    ids.append(input("Enter the student's id: "))
    indv_scores = []
    for j in range(num_assignment):
        indv_scores.append(int(input(f"Enter assignment score for assignment {j+1} of student {i+1} [0-100]: ")))
    scores.append(indv_scores)

print("===[Thanks for the inputs below you can find some insights on the provided data]===")

module_average = 0
av_list = []
min_assignment = 0
max_assignment = 0
max_module = 0
min_module = 0

for i in range(num_assignment):
    list_assignment = []
    for j in range(len(scores)):
        list_assignment.append(scores[i][j])
    av = average(list_assignment)
    print(f"Calculated average for assignment {i+1} is {av}")
    av_list.append(av)
    max_assignment, min_assignment = max_min(list_assignment) 

dup = []
for k in scores:
    for i in k:
        dup.append(i)
max_module, min_module = max_min(dup)

module_average = average(av_list)
out_data = []
obtained_scores = []

print(f"Calculated average for module over all assignments is {module_average}")

for i in range(num_students):
    total = 100 * num_assignment
    got = sum(scores[i])
    score_obt = (got/total*100)
    dat = f"{first_names[i]} {last_names[i]} got {score_obt} % out of 100% with a grade: {grade(score_obt)} and ID: {ids[i]}"
    out_data.append(dat)
    obtained_scores.append(score_obt)

print("===[Alphabetically sorted based on First Names]===")
list_grades_first_name = sort_names(out_data, 0)
[print(i) for i in list_grades_first_name]
print("===[Alphabetically sorted based on Last Names]===")
list_grades_last_name = sort_names(out_data, 1)
[print(i) for i in list_grades_last_name]
print("===[Based on Best Scores]===")
list_best_scores = sort_names(out_data, 3)
[print(i) for i in list_best_scores]

print("Do you want the details of the student who got minimum and maximum in the assignments? Y/n")
answer = input()
if(answer == 'Y' or answer == 'y'):
    print("Minimums: ")
    for i in range(len(scores)):
        if min_assignment in scores[i]:
            print(out_data[i])       
    print("Maximums: ")
    for i in range(len(scores)):
        if max_assignment in scores[i]:
            print(out_data[i])
