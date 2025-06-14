from dataclasses import dataclass

@dataclass
class Survey:
    title: str
    description: str
    id: int = None
