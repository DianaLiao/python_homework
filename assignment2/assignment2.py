import csv
import traceback

# Task 2
def read_employees():
  dict = {}
  rows = []

  try:
    with open("../csv/employees.csv", "r") as file:
      reader = csv.reader(file)

      for row_no, row_data in enumerate(reader):
        if row_no == 0:
          fields = row_data
        else:
          rows.append(row_data)

      dict["fields"] = fields
      dict["rows"] = rows

      return dict
  except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
      print(f"Exception message: {message}")
      print(f"Stack trace: {stack_trace}")

employees = read_employees()
# print(employees)

# Task 3
def column_index(str):
  return employees["fields"].index(str)

employee_id_column = column_index("employee_id")

# Task 4
def first_name(row_no):
  i = column_index("first_name")
  return employees["rows"][row_no][i]

# Task 5
def employee_find(employee_id):
  def employee_match(row):
    return int(row[employee_id_column]) == employee_id

  matches = list(filter(employee_match, employees["rows"]))

  return matches

# Task 6
def employee_find_2(employee_id):
  matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
  return matches

# Task 7
def sort_by_last_name():
  i = column_index("last_name")
  employees["rows"].sort(key=lambda row: row[i])

  return employees["rows"]

# sort_by_last_name()
# print(employees)

# Task 8
def employee_dict(row):
  emp_dict = {}

  for i in range(len(row)):
    emp_dict[employees["fields"][i]] = row[i]

  modified_emp_dict = dict(filter(lambda field: field[0] not in ["employee_id"], emp_dict.items()))

  return modified_emp_dict

# print(employee_dict(['Miranda', 'Harris', '+370 001-563-522-4308x77248']))

# Task 9
def all_employees_dict():
  all_emp_dict = {}
  for row in employees["rows"]:
    all_emp_dict[row[0]] = employee_dict(row)

  return all_emp_dict

import os
import custom_module

# Task 10
def get_this_value():
  return os.getenv("THISVALUE")

# Task 11
def set_that_secret(new_secret):
  custom_module.set_secret(new_secret)

set_that_secret("sqkrbkr")
# print(custom_module.secret)

# Task 12
def read_minutes_csv(filepath):
  dict = {}
  rows = []

  try:
    with open(filepath, "r") as file:
      reader = csv.reader(file)

      for row_no, row_data in enumerate(reader):
        if row_no == 0:
          fields = row_data
        else:
          rows.append(tuple(row_data))

      dict["fields"] = fields
      dict["rows"] = rows
  except Exception as e:
    print(f"An exception occured:{e}")

  return dict

def read_minutes():
  minutes1 = read_minutes_csv("../csv/minutes1.csv")
  minutes2 = read_minutes_csv("../csv/minutes2.csv")

  return minutes1, minutes2

minutes1, minutes2 = read_minutes()
# print(minutes1, minutes2)

# Task 13
def create_minutes_set():
  min1set = set(minutes1["rows"])
  min2set = set(minutes2["rows"])

  return min1set.union(min2set)

minutes_set = create_minutes_set()
# print(minutes_set)

# Task 14
from datetime import datetime

def create_minutes_list():

  def convert_date(tuple):
    return (tuple[0], datetime.strptime(tuple[1], "%B %d, %Y"))

  list_with_datetime = list(map(convert_date, minutes_set))

  return list_with_datetime

minutes_list = create_minutes_list()
# print(minutes_list)

# Task 15
def write_sorted_list():
  sorted_list = sorted(minutes_list, key=lambda e: e[1])

  sorted_string_list = list(map(lambda e: (e[0], datetime.strftime(e[1],"%B %d, %Y")), sorted_list))

  try:
    with open('./minutes.csv', 'w') as file:
      writer = csv.writer(file)
      writer.writerow(minutes1["fields"])

      for entry in sorted_string_list:
        writer.writerow(entry)
  except Exception as e:
      print(f"An exception occured:{e}")

  return sorted_string_list

print(write_sorted_list())
