#!/usr/bin/env python

import click, os

@click.command()
@click.option(
    '--extension', '-e',
    default='.py',
    help='''
    \b
    extension of the codes
    default is .py
    '''
)
@click.option(
    '--directory', '-d',
    default=os.getcwd(),
    help='''
    \b
    directory you want to count all lines of code inside it
    '''
)
@click.option(
    '--without-comment', '-wc',
    help='''
    \b
    use this to omit comment lines

    \b
    Caution: after -wc you have to enter the comment sign in that language,
    for example, in python it's "#" and in java it's "//"
    '''
)
def cli(extension, directory, without_comment):
    '''
    \b
    counts the number of the lines of the code, in one directory
    default extension is .py

    \b
    syntax:
        $ count-lines
        $ count-lines --extension .java
        $ count-lines --extension .java --directory C:/
        $ count-lines --extension .java --without-comment //
    \b
    Note: 
    '''

    res = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                lines = open(root+'\\'+file, closefd=True).readlines()
                for line in lines:
                    line = line.strip()
                    condition = line != ''
                    if without_comment:
                        condition = condition & (not line.startswith(without_comment))
                    if condition:
                        res += 1
    click.echo(str(res)+' lines')




if __name__ == "__main__":
    cli()