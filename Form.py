from tkinter import ttk
from tkinter import *
from Exporter import *


class Form:
    def __init__(self, parent, row, column, titles, values=None, identifier=None):
        self.exporter = Exporter()
        self.parent = parent
        self.formInputs = {}
        self.values = values
        self.identifier = identifier

        self.window = Toplevel()
        self.window.title("Agregar participante" if values ==
                          None else "Detalles del participante")

        # Sección de formulario
        form = LabelFrame(self.window, text="Formulario")
        form.pack(fill=X, padx=5, pady=5)

        for i in range(0, 10):
            container = Frame(form)
            label = Label(container, text=titles[i], width=15, anchor=W)
            label.pack(side=LEFT)

            self.formInputs[titles[i]] = Entry(container, width=25)
            self.formInputs[titles[i]].pack(side=LEFT, fill=X, expand=True)
            if values:
                self.formInputs[titles[i]].insert(
                    0, values[i] if values[i] != "None" else "")

            container.pack(fill=X, expand=True, side=TOP)

        # Sección de impresión de tickets
        prints = LabelFrame(self.window, text="Impresiones")
        prints.pack(fill=X, padx=5, pady=5)

        container = Frame(prints)

        label = Label(container, text="Tipo de archivo", width=15, anchor=W)
        label.pack(side=LEFT)

        extension = ttk.Combobox(
            container, values=["DOCX", "PDF", "TXT"], state="readonly")
        extension.current(0)
        extension.pack(side=LEFT, fill=X, expand=True)

        container.pack(fill=X, expand=True, padx=5, pady=5)

        ticket = Button(prints, text="Comprobante de pago",
                        command=lambda: self.getTicket(extension.get()), width=10)
        ticket.pack(fill=X, expand=True, padx=5, pady=5)

        certificate = Button(prints, text="Certificado",
                             command=lambda: self.getTicket(extension.get()), width=10)
        certificate.pack(fill=X, expand=True, padx=5, pady=5)

        firstPlace = Button(prints, text="Primer lugar",
                            command=lambda: self.getTicket(extension.get()), width=10)
        firstPlace.pack(fill=X, expand=True, padx=5, pady=5)

        secondPlace = Button(prints, text="Segundo lugar",
                             command=lambda: self.getTicket(extension.get()), width=10)
        secondPlace.pack(fill=X, expand=True, padx=5, pady=5)

        thirdPlace = Button(prints, text="Tercer lugar",
                            command=lambda: self.getTicket(extension.get()), width=10)
        thirdPlace.pack(fill=X, expand=True, padx=5, pady=5)

        # Sección de acciones
        actions = LabelFrame(self.window, text="Acciones")
        actions.pack(fill=X, padx=5, pady=5)

        if values is not None:
            cancel = Button(actions, text="Eliminar",
                            command=self.delete, width=10)
            cancel.pack(fill=X, expand=True, padx=5, pady=5)

        cancel = Button(actions, text="Cancelar", command=self.close, width=10)
        cancel.pack(side=LEFT, fill=X, expand=True, padx=5, pady=5)

        action = Button(actions, text="Guardar" if values == None else "Actualizar",
                        command=self.save if values == None else self.update, width=10)
        action.pack(side=LEFT, fill=X, expand=True, padx=5, pady=5)

    def getTicket(self, extension):
        success = self.exporter.getTicket(self.values, extension)

        alert = Toplevel()
        alert.title("Alerta")
        description = Label(alert, text="El documento ha sido creado" if success ==
                            True else "Ocurrió un error, inténtelo nuevamente")
        description.pack(fill=X, expand=True, padx=5, pady=5)

        button = Button(alert, text="Aceptar", width=10, command=alert.destroy)
        button.pack(fill=X, expand=True, padx=5, pady=5)

    def getCertificate(self, extension):
        success = self.exporter.getTicket(self.values, extension)

        alert = Toplevel()
        alert.title("Alerta")
        description = Label(alert, text="El documento ha sido creado" if success ==
                            True else "Ocurrió un error, inténtelo nuevamente")
        description.pack(fill=X, expand=True, padx=5, pady=5)

        button = Button(alert, text="Aceptar", width=10, command=alert.destroy)
        button.pack(fill=X, expand=True, padx=5, pady=5)

    def getAward(self, extension):
        success = self.exporter.getTicket(self.values, extension)

        alert = Toplevel()
        alert.title("Alerta")
        description = Label(alert, text="El documento ha sido creado" if success ==
                            True else "Ocurrió un error, inténtelo nuevamente")
        description.pack(fill=X, expand=True, padx=5, pady=5)

        button = Button(alert, text="Aceptar", width=10, command=alert.destroy)
        button.pack(fill=X, expand=True, padx=5, pady=5)

    def close(self):
        return self.window.destroy()

    def save(self):
        objects = self.formInputs.values()
        values = []

        for value in objects:
            values.append(value.get())

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
            values.append(value.get())

        try:
            success = self.parent.database.patchUser(
                data=(*values, self.identifier))
            print(success)
            if success:
                self.parent.getUsers()
                self.close()
        except Exception as e:
            print(e)

    def delete(self):
        try:
            success = self.parent.database.deleteUser(str(self.identifier))

            if success:
                self.parent.getUsers()
                self.close()
        except Exception as e:
            print(e)
