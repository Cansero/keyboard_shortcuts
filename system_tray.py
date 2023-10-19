from infi.systray import SysTrayIcon


class Variables:
    text = 'esto es un texto'

    def update_text(self, newtext):
        self.text = newtext
        return


def say_hello():
    print("Hello, World!")


def print_anotther_thing(text):
    print(text)


argument = Variables()
menu_options = (("Say Hello", None, say_hello),
                ("Otra funcion", None, print_anotther_thing, argument))

systray = SysTrayIcon(None, "Example tray icon", menu_options)
argument.update_text("otro texto namas pa ver que jale")
systray.start()
argument.update_text('esto es despues de empezar')