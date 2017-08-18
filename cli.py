import click
from tapedeck.tar import TAR_COMPRESSIONS
COMP_OPTIONS = list(TAR_COMPRESSIONS.keys())
COMP_OPTIONS.append("none")

@click.group()
def tapedeck():
    pass


@tapedeck.command()
def hello():
    click.echo("Hello World!")


@tapedeck.command()
@click.option("-n", "--number", help="number of files to put in tar", default=2)
@click.option("-c", "--compression", help="compression options", type=click.Choice(COMP_OPTIONS), default="none")
def stream(number, compression):
    from tapedeck.tar import write_tar
    from tapedeck.data import FILES
    from tapedeck.streams import StdOutByteWriter

    write_tar(FILES, StdOutByteWriter(), compression=compression)


if __name__ == "__main__":
    tapedeck()