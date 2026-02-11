#in order to convert it into a dataset/frame we need the pandas package
import pandas as pd

#and now we have to load the data set
data_frame = pd.read_csv("student.csv")

#now we have to filter the students based:
filtered_DataFrame = data_frame[
    (data_frame["studytime"] >= 3) &
    (data_frame["internet"] == 1) &
    (data_frame["absences"] <= 5)
]

#now we save the filtered data to a new csv file:
filtered_DataFrame.to_csv("high_engagement.csv", index=False)

#now we are going to print the number of students that were saved to the csv:
number_of_students = len(filtered_DataFrame)
print(f"Students that are highly engaged:", number_of_students)

#now we print the average grade:
average_grade = filtered_DataFrame["grade"].mean()
print(f"Average high engagement of students:",average_grade)