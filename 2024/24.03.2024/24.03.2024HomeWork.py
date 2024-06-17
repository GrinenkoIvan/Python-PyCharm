# class PayrollSystem:
#     def calculate(self, employees):
#         print("Расчёт заработной платы:")
#         print("=" * 60)
#         for employee in employees:
#             print(f"Заработная плата: {employee.id} - {employee.name}")
#             print(f"- Проверить сумму: {employee.calculate_payroll()}")
#             print()
#
#
# class Employee:
#     def __init__(self, id_employee, name):
#         self.id = id_employee
#         self.name = name
#
#
# class SalaryEmployee(Employee):
#
#     def __init__(self, id_employee, name, weekly_salary):
#         super().__init__(id_employee, name)
#         self.weekly_salary = weekly_salary
#
#     def calculate_payroll(self):
#         return self.weekly_salary
#
#
# class HourlyEmployee(Employee):
#
#     def __init__(self, id_employee, name, hours_worked, hour_rate):
#         super().__init__(id_employee, name)
#         self.hours_worked = hours_worked
#         self.hour_rate = hour_rate
#
#     def calculate_payroll(self):
#         return self.hours_worked * self.hour_rate
#
#
# class CommissionEmployee(Employee):
#
#     def __init__(self, id_employee, name, weekly_salary, commission_rate):
#         super().__init__(id_employee, name)
#         self.weekly_salary = weekly_salary
#         self.commission_rate = commission_rate
#
#     def calculate_payroll(self):
#         return self.weekly_salary + self.commission_rate
#
#
# salary_employee = SalaryEmployee(1, "Валерий Задорожний", 1500)
# hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
# commission_employee = CommissionEmployee(3, "Николай Хорольский", 1000, 250)
#
# payroll_system = PayrollSystem()
# payroll_system.calculate([salary_employee, hourly_employee, commission_employee])
