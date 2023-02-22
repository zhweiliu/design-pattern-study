from PaycheckFactor import IPaycheckFactor


class SalaryCalculator:

    def __init__(self, paycheck_factor: IPaycheckFactor):
        self.paycheck_factor: IPaycheckFactor = paycheck_factor

    def salary_calculating(self) -> float:
        return self.paycheck_factor.get_paycheck_factor()
