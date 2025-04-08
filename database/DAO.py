from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getCodins():
        cnx=DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor=cnx.cursor(dictionary=True)
            query="SELECT c.codins FROM corso c"
            cursor.execute(query)
           #lista di stringhe con il codice del corso
            for row in cursor:
                res.append(row["codins"])
            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getAllCorsi():
        cnx=DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            cursor=cnx.cursor(dictionary=True)
            query="SELECT * FROM corso c"
            cursor.execute(query)

            for row in cursor:
                #res.append(Corso(codins=row["codins"],crediti=row["crediti"], nome=row["nome"],pd= row["pd"]))
                res.append(Corso(**row))
                #il ** fa unpackp e passa al paramentro del costruttore di corso che ha lo stesso nome del dizionario la stessa cosa
            #processa res
            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getCorsiPD(pd):
        #guarda che qui pd deve essere 1 o 2 perchè nel data base sono così
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            #controlla che non sia non e e restituisci una lista vuota se è none

            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM corso c Where c.pd=%s"
            cursor.execute(query, (pd,))

            for row in cursor:
                # res.append(Corso(codins=row["codins"],crediti=row["crediti"], nome=row["nome"],pd= row["pd"]))
                res.append(Corso(**row))
                # il ** fa unpackp e passa al paramentro del costruttore di corso che ha lo stesso nome del dizionario la stessa cosa

            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getCorsiPDwithIscritti(pd):
        # guarda che qui pd deve essere 1 o 2 perchè nel data base sono così
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            # controlla che non sia non e e restituisci una lista vuota se è none

            cursor = cnx.cursor(dictionary=True)
            query = """select c.codins, c.crediti, c.nome, c.pd, count(*) as n
                        from corso c, iscrizione i
                        where c.codins=i.codins 
                        and c.pd=%s
                        group by c.codins, c.crediti, c.nome, c.pd"""


            cursor.execute(query, (pd,))

            for row in cursor:
               res.append((Corso(row["codins"], row["crediti"], row["nome"], row["pd"]), row["n"]))
                #per corso non puoi fare ** corso perchè hai anche la colonna n
            cursor.close()
            cnx.close()
            return res



    @staticmethod
    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            # controlla che non sia non e e restituisci una lista vuota se è none

            cursor = cnx.cursor(dictionary=True)
            query = """select  s.*
                        from iscrizione i, studente s
                        where i.matricola=s.matricola 
                        and i.codins=%s"""
            cursor.execute(query, (codins,))

            for row in cursor:
               res.append(Studente(**row))

            cursor.close()
            cnx.close()
            return res

    @staticmethod
    def getCDSofCorso(codins):
        cnx = DBConnect.get_connection()
        res = []
        if cnx is None:
            return res
        else:
            # controlla che non sia non e e restituisci una lista vuota se è none

            cursor = cnx.cursor(dictionary=True)
            query = """select  s.CDS, count(*) as n
                        from iscrizione i, studente s
                        where i.matricola=s.matricola 
                        and i.codins=%s
                        and s.CDS!=""
                        group by s.CDS"""

            cursor.execute(query, (codins,))

            for row in cursor:
                res.append((row["CDS"], row["n"]))

            cursor.close()
            cnx.close()
            return res




if __name__ == '__main__':
    print(DAO.getCodins())
    for c in DAO.getStudentiCorso("01KSUPG"):
     print(c)