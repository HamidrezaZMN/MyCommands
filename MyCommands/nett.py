#!/usr/bin/env python

import os, click, subprocess, platform, configparser

# appropriate os
theOS = platform.system().lower()
if theOS not in ['linux', 'windows']:
    import sys
    print('your os is not defined')
    print('your os: '+theOS+'\n')
    sys.exit()
cmds_ = {
    'linux' : {
        'list_wifi' : 'nmcli d wifi list ifname wlan0',
        'connect' : 'nmcli d wifi connect "{}" password "{}" ifname wlan0',
        'disconnect' : 'nmcli d disconnect wlan0'
    },
    'windows' : {
        'list_wifi' : 'netsh wlan show profiles',
        'connect' : 'netsh wlan connect "{}"',
        'disconnect' : 'netsh wlan disconnect'
    }
}

# my data
config = configparser.ConfigParser()
source_path = os.path.realpath(os.path.dirname(__file__))
config.read(source_path+'/data/myinfo.config')
SSID = config['wifi_data']['SSID']
PASSWD = config['wifi_data']['PASSWD']


@click.command()
@click.option(
    '--list-wifi', '-l',
    is_flag=True,
    help='lists available wifis'
)
@click.option(
    '--start/--end', '-s/-e',
    is_flag=True,
    required=False,
    default=None,
    help='starts connection / end connection'
)
@click.argument(
    'ssid',
    default=SSID,
    required=False
)
@click.argument(
    'password',
    default=PASSWD,
    required=False
)
def cli(list_wifi, start, ssid, password):
    '''
    connect to network via this command

    \b
    syntax:
        $ nett -l
        $ nett -s
        $ nett -e
        $ nett -s YOUR_SSID
        $ nett -s YOUR_SSID YOUR_PASSWORD
    '''

    # wrong syntax
    if list_wifi and start is not None:
        click.echo('wrong syntax')
        click.echo('type "nett --help" for more info')

    else:
        if list_wifi:
            click.echo(os.popen(cmds_[theOS]['list_wifi']).read())

        if start is not None:
            if start:
                text = cmds_[theOS]['connect'].format(ssid, password)
            else:
                text = cmds_[theOS]['disconnect'].format(ssid, password)

            # execution
            try:
                subprocess.check_output(text, shell=True)
                click.echo('DONE!-----------')
            except:
                click.echo('something went wrong')




if __name__ == '__main__':
    cli()