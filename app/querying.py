import flask_sqlalchemy as sa
from flask import Flask
from sqlalchemy import text


def get_winrate(app, champ:str):
    with app.app_context():
        count = db.session.execute(text('''SELECT * FROM Champions WHERE champion = "''' + champ + '''"'''))
        wins = db.session.execute(text('''SELECT * FROM Champions WHERE champion = "''' + champ + '''" AND win = "True"'''))
        count_wins = (len(wins.all()))
        count_count = (len(count.all()))
        print("Count", count_count)
        print("Wins", count_wins)
        wr = round((100 * count_wins / count_count), 2)
        print("Winrate:", wr)
        return wr
    
#get_winrate("Aatrox")