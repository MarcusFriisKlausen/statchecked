from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    root = os.getcwd()
    basepath_tiles = os.path.join(root, 'app', 'static', 'img', 'tiles')
    basepath_splash = os.path.join(root, 'app', 'static', 'img', 'splash')
    basepath_loading = os.path.join(root, 'app', 'static', 'img', 'loading')
    badpath_len = len(os.path.join(root, 'app'))
    print(basepath_tiles)
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
        tuple_list.append((final_list_tiles[i], final_list_splash[i], final_list_loading[i]))

    return render_template('index.html', pics=tuple_list)

@app.route("/champ_page")
def champ_page():
    return render_template('champ_page.html')