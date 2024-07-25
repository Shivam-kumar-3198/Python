from taipy import Gui

page = """
<h1> Hey this is me </h1>

<p> Hloo Guys </p>

"""

if __name__ == "__main__":
    app = Gui()
    app.run(use_reloader=True)