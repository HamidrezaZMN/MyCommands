#!/usr/bin/env python

import click, requests

@click.command()
@click.option(
    '--video', '-v', 
    is_flag=True, 
    help='the extension is mp4'
)
@click.option(
    '--picture', '-p', 
    is_flag=True, 
    help='the extension is jpg'
)
@click.argument('file_name')
@click.argument('url')
def cli(video, picture, file_name, url):
    '''
    download file from the url

    \b
    examples:
        dlfile facebook_icon.ico "http://facebook.com/some/url/containing/icon/file"

    \b
    if it's a mp4 or jpg file you can use this:
    dlfile -v file-name "http://url/with/video/"
    dlfile -p file-name "http://url/with/picture/"
    '''

    def wrong_syntax():
        click.echo('wrong syntax')
        click.echo('type "dlfile --help" for more info')

    # make the name
    name = file_name
    if video and picture:
        wrong_syntax()
    
    elif video:
        if '.' in video:
            wrong_syntax()
        else:
            name = file_name+'.mp4'
    
    elif picture:
        if '.' in video:
            wrong_syntax()
        else:
            name = file_name+'.jpg'
    

    if '.' not in name:
        wrong_syntax()
    else:
        # download the file
        r = requests.get(url, allow_redirects=True)
        open(name, 'wb').write(r.content)



if __name__ == '__main__':
    cli()