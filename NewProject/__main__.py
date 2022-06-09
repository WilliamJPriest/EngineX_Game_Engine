from subprocess import check_output
import os
import sys



def Newproject(project):
    os.system(f'cp demo.py {project}')

Newproject(sys.argv[1])
