#!/usr/bin/env python

import click, os, platform

theOS = platform.system().lower()
if theOS not in ['linux', 'windows']:
    print('your os is not defined')
    print('your os: '+theOS+'\n')
    import sys; sys.exit()


def FindDir(rootDir, folder):
    root = ''
    dirs = []
    for r, d, t in os.walk(rootDir):
        root = r
        dirs = d
        break

    all = []
    for directory in dirs:
        if folder.lower() in directory.lower():
            all.append(directory)

    cd_text = ''
    if len(all)!=0:
        if len(all)==1:
            cd_text = all[0]
        else:
            for x in range(len(all)):
                click.echo(f'{x}. {all[x]}')
            inp = int(input('\nenter: '))
            cd_text = all[inp]
    return cd_text


@click.command()
@click.argument('directory_name')
@click.option(
    '--powershell', '-p', 
    is_flag=True, 
    help='''
use it to open with poweshell
instaed of cmd (if you use windows)
''',
)
def cli(directory_name, powershell):
    """
    cd to directory with few characters
    
    \b
    syntax:
    if you want to cd to "myfolder"
    type: ecd fol
    if more than one dir has "fol" in it, it will ask you to choose
    else, it will automaticly cd to that
    """
    
    terminal = 'bash' if theOS=='linux' else ('powershell' if powershell else 'cmd')
    dest = FindDir(os.getcwd(), directory_name)
    if dest=='':
        click.echo('there is no directory called '+directory_name)
    else:
        os.chdir(dest)
        os.system(terminal)



if __name__ == '__main__':
    cli()