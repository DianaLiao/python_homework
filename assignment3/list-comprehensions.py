import csv

try:
  with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    list_of_lists = []

    for row in reader:
      list_of_lists.append(row)

except Exception as e:
  print(f"An error occurred: {e}")

employee_names = [row[1]+" " + row[2] for row in list_of_lists[1:]]

print(employee_names)

employee_names_with_e = [name for name in employee_names if "e" in name.lower()]

print(employee_names_with_e)
