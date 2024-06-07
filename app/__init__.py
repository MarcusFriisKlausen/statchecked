from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import flask_sqlalchemy as sa
from sqlalchemy import text

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = sa.SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(os.getcwd(), 'instance', 'project.db')}"
db.init_app(app)

def get_winrate(champ:str):
    with app.app_context():
        count = db.session.execute(text('''SELECT * FROM Champions WHERE champion = "''' + champ + '''"'''))
        wins = db.session.execute(text('''SELECT * FROM Champions WHERE champion = "''' + champ + '''" AND win = "True"'''))
        count_wins = (len(wins.all()))
        count_count = (len(count.all()))
        # print("Count", count_count)
        # print("Wins", count_wins)
        if count_count > 0: 
            wr = round((100 * count_wins / count_count), 2)
        else:
            print(champ)
            wr = 0
        # print("Winrate:", wr)
        return wr

def get_games_played(champ:str):
    with app.app_context():
        games = db.session.execute(text('''SELECT * FROM Champions WHERE champion = "''' + champ + '''"'''))
        count_games = (len(games.all()))
        return count_games
    
def get_pickrate(champ:str):
    with app.app_context():
        all_games = db.session.execute(text('''SELECT * FROM Champions'''))
        count_champ_games = get_games_played(champ)
        count_all_games = (len(all_games.all()))
        pr = round((100 * count_champ_games / count_all_games), 2)
        return pr


@app.route("/")
def index():
    root = os.getcwd()
    basepath_tiles = os.path.join(root, 'static', 'img', 'tiles')
    basepath_splash = os.path.join(root, 'static', 'img', 'splash')
    basepath_loading = os.path.join(root, 'static', 'img', 'loading')
    badpath_len = len(os.path.join(root))
    dir_tiles = os.walk(basepath_tiles)
    dir_splash = os.walk(basepath_splash)
    dir_loading = os.walk(basepath_loading)
    file_list_splash = []
    final_list_splash = []
    file_list_loading = []
    final_list_loading = []
    file_list_tiles = []
    final_list_tiles = []

    for path, subdirs, files in dir_tiles:
        for file in files:
            temp = os.path.join(path, file)
            file_list_tiles.append(temp)
    for i in range(len(file_list_tiles)):
        if not ((file_list_tiles[i])[-6] + (file_list_tiles[i])[-5] == '_0'):
            continue
        else:
            file_list_tiles[i] = file_list_tiles[i][-(len(file_list_tiles[i])-badpath_len):]
            final_list_tiles.append(file_list_tiles[i])
    final_list_tiles.sort(reverse=False)

    for path, subdirs, files in dir_splash:
        for file in files:
            temp = os.path.join(path, file)
            file_list_splash.append(temp)
    for i in range(len(file_list_splash)):
        if not ((file_list_splash[i])[-6] + (file_list_splash[i])[-5] == '_0'):
            continue
        else:
            file_list_splash[i] = file_list_splash[i][-(len(file_list_splash[i])-badpath_len):]
            final_list_splash.append(file_list_splash[i])
    final_list_splash.sort(reverse=False)

    for path, subdirs, files in dir_loading:
        for file in files:
            temp = os.path.join(path, file)
            file_list_loading.append(temp)
    for i in range(len(file_list_loading)):
        if not ((file_list_loading[i])[-6] + (file_list_loading[i])[-5] == '_0'):
            continue
        else:
            file_list_loading[i] = file_list_loading[i][-(len(file_list_loading[i])-badpath_len):]
            final_list_loading.append(file_list_loading[i])
    final_list_loading.sort(reverse=False)

    tuple_list = []

    for i in range(len(final_list_loading)):
        champ_name = (final_list_tiles[i][len(basepath_tiles)-badpath_len+1:])[:-6]
        wr = get_winrate(champ_name)
        games_picked = get_games_played(champ_name)
        pr = get_pickrate(champ_name)
        tuple_list.append((final_list_tiles[i], final_list_splash[i], final_list_loading[i], wr, champ_name, pr, games_picked))
    return render_template('index.html', pics=tuple_list)

@app.route("/champ_page")
def champ_page():
    return render_template('champ_page.html')

root = os.getcwd()
basepath = os.path.join(root, 'static', 'data', "Champions.csv")
data = pd.read_csv(basepath)
champions = data['champion'].tolist()

@app.route('/search_champion')
def search_champion():
    query = request.args.get('q')
    if query:
        query = query.title()  # Capitalize the first letter of each word
        if query in champions:
            return redirect(url_for('champ_page') + '?loading=/static/img/loading/' + query + '_0.jpg&splash=/static/img/splash/' + query + '_0.jpg&win=' + str(get_winrate(query)) + '&pickr=' + str(get_pickrate(query)) + '&games=' + str(get_games_played(query)))
    # If the champion is not found, you can redirect to an error page or back to the index
    return redirect(url_for('index'))