from tkinter import *

class IDE:
    def __init__(self, title, **kwargs):
        self.title = title

    def run(self):
        code = self.editor.get('1.0', END)
        exec(code)

    def run_ide(self):
        compiler = Tk()
        compiler.title(self.title)
        menu_bar = Menu(compiler)
        run_bar = Menu(menu_bar)
        run_bar.add_command(label='Run', command=self.run)
        menu_bar.add_cascade(label='Run', menu=run_bar)
        compiler.config(menu=menu_bar)
        self.editor = Text(bg='darkblue',fg='white')
        self.editor.pack()
        compiler.mainloop()

if __name__ == '__main__':
    IDE('Add Script').run_ide()
