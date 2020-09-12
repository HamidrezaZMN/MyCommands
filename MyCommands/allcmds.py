#!/usr/bin/env python
import os, click


@click.command()
def cli():
    '''
    shows all commands
    '''

    source_path = os.path.realpath(os.path.dirname(__file__))
    lines = open(source_path+'/data/cmds_texts.txt', encoding='utf-8').readlines()
    for line in lines:
        line = line.strip()
        if line != '':
            click.echo(line)



if __name__ == '__main__':
    cli()