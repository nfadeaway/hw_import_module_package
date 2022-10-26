from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime, date

employees = ['Иванов Иван Иванович', 'Петров Пётр Петрович']

if __name__ == '__main__':
    print(f'Информация по состоянию на {datetime.today().date()}')
    get_employees(employees)
    calculate_salary(employees[0], 1200, 25)
