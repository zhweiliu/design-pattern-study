from abc import ABC, abstractmethod


class IPaycheckFactor(ABC):

    def __init__(self, employee_id: int):
        self._employee_id: int = employee_id
        self._factor: float = -1.0

    @abstractmethod
    def get_paycheck_factor(self) -> float:
        """
        Get work factor with employee id
        :return: (float) total hours of worked time or others
        """
        pass
