import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddCodinsValue= None

    def fillddCodins(self):
         # for cod in self._model.getCodins():
         #     self._view.ddCodins.options.append(ft.dropdown.Option(cod))
         for c in self._model.getAllCorsi():
             self._view.ddCodins.options.append(ft.dropdown.Option(key=c.codins,
                                                                   data=c,
                                                                   on_click=self._chiceDDCodins))
            #quando seleziono la voce mi va a eseguire on click

    def ddCodinsSelected(self,e):
        #viene chiamato quando schiacci su una opzione del dd
        print(type(self._view.ddCodins.value))  #ti dice di che tipo è il value del dd che hai selezionato

    def _chiceDDCodins(self,e):
        self._ddCodinsValue=e.control.data #in data ho oggetto e lo recupero dandolo al ddCodinsValue che è una variabile del controller
        print(self._ddCodinsValue)
        print(type(self._ddCodinsValue))

    def handlePrintCorsiPD(self,e):
        #stampa corsi di un periodo didattico scelto nel dd (corsi del I o del II)
        self._view.lvTxtOut.controls.clear()
        pd=self._view.ddPD.value #guarda che è I o II a te serve 1 o 2
        if pd is None:
            self._view.create_alert("Attenzione selezionare un periodo didattico")
            #alert è già fatto basta chiamare e passare un messaggio da visualizzare
            self._view.update_page()
            return

        #a questo punto pd è uguale a I o a II invece il modello si aspetta 1 o 2
        if pd=="I":
            pdInt=1
        else:
            pdInt=2

        corsiPD=self._model.getCorsiPd(pdInt)
        if len(corsiPD)==0:
            #qui non ci entro mai perchè il data base è pieno, ma fa parte dei controlli che dev fare
            self._view.lvTxtOut.controls.append(ft.Text(f"Nessun corso trovato in questo periodo"))
            self._view.update_page()
            return
        self._view.lvTxtOut.controls.append(ft.Text(f"Corsi del {pd} periodo didattico", color="green"))
        for c in corsiPD:
            self._view.lvTxtOut.controls.append(ft.Text(c))

        self._view.update_page()




    def handlePrintIscrittiCorsiPD(self,e):
        #stampa numero di iscritti ai corsi di un periodo didattico scelto
        self._view.lvTxtOut.controls.clear()
        pd=self._view.ddPD.value
        if pd is None:
            self._view.create_alert("Attenzione selezionare un periodo didattico")
            self._view.update_page()
            return
        if pd=="I":
            pdInt=1
        else:
            pdInt=2
        corsiPdwithIscritti=self._model.getCorsiPdwithIscritti(pdInt)

        if len(corsiPdwithIscritti)==0:
            #qui non ci entro mai perchè il data base è pieno, ma fa parte dei controlli che dev fare
            self._view.lvTxtOut.controls.append(ft.Text(f"Nessun corso trovato in questo periodo"))
            self._view.update_page()
            return

        self._view.lvTxtOut.controls.append(ft.Text(f"Dettagli corsi del periodo didattico"))
        for c in corsiPdwithIscritti:
            self._view.lvTxtOut.controls.append(ft.Text(f"{c[0]} -> Numero iscritti: {c[1]}"))
        self._view.update_page()
        return


    def handlePrintIscrittiCodins(self,e):
        #stampa tutti gli studenti iscritti al corso selezionato
        #codins = self._view.ddCodins.value  # così hai una stringa
        self._view.lvTxtOut.controls.clear()
        if self._ddCodinsValue is None: #così hai l'oggetto
            self._view.create_alert("Attenzione selezionare un corso di interesse")
            self._view.update_page()
            return
        students=self._model.getStudentiCorso(self._ddCodinsValue.codins)
        if len(students) == 0:
            # qui non ci entro mai perchè il data base è pieno, ma fa parte dei controlli che dev fare
            self._view.lvTxtOut.controls.append(ft.Text(f"Nessuno studente trovato"))
            self._view.update_page()
            return

        self._view.lvTxtOut.controls.append(ft.Text(f"Studenti iscritti al corso {self._ddCodinsValue}"))

        for s in students:
            self._view.lvTxtOut.controls.append(ft.Text(s))
        self._view.update_page()




    def handlePrintCDSCodins(self,e):
        #divisione degli studenti iscritti a quel croso per corso di studi frequentato
        self._view.lvTxtOut.controls.clear()
        if self._ddCodinsValue is None:  # così hai l'oggetto
            self._view.create_alert("Attenzione selezionare un corso di interesse")
            self._view.update_page()
            return
        cds=self._model.getCDSofCorso(self._ddCodinsValue.codins)

        if len(cds) == 0:
            # qui non ci entro mai perchè il data base è pieno, ma fa parte dei controlli che dev fare
            self._view.lvTxtOut.controls.append(ft.Text(f"Nessuno corso di studi offre questo corso"))
            self._view.update_page()
            return


        self._view.lvTxtOut.controls.append(ft.Text(f"CDS che frequentano il corso {self._ddCodinsValue}"))
        for c in cds:
            self._view.lvTxtOut.controls.append(ft.Text(f"CDS: {c[0]} - Numero iscritti: {c[1]}"))

        self._view.update_page()
