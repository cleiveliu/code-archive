from bottle import Bottle, run, static_file
import os

html_file_path = r"C:\Users\gusto\Desktop\here"


app = Bottle()


@app.route('/')
@app.route('/hello')
def hello():
    return "hehe!!"


@app.route("/article/:id_")
def get_article(id_):
    dirs = os.listdir(html_file_path)
    id_ = int(id_)
    if id_ < len(dirs):
        return static_file(dirs[id_], root=r"C:\Users\gusto\Desktop\here")
    else:
        return f"no article {id_}"


run(app, host='localhost', port=7777)
