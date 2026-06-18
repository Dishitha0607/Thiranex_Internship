import pandas as pd
import random

data = []

for i in range(100):

  study_hours = random.randint(1,100)
  attendance = random.randint(40,100)
  prev_marks = random.randint(30,100)
  assignments = random.randint(1,10)

  if (
    study_hours >= 4 and
    attendance >= 60 and 
    prev_marks >= 50
  ):
    result = "Pass"
  else:
    result = "Fail"

  data.append([study_hours,attendance,prev_marks,assignments,result])

df = pd.DataFrame(data, columns=[
  "StudyHours","Attendance", "PreviousMarks","Assignments","Result"
])

df.to_csv("student_data.csv",index=False)
print("Dataset created successfully!")
print(df.head())