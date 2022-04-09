from sqlalchemy import Integer
from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(30), nullable=False)
    stadium = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    players = db.relationship('Players', backref='team')

class TeamForm(FlaskForm):
    teamName = StringField('Enter the team name')
    stadium = StringField('Enter the stadium')
    city = StringField('Enter the city')
    submit = SubmitField('submit')

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(20), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)


class PlayerForm(FlaskForm):
    name = StringField('Enter player name')
    position = StringField('Enter player position')
    team_id = IntegerField('Enter the team id')
    submit = SubmitField('submit')