"""

<h1> {{ heading }} </h1>

"""

from mf import component


@component(
    template="./home.component.html",
    styles=["./home.component.scss"],
)
class HomeComponent:
    def __init__(self):
        self.heading = "Welcome to new era!"

    def changeHeading(self):
        self.heading = "Welcome!"
