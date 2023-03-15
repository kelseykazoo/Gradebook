studentName = input("Enter the student's name:")
numOfAssign = input("Enter number of assigment grades:")
numOfAssign = int(numOfAssign)
counter = 0
grade_tally = 0
while counter < numOfAssign:
  grade = input("Please enter an assignment grade:")
  grade = int(grade)
  grade_tally += grade
  counter = counter + 1 
average = grade_tally / numOfAssign
print(f"Student {studentName} received a final grade of {average}") 