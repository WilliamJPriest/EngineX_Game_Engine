
if __name__ == '__main__':
    import os
    from Editor.gui.error_windows import Error_Window_Tk

    try:
        os.system("python3 EngineX/demo.py")
    except Exception as e:
        Error_Window_Tk(e)
