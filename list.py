# LIST IS COMPLEX DATA TYPE , DIFF TYPES OF DATATYPE IS STORED IN IT
# INDEX LEFT->RIGHT (0 ,1,..........) RIGHT->LEFT(-1,-2......)
marks = [95,98,92,81]
print(marks[-1]) # ONLY PRINT -1 INDEX
print(marks[0:2]);   # it only print upto index 2 (0,1)will be print not index 2
for score in marks:   # PRINTING LIST USING LOOPS
    print(score)
marks.append(99)  # TO INSERT ANYTHING AT THE END OF LIST
print(marks)
marks.insert(0,85) # TO INSERT ANYWHERE IN LIST FIRST WE GIVE INDEX THEN MARKS
print(marks)