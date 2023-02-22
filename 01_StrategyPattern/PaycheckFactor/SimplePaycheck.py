from .IPaycheckFactor import IPaycheckFactor
import random


class SimplePaycheck(IPaycheckFactor):

    def __init__(self, employee_id: int):
        super().__init__(employee_id)
        self._hourly_wage: float = 200.0

    def get_paycheck_factor(self) -> float:
        self._factor = self._hourly_wage * self._search_worked_time_by_employee_id()
        return self._factor

    def _search_worked_time_by_employee_id(self):
        # assume to query worked time in current month from db,
        # but simulate by random function for return value
        return random.randrange(start=160, stop=214)
