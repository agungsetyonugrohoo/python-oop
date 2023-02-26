class Team:
    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(self.team)

class Tipe_Hero:
    def setTipe(self, tipe):
        self.tipe = tipe
    
    def showTipe(self):
        print(self.tipe)

class Hero(Team, Tipe_Hero):
    def __init__(self, name, health):
        self.name = name
        self.health = health

Ucup = Hero('Ucup', 100) # berperan sebagai class Hero
# karena sudah memperoleh inheritance dari class Team dan Tipe_hero maka bisa dibuat seperti ini.
Ucup.setTeam("merah") # berperan sebagai class Team
Ucup.setTipe("cundang") # berperans sebagai class Tipe_Hero
# sehingga bisa diketahui bahwa variable Ucup memili beda-beda bentuk yang merepresentasikan semua class di atas berdasarkan sub class Hero yang menginherit super class Team dan Tipe_Hero

Ucup.showTeam()
Ucup.showTipe()