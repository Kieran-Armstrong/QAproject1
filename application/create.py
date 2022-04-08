from app import db, Teams, Players

db.create_all() # Creates all table classes defined

arsenal = Teams(name = 'Arsenal') #Add example to countries table
db.session.add(arsenal)
db.session.commit()

# Here we reference the country that london belongs to useing 'country', this is what we named the backref variable in db.relationship()
ARamsdale = Players(name='Aaron Ramsdale', team = arsenal)
esr = Players(name='Emile Smith Rowe', team = Teams.query.filter_by(name='Arsenal').first())

db.session.add(ARamsdale)
db.session.add(esr)
db.session.commit()

print(f"Player: {arsenal.players[0].name}, {arsenal.players[1].name}")
print(f"Aaron Ramsdale plays for: {ARamsdale.team.name}")
print(f"ESR plays for: {esr.team.name}")