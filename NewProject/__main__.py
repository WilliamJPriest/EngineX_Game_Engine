def NewProjectLinux(project):
    os.system(f'bash NewProject/new_project_linux.sh {project}')



if __name__ == '__main__':
    import os
    import sys

    NewProjectLinux(sys.argv[1])
