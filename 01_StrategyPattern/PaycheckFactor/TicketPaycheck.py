from .IPaycheckFactor import IPaycheckFactor
import random


class TicketPaycheck(IPaycheckFactor):

    def __init__(self, employee_id: int):
        super().__init__(employee_id)
        self._finished_tickets: int = -1
        self._ticket_bonus: float = 40.0

    def get_paycheck_factor(self) -> float:
        employee_finished_tickets = self._search_finished_tickets_by_employee_id()
        self._factor = self._ticket_bonus * employee_finished_tickets
        return self._factor

    def _search_finished_tickets_by_employee_id(self):
        # assume each ticket can be finished in 10 minutes
        # and push ticket per 10 minutes
        return random.randrange(start=480, stop=1440)
