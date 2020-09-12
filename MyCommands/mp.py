#!/usr/bin/env python

import os, click, platform

# appropriate os
theOS = platform.system().lower()
if theOS not in ['linux', 'windows']:
    print('your os is not defined')
    print('your os: '+theOS+'\n')
    import sys; sys.exit()
cmds_ = {
    'linux' : {
        'desktop' : os.popen('echo $HOME').read().strip()+'/Desktop',
        'open' : 'xdg-open {}'
    },
    'windows' : {
        'desktop' : 'C:/Users/'+os.popen('echo %USERNAME%').read().strip()+'/desktop',
        'open' : 'start {}'
    }
}


help_ = {
    'destination' : '''
\b
the destination of the project
default is desktop
''',
    'open_folder' : '''
\b
use this to open the folder of the project
''',
    'open_editor' : '''
\b
use this to open the folder of the project with vscode
''',
    'powershell' : '''
\b
use this to open the terminal with powershell (if youre using windows)
it wil automaticly open it with cmd or bash (according to your os)
'''
}
main_file_help = '''
\b
name of the class with main method inside it
Note: it will automaticly be found if theres one class like that
'''

@click.command()
# type of the project
@click.argument('project_type')
# name of the project
@click.argument('project_name')
# name of the main-file
@click.argument('main_file')
# destination of the project
@click.option(
    '--destination', '-d',
    default=cmds_[theOS]['desktop'],
    help=help_['destination']
)
# open the folder or not
@click.option(
    '--open-folder', '-f',
    is_flag=True,
    help=help_['open_folder']
)
# open the editor or not
@click.option(
    '--open-editor', '-e',
    is_flag=True,
    help=help_['open_editor']
)
# open terminal with powershell
@click.option(
    '--powershell', '-p',
    is_flag=True,
    help=help_['powershell']
)
def cli(project_type, project_name, main_file, destination, open_folder, open_editor, powershell):
    '''
    makes a simple project

    \b
    syntax:
    main syntax is:
        $ mp <type-of-the-project> <name-of-the-project> <name-of-the-main-file>
    additional keys:
        -d / -f / -e / -p

    \b
    types:
        p/py/python      : python
        j/java           : java
        c                : c
        cpp/c++          : c++
        cs/c#            : c#
        h/html           : html
        js/javascript    : java script
        php              : php

    \b
    examples:
        $ mp python MyProject MainFile
        $ mp java MyProject MainFile -d E:/
        $ mp js MyProject MainFile -f -e
        $ mp php MyP MainF --open-editor --destination E:/ --powershell --open-folder
    '''

    # cd to destination
    os.chdir(destination)

    # make folder
    os.system(f'mkdir {project_name}')

    # make main file
    os.chdir(project_name)
    extensions = {
        '.py' : ['p', 'py', 'python'],
        '.java' : ['j', 'java'],
        '.c' : ['c'],
        '.cpp' : ['cpp', 'c++'],
        '.cs' : ['cs', 'c#'],
        '.html' : ['h', 'html'],
        '.js' : ['js', 'javascript'],
        '.php' : ['php']
    }
    for ext, values in extensions.items():
        if project_type in values:
            open(main_file+ext, 'w')
            break
    else:
        click.echo('\nnot a appropriate type')
        click.echo('main file didn\'t create')

    # open folder
    if open_folder:
        os.system(cmds_[theOS]['open'].format('.'))

    # open editor
    if open_editor:
        try:
            os.system('code .')
        except:
            click.echo('\ncan\'t open editor')
            click.echo('REASON: vscode is not installed')

    # open terminal
    terminal = 'bash' if theOS=='linux' else ('powershell' if powershell else 'cmd')
    os.system(terminal)


if __name__ == '__main__':
    cli()