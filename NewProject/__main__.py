def Newproject(project):
    os.system(f'cp demo.py {project}.py')



if __name__ == '__main__':
    from subprocess import check_output
    import os
    import sys

    Newproject(sys.argv[1])
