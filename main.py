from tkinter import ttk
from tkinter import *
from Database import *
from Form import *
from tkinter.font import Font
import sqlite3


class Application:
    def __init__(self, window, database):
        self.database = database
        self.window = window
        self.window.title("Administrador de participantes")

        self.formInputs = {}
        self.columns = ('first_name', 'first_last_name', 'second_last_name',
                        'age', 'gender', 'school', 'address', 'curp', 'category', 'fee')
        self.titles = ('Nombre', 'Apellido paterno', 'Apellido materno',
                       'Edad', 'Sexo', 'Escuela', 'Domicilio', 'CURP', 'Categoría', 'Inscripción')

        title = Label(
            self.window, text="Sistema de gestión de participantes")
        title.pack()

        self.header = Frame(self.window)
        self.header.pack(fill=X, padx=5, pady=5)

        self.add()
        self.searchBar()
        self.table()

        self.window.mainloop()
        pass

    def searchBar(self):
        container = LabelFrame(
            self.header, text="Buscar por nombre o apellidos")
        container.pack(fill=X, expand=True, side=LEFT)

        searchInput = Entry(container)
        searchInput.pack(expand=True, fill=BOTH, side=LEFT, padx=5, pady=5)

        clearButton = Button(container, text="Limpiar",
                             command=lambda: self.getUsers(), width=10)
        clearButton.pack(fill=BOTH, side=LEFT, padx=5, pady=5)

        searchButton = Button(container, text="Buscar", command=lambda: self.searchUsers(
            "%" + searchInput.get() + "%"), width=10)
        searchButton.pack(fill=BOTH, side=LEFT, padx=5, pady=5)

    def add(self):
        container = LabelFrame(self.header, text="Agregar")
        container.pack(side=LEFT)

        add = Button(container, text="Agregar", command=self.addUser, width=10)
        add.pack(padx=5, pady=5)

    def table(self):
        self.table = ttk.Treeview(
            height=15, columns=self.columns, show='headings')
        self.table.pack(fill=BOTH, expand=True, padx=5, pady=5)
        self.table.bind("<Double-1>", self.showUser)

        for index, column in enumerate(self.columns):
            self.table.heading(column, text=self.titles[index], anchor=W)
            self.table.column(column, width=100, stretch=True)

        self.getUsers()

    def getUsers(self):
        self.table.delete(*self.table.get_children())
        data = self.database.getUsers()
        for row in data:
            self.table.insert('', 0, text=row[0], values=row[1:])

    def searchUsers(self, query):
        self.table.delete(*self.table.get_children())
        data = self.database.searchUsers(query)
        for row in data:
            self.table.insert('', 0, text=row[0], values=row[1:])

    def addUser(self):
        form = Form(self, 0, 0, self.titles)

    def showUser(self, event):
        selected_item = self.table.focus()
        if selected_item:
            form = Form(self, 0, 0, self.titles, self.table.item(selected_item)[
                        'values'], self.table.item(selected_item)['text'])


if __name__ == "__main__":
    database = Database("data.db")
    window = Tk()
    Application(window, database)
    pass
