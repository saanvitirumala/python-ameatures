student_list = ["Komali", "Navin & Navya","Udeepth",  "Akshar","Adityamithran", "Adityamithram"]
# Index starts from 0

long_name_list = [student_list[0]]  #intialize

for student_name in student_list :    # visit all names
  if len(student_name) == len(long_name_list[0]) and  student_name !=  long_name_list[0] :
    long_name_list.append(student_name)   # Add to existing long names list 
  elif len(student_name) > len(long_name_list[0]) :
    long_name_list.clear()   # clear/forget  all  long names 
    long_name_list.append(student_name)  # This is the new long name add it

for student_name in long_name_list :
  print(student_name)


short_name_list = [student_list[0]]  #intialize

for student_name in student_list :    # visit all names
  if len(student_name) == len(short_name_list[0]) and  student_name !=  short_name_list[0] :
    short_name_list.append(student_name)   # Add to existing long names list 
  elif len(student_name) < len(short_name_list[0]) :
    short_name_list.clear()   # clear/forget  all  long names 
    short_name_list.append(student_name)  # This is the new long name add it

print("---Lengthiest--")
for student_name in long_name_list :
  print(student_name)

print("--Shortest--")

for student_name in short_name_list :
  print(student_name)



  student_list = ["Komali", "Navin & Navya","Udeepth",  "Akshar","Adityamithran"]
# Index starts from 0

print("---- Before sorting--")

for student_name in student_list :
      print(student_name)

#Sort in descending
sorted_student_list = sorted(student_list, key=len, reverse=True)

for student_name in sorted_student_list :
  if len(student_name) !=len(sorted_student_list[0]) : # Break if student name length is difrent break loop
        break
  print(student_name)