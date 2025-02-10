"""Exercise1"""
# def add_task(tasks, task_name, status='Pending'):
#     tasks[task_name] = {'status': status}
#
# def update_task_status(tasks, task_name, new_status):
#     if task_name in tasks:
#         tasks[task_name]['status'] = new_status
#     else: print("Task not found")
#     return tasks
#
# def get_pending_tasks(tasks):
#     pending_tasks = []
#     for task, details in tasks.items():
#         if details['status'] == 'Pending':
#             pending_tasks.append(task)
#     return pending_tasks
#
# tasks = {}
# add_task(tasks, "Task 1", "Pending")
# add_task(tasks, "Task 2", "Completed")
# add_task(tasks, "Task 3", "Pending")
#
# print(get_pending_tasks(tasks))
# print(update_task_status(tasks,"Task 4", "Completed"))
# print(get_pending_tasks(tasks))
# """
# output:
# ['Task 1', 'Task 3']
# Task not found
# {'Task 1':{'status':'pending'},'Task 2':{'status':'Completed'},'Task 3':{'status':'pending'}}
# ['Task 1', 'Task 3']
# """



"""Exercise2"""
# def calculate_average(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total / len(numbers)
#
# numbers = [1, 2, 3, 4, 5]
# print("Average:", calculate_average(numbers))
# numbers = [3,5,7]
# print("Average:", calculate_average(numbers))
# """
# output:
# Average: 3
# Average: 5
# """

"""Exercise3"""
# def calculate_median(numbers):
#     sorted_numbers = sorted(numbers)
#     n = len(sorted_numbers)
#     if n % 2 == 0:
#         median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
#     else:
#         median = sorted_numbers[n//2]
#     return median
# numbers = [1, 3, 5, 7, 9]
# print("Median:", calculate_median(numbers))
# numbers = [1, 2, 3, 4, 5, 6]
# print("Median:", calculate_median(numbers))
# """
# output:
# Median: 5
# Median: 3.5
# """

"""Exercise4"""
def add_employee(employees, name, salary):
    employees[name] = {'salary': salary}

def increase_salary(employees, name, amount):
    if name in employees:
        employees[name]['salary'] += amount
    else: print("Employee not found")
    return employees

employees = {}
add_employee(employees, "John", 50000)
add_employee(employees, "Jane", "60000")
print(increase_salary(employees, "John", 5000))
print(increase_salary(employees, "Doe", 5000))
"""
output:

"""
