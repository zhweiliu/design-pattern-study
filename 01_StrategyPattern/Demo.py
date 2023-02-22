from SalaryDef import SalaryCalculator
from PaycheckFactor import SimplePaycheck, TicketPaycheck

if __name__ == '__main__':

    salary_calculator_for_employee_1 = SalaryCalculator(SimplePaycheck(employee_id=1002003))
    salary_calculator_for_employee_2 = SalaryCalculator(TicketPaycheck(employee_id=3002001))

    print(f'employee_1 salary of this month : {salary_calculator_for_employee_1.salary_calculating()}')
    print(f'employee_2 salary of this month : {salary_calculator_for_employee_2.salary_calculating()}')
