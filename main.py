from tkinter import ttk
from tkinter import *
from Database import *
from Form import *
import sqlite3


class Application:
    def __init__(self, window, database):
        self.window = window
        self.database = database
        self.columns = ('first_name', 'first_last_name', 'second_last_name',
                        'age', 'gender', 'school', 'address', 'curp', 'category', 'fee')
        self.titles = ('Nombre', 'Apellido paterno', 'Apellido materno',
                       'Edad', 'Sexo', 'Escuela', 'Domicilio', 'CURP', 'Categoría', 'Inscripción')
        self.formInputs = {}

        self.window.title("Administrador de participantes")

        self.searchBar()
        self.table()

        delete = Button(self.window, text="Eliminar", command=self.deleteUser)
        delete.grid(row=5, column=0, sticky=EW)

        edit = Button(self.window, text="Editar", command=self.updateUser)
        edit.grid(row=5, column=1, sticky=EW)

        add = Button(self.window, text="Agregar", command=self.addUser)
        add.grid(row=5, column=2, sticky=EW)

        self.window.mainloop()
        pass

    def searchBar(self):
        # container = Frame(self.window)
        # container.grid(row=0, column=0, columnspan=12, sticky=EW)

        searchInput = Entry(self.window)
        searchInput.grid(row=0, column=0, columnspan=8, sticky=EW)

        clearButton = Button(self.window, text="Limpiar",
                             command=lambda: self.getUsers())
        clearButton.grid(row=0, column=8, columnspan=2, sticky=EW)

        searchButton = Button(self.window, text="Buscar", command=lambda: self.searchUsers(
            "%" + searchInput.get() + "%"))
        searchButton.grid(row=0, column=10, columnspan=2, sticky=EW)

    def table(self):
        self.table = ttk.Treeview(
            height=15, columns=self.columns, show='headings')
        self.table.grid(row=2, columnspan=12, column=0)
        self.table.bind("<Double-1>", self.open_toplevel)

        for index, column in enumerate(self.columns):
            self.table.heading(column, text=self.titles[index], anchor=W)
            self.table.column(column, width=100, stretch=True)

        self.getUsers()

    def getUsers(self):
        self.table.delete(*self.table.get_children())
        data = self.database.getUsers()
        for row in data:
            self.table.insert('', 0, text=row[0], values=row[1:])

    def searchUsers(self, data):
        self.table.delete(*self.table.get_children())
        data = self.database.searchUsers((data, data, data))
        for row in data:
            self.table.insert('', 0, text=row[0], values=row[1:])

    def deleteUser(self):
        try:
            item = self.table.item(self.table.selection())['text']
            self.database.deleteUser((str(item),))
        except Exception as e:
            print(e)
        finally:
            self.getUsers()
        print(item)
        pass

    def updateUser(self):
        self.editForm = Toplevel()
        self.editForm.title("Editar usuario")
        form = Form(self, 0, 0, self.titles)

    def addUser(self):
        # self.editForm = Toplevel()
        # self.editForm.title("Editar usuario")
        form = Form(self, 0, 0, self.titles)

    def open_toplevel(self, event):
        selected_item = self.table.focus()  # obtenemos el item seleccionado
        if selected_item:  # si se seleccionó un item
            form = Form(self, 0, 0, self.titles, self.table.item(selected_item)[
                        'values'], self.table.item(selected_item)['text'])
            # pass

            # toplevel = Toplevel()
            # toplevel.geometry("200x100")
            # label = Label(toplevel, text=f"Item seleccionado: {self.table.item(selected_item)['values']}")
            # label.pack()


if __name__ == "__main__":
    database = Database("data.db")
    window = Tk()
    Application(window, database)
    pass
