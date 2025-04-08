from dataclasses import dataclass

from model import studente


@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int
    # studenti: list[studente]=None
    # matricole: list[str] =None


    def __eq__(self,other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)

    def __str__(self):
        return f"{self.nome} ({self.codins})- {self.crediti} cfu"