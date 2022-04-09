from application import db
from application.models import Players, Teams

db.drop_all()
db.create_all()

teamT1 = Teams(teamName = "Arsenal" , stadium= "Emirates Stadium", city = "N London")
db.session.add(teamT1)
db.session.commit()
playerT1 = Players(name = "Aaron Ramsdale", position = "GK", team_id = teamT1.id)
db.session.add(playerT1)
db.session.commit()

