import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.lvTxtOut = None
        self._page = page
        self._page.title = "Gestore corsi edizione 2025"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddPD = None
        self.ddCodins= None
        self.btnPrintCordiPD= None
        self.btnPrintIscrittiCorsiPD= None
        self.btnPrintIscrittiCodins= None
        self.btnPrintCDSCodins= None

    def load_interface(self):
        self.title=ft.Text("Gestione corsi edizione 2025", color="blue")
        self.ddPD = ft.Dropdown(label="Periodo didattico", options=[ft.dropdown.Option("I"), ft.dropdown.Option("II")])
        self.ddCodins = ft.Dropdown(label="Codice corso")
        #ci metto dentro un on click per poter tirare fuori oggetto se no mi da sempre una stringa

        #devo decidere se mettere nei dd delle sctringhe o dei oggetti
        self._controller.fillddCodins() #chiede al modello che chiede al dao e torna indietro

        self.btnPrintCordiPD = ft.ElevatedButton(text="Stampa corsi di un PD", on_click=self._controller.handlePrintCorsiPD, width=300)
        self.btnPrintIscrittiCorsiPD = ft.ElevatedButton(text="Stampa numero iscritti ", on_click=self._controller.handlePrintIscrittiCorsiPD, width=300)
        self.btnPrintIscrittiCodins = ft.ElevatedButton(text="Stampa iscritti al corso", on_click=self._controller.handlePrintIscrittiCodins, width=300)
        self.btnPrintCDSCodins = ft.ElevatedButton(text="Stampa CDS afferenti", on_click=self._controller.handlePrintCDSCodins, width=300)
        self.lvTxtOut= ft.ListView(expand=True)

        row1=ft.Row([self.ddPD,self.btnPrintCordiPD, self.btnPrintIscrittiCorsiPD], alignment=ft.MainAxisAlignment.CENTER)
        row2=ft.Row([self.ddCodins,self.btnPrintIscrittiCodins,self.btnPrintCDSCodins], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add( self.title,row1, row2, self.lvTxtOut)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
