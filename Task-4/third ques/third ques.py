#Q3.Write a python program to make a 2-dimensional list that contains 
#represents a table of records, for instance, student details like Roll no, 
#Student Name, Marks; And complete the following 2 sub-tasks.
# i) Add some records in the list and print the list in tabular form,
# ii) From created list, extract and print second record/row that contains,
import pandas as pd
win = []
vif = int(input("Enter number of students: "))

for p in range(0, vif):
    print("Enter the student details in Roll number, Student Name, Marks : \n")
    win.append([])
    for o in range(0, 4):
        if o==3:
           Enter_details = ''
        else:
           Enter_details = input()
        win[p].append(Enter_details)
df = pd.DataFrame(win, columns=["Roll number  ",   "Student Name  ",   "Marks  ", ""])
df = df.set_index(['Roll number  ',   'Student Name  ',   'Marks  '])
print()
print('i)')
print(df)
print()
print('ii)')
print(df[1:2])
