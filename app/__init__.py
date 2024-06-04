from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    root = os.getcwd()
    basepath = os.path.join(root, 'app', 'static', 'img', 'tiles')
    badpath_len = len(os.path.join(root, 'app'))
    print(basepath)
    dir = os.walk(basepath)
    file_list = []
    final_list = []

    for path, subdirs, files in dir:
        for file in files:
            temp = os.path.join(path, file)
            file_list.append(temp)
    for i in range(len(file_list)):
        if not ((file_list[i])[-6] + (file_list[i])[-5] == '_0'):
            continue
        else:
            file_list[i] = file_list[i][-(len(file_list[i])-badpath_len):]
            final_list.append(file_list[i])
    final_list.sort(reverse=False)
    return render_template('index.html', hists=final_list)


