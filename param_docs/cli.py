"""Console script for param_docs."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for param_docs."""
    click.echo("Replace this message by putting your code into "
               "param_docs.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
