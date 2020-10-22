from mf import Component


@Component(
    template="./home.component.html",
    styles=["./home.component.scss"]
)
class HomeComponent:
    def __init__(self):
        self.heading = "We're in home"
    
    def updateHeading(self):
        self.updateHeading()
