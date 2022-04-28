import typer
from beerlog.core import add_beer_to_database, get_beers_from_database

main = typer.Typer(help="Beer Management Application")

@main_command('add')
def add(
    name: str, 
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...)
    ):
    '''Adds a new beer to database.'''
    if add_beer_to_database(name, style, flavor, image, cost):
        print("Beer added to database.")
    else:
        print("Something went wrong.")

@main_command('list')
def list_beers(style: str) -> List[Beer]:
    '''Lists beers in database.'''
    beers = get_beers_from_database()
    print(beers)
