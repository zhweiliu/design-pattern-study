from dataclasses import dataclass


@dataclass
class DescriptionData:
    materials: list
    name: str
    output: float

    def __repr__(self) -> str:
        return str({
            'name': self.name,
            'materials': self.materials,
            'output': self.output
        })
