from tkinter import ttk
from tkinter import *
from Database import *
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

        self.form()
        self.table()

        self.window.mainloop()
        pass

    def form(self):

        def save():
            objects = self.formInputs.values()
            values = []

            for value in objects:
                values.append(value.get() if value.get() != "" else None)

            print(values)
            self.database.postUser(data=values)
            self.getUsers()
            pass

        form = Frame(self.window)
        form.grid(row=0, column=0, sticky=EW)

        inputs = Frame(form, bg="#00aaff")
        inputs.grid(row=0, column=0, sticky=EW)

        for i in range(0, 10):
            container = Frame(inputs)
            Label(container, text=self.titles[i]).grid(
                row=1, column=0, sticky=EW)
            self.formInputs[self.titles[i]] = Entry(container)
            self.formInputs[self.titles[i]].grid(row=1, column=1, sticky=EW)

            container.grid(row=i, sticky=EW)

        Button(form, text="Guardar", command=save).grid(
            row=1, columnspan=2, sticky=W+E)

        pass

    def table(self):
        self.table = ttk.Treeview(
            height=25, columns=self.columns, show='headings')
        self.table.grid(row=4, column=0)

        for index, column in enumerate(self.columns):
            self.table.heading(column, text=self.titles[index], anchor=W)
            self.table.column(column, width=100, stretch=True)

        self.getUsers()

    def getUsers(self):
        self.table.delete(*self.table.get_children())
        data = self.database.getUsers()
        for row in data:
            self.table.insert('', 0, text=self.titles[1], values=row[1:])

        pass


if __name__ == "__main__":
    database = Database("data.db")
    window = Tk()
    Application(window, database)
    pass
