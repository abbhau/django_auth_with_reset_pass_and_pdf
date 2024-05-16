

def sorted_list(n):
    li = []
    for i in range(n):
        ele = int(input("enter element"))
        li.append(ele)
    
    for ind in range(len(li)):
        for j in range(ind, len(li)):
            if li[ind] > li[j]:
                li[ind],li[j] = li[j] ,li[ind]
    return li
#n1 = int(input("no of element"))
# print(sorted_list(n1))

def find_index(n):
    n1 = int(input("no of element"))
    li = []
    for i in range(n1):
        ele = int(input("enter element"))
        li.append(ele)
    try:
        ind = li.index(n)
        return ind
    except:
        return "number not found in list"

#print(find_index(99))  

def find_occurance():
    n1 = [5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 2, 2, 2, 2, 7, 7, 78, 8]
    li = []
    for i in n1:
        # ele = int(input("enter element"))
        li.append(i)
    di = {}
    for i in set(li):
        di[i] = li.count(i)
    print(di)
    di1 = dict(sorted(di.items(), key=lambda n: n[1]))
    res = []
    for i in di1.items():
        for j in range(i[1]):
            res.append(i[0])
    res.reverse()
    return res
    

#print(find_occurance())    

# importing the csv module
import csv

# my data rows as dictionary objects
mydict = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
		{'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
		{'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
		{'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
		{'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
		{'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]

# field names
fields = ['name', 'branch', 'year', 'cgpa']

# name of csv file
filename = "user_pro/media/csv/university_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv dict writer object
	writer = csv.DictWriter(csvfile, fieldnames=fields)

	# writing headers (field names)
	writer.writeheader()

	# writing data rows
	writer.writerows(mydict)

with open(filename, 'r') as csvfile:
    writer = csv.DictReader(csvfile)
    print(list(writer))


