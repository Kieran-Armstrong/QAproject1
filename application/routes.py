from flask.templating import render_template
from application import app, db
from application.models import Teams
from flask import redirect, url_for, request
from application.models import Teams, Players, TeamForm, PlayerForm



@app.route('/', methods=['GET', 'POST'])
def home1():
    return render_template('home.html',)
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html',)



@app.route('/create_team', methods=['GET', 'POST'])
def create_team():
    form = TeamForm()
    if form.validate_on_submit():
        new_team = Teams(teamName=form.teamName.data, stadium=form.stadium.data, city=form.city.data)
        db.session.add(new_team)
        db.session.commit()
        return redirect(url_for('create_team'))
    else:
        return render_template('addteam.html', form=form)

@app.route('/read_team')
def read_team():
    all_teams = Teams.query.all()
    return render_template('teamlist.html', all_teams=all_teams)

    
@app.route('/update_team/<int:id>',methods = ['GET','POST'])
def update_team(id):
    form = TeamForm()
    
    if request.method == 'POST':
        update_team = Teams.query.filter_by(id=id).first()
        if update_team: 
            update_team.teamName = request.form['teamName']
            update_team.stadium = request.form['stadium']
            update_team.city = request.form['city']
            db.session.commit()
            return redirect(url_for('read_team'))
        return f"Team with id = {id} Does not exist"
    else:
        return render_template('updateteam.html', form=form, id=id)
           
    
@app.route('/delete_team/<int:id>', methods=['GET', 'POST'])
def delete_team(id):
    team = Teams.query.filter_by(id=id).first()
    if team:
        db.session.delete(team)
        db.session.commit()
        return redirect(url_for('read_team'))
    else:
        return render_template('teamlist.html', id=id)
    


@app.route('/create_player', methods=['GET', 'POST'])
def create_player():
    form = PlayerForm()
    if form.validate_on_submit():
        new_player = Players(name=form.name.data, position=form.position.data, team_id=form.team_id.data)
        db.session.add(new_player)
        db.session.commit()
        return redirect(url_for('create_player'))
    else:
        return render_template('addplayer.html', form=form)

@app.route('/read_player')
def read_player():
    all_players = Players.query.all()
    return render_template('playerlist.html', all_players=all_players)

@app.route('/update_player/<int:id>',methods = ['GET','POST'])
def update_player(id):
    form = PlayerForm()
    
    if request.method == 'POST':
        update_player = Players.query.filter_by(id=id).first()
        if update_player: 
            update_player.name = request.form['name']
            update_player.position = request.form['position']
            update_player.team_id = request.form['team_id']
            db.session.commit()
            return redirect(url_for('read_player'))
    else:
        return render_template('addplayer.html', form=form, id=id)

@app.route('/delete_review/<int:id>', methods=['GET', 'POST'])
def delete_player(id):
    player = Players.query.filter_by(id=id).first()
    if player:
        db.session.delete(player)
        db.session.commit()
        return redirect(url_for('read_player'))
    else:
        return render_template('playerlist.html', id=id)

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
