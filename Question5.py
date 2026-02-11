#we need to import the pandas package again:
import pandas as pd

#first we must load the dataset:
data_frame = pd.read_csv("student.csv")

#now we have to create the column indicated (grade_band):
data_frame["grade_band"] = pd.cut(
    data_frame["grade"],
    bins = [-float("inf"), 9, 14, float("inf")],
    labels = ["Low", "Medium", "High"]
)

#creating the grouped summary table:
summary_table = data_frame.groupby("grade_band").agg(
    number_of_students = ("grade", "count"),
    average_of_absences = ("absences", "mean"),
    internet_percentage = ("internet", "mean")
)
#now we have to convert the internet proportion into percentage:
summary_table["internet_percentage"] = summary_table["internet_percentage"] * 100

#saving the summary table from above to a CSV file called students_bands:
summary_table.to_csv("student_bands.csv")