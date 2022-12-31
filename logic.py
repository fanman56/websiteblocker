from pathlib import Path
from rich.console import Console
# main class

console = Console()


class Website():
    def __init__(self, site) -> None:
        self.orignalfile = Path("c:/Windows/System32/Drivers/etc/hosts")

        self.site = ' '.join(map(str, site))
    # blocking site method

    def block(self):
        newvar = self.orignalfile.read_text()+"\n"+"0.0.0.0 "+self.site
        self.orignalfile.write_text(newvar)
        console.print(f"{self.site} :Successfully blocked",
                      style="bold underline red")
    # unblocking site method

    def unblock(self):

        if self.site in self.orignalfile.read_text():
            newvar = self.orignalfile.read_text()
            out = newvar.replace("0.0.0.0 "+self.site, "")
            self.orignalfile.write_text(out)
            console.print(f"{self.site} :Unblocked successfully",
                          style='bold underline blue')

        else:
            console.print("Site already working", style='cyan')
    # list reading

    def readlist(self):
        console.print(self.orignalfile.read_text().rstrip())
