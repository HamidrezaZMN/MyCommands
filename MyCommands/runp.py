#!/usr/bin/env python

import os, click

mc_help = '''
\b
name of the main class
it will find it automaticly if there's only one main class
(main class: class with main func)
'''
@click.command()
@click.option(
    '--main-class', '-mc',
    help='the name of the main class'
)
def cli(main_class):
    def checker(text):
        psv = 'public static void main'
        for i in range(len(text)-len(psv)):
            if text[i:i+len(psv)]==psv:
                return True
        return False

    # full path of the current py file
    rpath = os.getcwd()
    rpath = rpath.split('\\')

    # package of the java file
    package = rpath[-1]

    # extract java files
    all_files = os.listdir()
    java_files = []
    for file in all_files:
        if file.endswith('.java'):
            java_files.append(file)
            
    if main_class:
        main_file = main_class
    else:
        # extacting the java file with main method in it
        for java_file in java_files:
            file = open(java_file)
            if checker(file.read())==True:
                main_file = java_file
                file.close()
                break
            file.close()

    # going up one directory
    parent = os.path.dirname(os.getcwd())
    os.chdir(parent)

    # compile and running the package
    os.system(f'javac -cp . {package}/{main_file}')
    os.system(f'java -cp . {package}/{main_file}')

    # going back to the package
    os.chdir(package)

    # deleting all the class files
    for file in os.listdir():
        if file.endswith('.class'):
            os.system(f'del {file}')



if __name__ == '__main__':
    cli()