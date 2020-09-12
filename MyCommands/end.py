#!/usr/bin/env python

import os, click, platform, sys
try:
    import psutil
except:
    try:
        os.system('pip3 install psutil')
    except:
        print('somthing went wrong installing pip3-psutil')
        sys.exit()
    import psutil


# appropriate os
theOS = platform.system().lower()
if theOS not in ['linux', 'windows']:
    print('your os is not defined')
    print('your os: '+theOS+'\n')
    import sys; sys.exit()
cmds_ = {
    'linux' : 'killall "{}"',
    'windows' : 'TASKKILL /F /IM "{}"'
}


@click.command()
@click.argument('program_name')
def cli(program_name):
    '''
    ends running programs and processes with name

    \b
    syntax:
        $ end python   >> ends python.exe
    '''

    # running programs
    running_programs = [p.name() for p in psutil.process_iter()]
    
    # all the programs including that name
    all_ = []
    for program in running_programs:
        if program_name in program:
            all_.append(program)


    def printPrograms(programs_names=all_):
        click.echo(f'{len(programs_names)} program with that name found:')
        for p in programs_names:
            click.echo('    '+p)


    def endPrograms(programs_names=set(all_)):
        try:
            flag = True
            for program in programs_names:
                output = os.popen(cmds_[theOS].format(program)).read()
                if 'success' not in output.lower():
                    flag = False
            if flag:
                click.echo('\nDONE!---------')
            else:
                click.echo('\none or more of the tasks failed')
        except:
            click.echo('somthing went wrong')



    # prints nothing happened
    def nothing_happened():
        click.echo('nothing happened')

    num_ = len(all_)
    if num_==0:
        click.echo('no program with that name found\n')
    elif num_==1:
        printPrograms()
        inp = input('\nend that? (y/n) ')
        if inp.strip().lower() in ['y', 'yes']:
            endPrograms()
        else:
            nothing_happened()
    else:
        printPrograms()
        inp = input('\nend them all? (y/n) ')
        if inp.strip().lower() in ['y', 'yes']:
            endPrograms()
        else:
            nothing_happened()




if __name__ == '__main__':
    cli()