''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv


# create a file object to open the file in read mode
with open ('students.csv','r') as students:
    reader = csv.reader(students)            


# create a csv object from the file object
    with open('processedStudents.csv','a') as processedStudents:
        append_file = csv.append(processedStudents)    

#skip the header row
header = next(reader)





#create an outfile object for the pocessed record
with open ('processedStudents.csv','w') as openprocessed:
   write_file = csv.write_file(openprocessed)





#create a new dictionary named 'student_dict'
student_dict = {}





#use a loop to iterate through each row of the file
    #check if the GPA is below 3.0. If so, write the record to the outfile
for row in openprocessed:
    gpa = float(row[8])
    if gpa < 3.0:
        writer.writerow(row)
        
    

    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA
    
for row in openprocessed:
    student_id = row[0]
    gpa = float(row[8])
    student_dict[student_id] = gpa
    print(student_dict)
    





#print the entire dictionary
for row in openprocessed:
    student_id = row[0]
    gpa = float(row[8])
    student_dict[student_id] = gpa
    print(student_dict)
    
#Print the student id 
for student_id in student_dict:
    print(student_id)

#print out the corresponding GPA from the dictionary

for student_id,gpa in student_dict.items():
    print(gpa)

#close the outfile
write_file.close






