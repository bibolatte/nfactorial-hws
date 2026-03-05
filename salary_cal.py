basic_salary = 500000
bonus = 50000
tax = 0.13
employee_name = "Bibolat"

salary = basic_salary + bonus
need_tax = salary * tax
net_salary =  salary - need_tax

print(f"Сотрудник: {employee_name}")
print(f"Зарплата до налогов: {salary} тенге")
print(f"Налог: {need_tax} тенге")
print(f"к выплате: {net_salary} tenge")
print(type(salary))