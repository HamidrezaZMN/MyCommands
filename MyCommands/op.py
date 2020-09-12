#!/usr/bin/env python

import os, click, platform

# appropriate os
theOS = platform.system().lower()
if theOS not in ['linux', 'windows']:
    print('your os is not defined')
    print('your os: '+theOS+'\n')
    import sys; sys.exit()
if theOS=='linux':
    desktop = os.popen('echo $HOME').read().strip()+'/Desktop'
else:
    desktop = 'C:/Users/'+os.popen('echo %USERNAME%').read().strip()+'/desktop'
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
    'address' : '''
\b
the directory where project is located
''',
    'open_folder' : '''
\b
use this to open the folder of the project
''',
    'powershell' : '''
use this to start the terminal with powershell
'''
}

@click.command()
# name of the folder of the project
@click.argument('project_name')
# address of the project
@click.option(
    '--address', '-a',
    default=cmds_[theOS]['desktop'],
    show_default=True,
    help=''
)
# open folder or not
@click.option(
    '--open-folder', '-f',
    is_flag=True,
    help=''
)
# open terminal with powershell or not
@click.option(
    '--powershell', '-p',
    is_flag=True,
    help=''
)
def cli(project_name, address, open_folder, powershell):
    '''
    
    '''

    # cd to project'f folder
    os.chdir(address+'/'+project_name)

    # open folder
    if open_folder:
        os.system(cmds_[theOS]['open'].format('.'))

    # open editor
    os.system('code .')

    # open terminal
    terminal = 'bash' if theOS=='linux' else ('powershell' if powershell else 'cmd')
    os.system(terminal)



if __name__ == '__main__':
    cli()