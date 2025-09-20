from typer import Typer


app = Typer(name="pybrary", no_args_is_help=True)


@app.command("test", help="Test the CLI")
def do_test():
    print("It works!")


@app.command("book", help="Get a book")
def do_get_book(book_id: int):
    print("TODO")
