from Editor.project import *
if __name__ == '__main__':
    import os
    from Editor.gui.error_windows import Error_Window_Tk

    try:
        os.system(f"python3 EngineX/{projectFile}")
    except Exception as e:
        Error_Window_Tk(e)
