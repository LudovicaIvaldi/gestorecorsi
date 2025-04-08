from dataclasses import dataclass

from model import corso


@dataclass
class Studente:
    matricola: int
    cognome: str
    nome: str
    CDS: str
    # corsi: list[corso]=None
    # codins: list[str]=None #puoi decidere se farne uno 2 o tutti e 2


    def __eq__(self, other):
        return self.matricola == other.matricola
    def __hash__(self):
        return hash(self.matricola)
    def __str__(self):
        return f"{self.cognome} {self.nome} ({self.matricola}) - {self.CDS}"
