__version__ = '0.1.0'

import click

@click.command()
@click.option("--path", prompt="Enter path to analize",
              help="Folder path to look for audio files.")
def getGenre(path):
    """CLI to prepare and manage music selection."""
    click.echo("Path to look for files is: %s" % path)

if __name__ == '__main__':
    getGenre()