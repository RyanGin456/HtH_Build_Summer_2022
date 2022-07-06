import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

student_data = pandas.read_csv("Finding-an-interetsing-dataset/student_data.csv")

print(student_data)