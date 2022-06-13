import tkinter

class Error_Window_Tk:
    def err_win_tk(self, err):
        compiler = tkinter.Tk()
        compiler.title(err)
        text = tkinter.Label(compiler, text=f'{err}', width=40)
        text.pack()
        compiler.mainloop()