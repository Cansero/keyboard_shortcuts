from infi.systray import SysTrayIcon
hover_text = "SysTrayIcon Demo"
def hello():
    print("Hello World.")
def simon():
    print("Hello Simon.")
def bye():
    print('Bye, then.')
def do_nothing():
    pass
menu_options = (('Say Hello', "hello.ico", hello, None),
                ('Do nothing', None, do_nothing, None),
                ('A sub-menu', "submenu.ico", (('Say Hello to Simon', "simon.ico", simon, None),
                                               ('Do nothing', None, do_nothing, None),
                                              ), None)
               )
sysTrayIcon = SysTrayIcon("main.ico", hover_text, menu_options, on_quit=[bye, None], default_menu_index=1)
sysTrayIcon.start()
