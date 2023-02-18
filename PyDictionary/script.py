import click

try:
    from .core import *
except:
    from core import *

@click.command()
@click.option('--mode','-m',default="meaning",help="Mode of Script [meaning, antonym, synonym]")
@click.option('--words', '-w',prompt="Enter words in a string separated by commas")
@click.option('--output','-o',default='console',help="Output format [console, file, database]")
@click.option('--filename','-f',default='output.txt',help="Output filename")
def script(words,mode,output,filename):
    """
    This script uses PyDictionary to find meanings, antonyms, or synonyms of words.
    """
    word_values = [w.strip() for w in words.split(',')]
    d = PyDictionary(word_values)
    maps = {"meaning":d.printMeanings,"antonym":d.printAntonyms,"synonym":d.printSynonyms}

    if output == 'console':
        click.echo(maps[mode]())
    elif output == 'file':
        with open(filename, 'w') as f:
            f.write(maps[mode]())
        click.echo(f"Output written to {filename}.")
    elif output == 'database':
        # Code to write to a database can be added here
        click.echo("Database output not yet implemented.")

if __name__ == '__main__':
    script()

