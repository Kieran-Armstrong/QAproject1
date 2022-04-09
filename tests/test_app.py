from flask import url_for
from flask_testing import TestCase
from application.models import Teams, Players, TeamForm, PlayerForm
from application import app, db

class  TestApp(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )
        return app
        

    def setUp(self):
        db.create_all()
        test_player1 = Players(name="test_name", position="test_position", team_id=1)
        test_team1 = Teams(teamName="test_teamName", stadium="test_stadium", city="test_city")
        db.session.add(test_team1)
        db.session.add(test_player1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestRead(TestApp):
    def test_read_team(self):
        response = self.client.get(url_for('read_team'))
        assert 'test_team'in response.data.decode()
        assert 'test_stadium'in response.data.decode()
        assert 'test_city'in response.data.decode()
        
class TestCreate(TestApp):
    def test_create_team(self):
        response = self.client.post(url_for('create_team'), data=dict(teamName="test_teamName", stadium="test_stadium", city="test_city"), follow_redirects=True)
        assert 'Enter Team Name'in response.data.decode()
        

class TestUpdate(TestApp):
    def test_update_team(self):
        response = self.client.post(url_for('update_team', id=1), data=dict(teamName="test_teamName", stadium="test_stadium", city="test_city"), follow_redirects=True)
        assert 'test_team'in response.data.decode()
        assert 'test_stadium'in response.data.decode()
        assert 'test_city'in response.data.decode()

class TestDelete(TestApp):
    def test_delete_player(self):
        response = self.client.get(
            url_for('delete_player', id=1),   
            follow_redirects=True   
        )
        response1 = self.client.get(
            url_for('delete_team', id=1),   
            follow_redirects=True   
        )
        assert "Players" in response.data.decode()
        assert "Teams" in response1.data.decode()

class TestCreatePlayer(TestApp):
    def test_create_player(self):
        response = self.client.post(url_for('create_player'), data=dict(name="test_name", position="test_position", team_id=1), follow_redirects=True)
        assert 'Enter Player'in response.data.decode()

class TestReadPlayer(TestApp):
    def test_read_player(self):
        response = self.client.get(url_for('read_player'))
        assert 'test_name'in response.data.decode()
        assert 'test_position'in response.data.decode()
        assert '1'in response.data.decode()

class TestUpdatePlayer(TestApp):
    def test_update_Player(self):
        response = self.client.post(url_for('update_player', id=1), data=dict(name="test_name", position="test_position", team_id=1), follow_redirects=True)
        assert 'test_name'in response.data.decode()
        assert 'test_position'in response.data.decode()
        assert '1'in response.data.decode()

class TestDeletePlayer(TestApp):
    def test_delete_player(self):
        response = self.client.get(
            url_for('delete_player', id=1),   
            follow_redirects=True   
        )
        response1 = self.client.get(
            url_for('delete_team', id=1),   
            follow_redirects=True   
        )
        assert "Players" in response.data.decode()
        assert "Teams" in response1.data.decode()
        




class TestViews(TestApp):

    def test_home_page(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_create_team(self):
        response = self.client.get(url_for('create_team'))
        self.assertEqual(response.status_code, 200)
      
    def test_update_team(self):
        response = self.client.get(url_for('update_team', id=1))
        self.assertEqual(response.status_code, 200)

    def test_create_player(self):
        response = self.client.get(url_for('create_player', id=1))
        self.assertEqual(response.status_code, 200)
        
    def test_read_player(self):
        response = self.client.get(url_for('read_player', id=1))
        self.assertEqual(response.status_code, 200)

    def test_update_player(self):
        response = self.client.get(url_for('update_player', id=1))
        self.assertEqual(response.status_code, 200)