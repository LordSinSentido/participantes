from tkinter import ttk
from tkinter import *


class Form:
    def __init__(self, parent, row, column, titles, values=None, identifier=None):
        self.parent = parent
        self.formInputs = {}
        self.identifier = identifier

        self.window = Toplevel()
        self.window.title("Agregar participante" if values ==
                          None else "Actualizar participante")

        form = Frame(self.window, bg="#00aaff", background="#00aaff")
        form.grid(row=row, column=column, sticky=EW)

        inputs = Frame(form)
        inputs.grid(row=0, column=0, columnspan=2, sticky=EW)

        for i in range(0, 10):
            container = Frame(inputs, pady=2)
            Label(container, text=titles[i]).grid(
                row=0, column=0, columnspan=2, sticky=EW)
            self.formInputs[titles[i]] = Entry(container)
            self.formInputs[titles[i]].grid(
                row=0, column=3, columnspan=2, sticky=EW)
            if values:
                self.formInputs[titles[i]].insert(
                    0, values[i] if values[i] != "None" else "")

            container.grid(row=i, column=0, columnspan=2, sticky=EW)

        if values:
            Button(form, text="Actualizar", command=self.update).grid(
                row=1, column=1, sticky=EW)
        else:
            Button(form, text="Guardar", command=self.save).grid(
                row=1, column=1, sticky=EW)

        Button(form, text="Cancelar", command=self.close).grid(
            row=1, column=0, sticky=EW)

    def close(self):
        return self.window.destroy()

    def save(self):
        objects = self.formInputs.values()
        values = []

        for value in objects:
            values.append(value.get() if value.get() != "" else None)

        try:
            success = self.parent.database.postUser(data=values)
            print(success)
            if success:
                self.parent.getUsers()
                self.close()
        except Exception as e:
            print(e)

    def update(self):
        objects = self.formInputs.values()
        values = []

        for value in objects:
            values.append(value.get() if value.get() != "" else None)

        try:
            success = self.parent.database.patchUser(data=(*values, self.identifier))
            print(success)
            if success:
                self.parent.getUsers()
                self.close()
        except Exception as e:
            print(e)
