from bottle import error
from bottle import static_file
import os
from bottle import get, post, request
from bottle import route, run, template


@route('/')
@route('/hello')
@route('/hello/<name>')
def hello(name="Stranger"):
    return template('Hello {{name}},How\'s today?', name=name)


USERList = {"quan": "123456"}


@route('/login')  # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


@post('/login')  # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


def check_login(username, password):
    if username in USERList and USERList[username] == password:
        return True
    else:
        return False


pic_dir = 'C:\\Users\\gusto\\code\\blog\\ablog\\bingpic'
pic_names = os.listdir(pic_dir)
pic_nums = len(pic_names)
pic_index = 0
@route('/bingpic')
def get_pic():
    global pic_index
    tem_index = pic_index
    pic_index += 1
    if pic_index >= pic_nums:
        pic_index = 0
    print(pic_names[tem_index])
    return static_file(
        pic_names[tem_index],
        root='C:\\Users\\gusto\\code\\blog\\ablog\\bingpic')


@route("/bingpic/<filename_or_index>")
def get_pic2(filename_or_index):
    try:
        return static_file(pic_names[int(filename_or_index)],
                           root='C:\\Users\\gusto\\code\\blog\\ablog\\bingpic')
    except ValueError:
        pass
    else:
        return static_file(
            filename_or_index,
            root='C:\\Users\\gusto\\code\\blog\\ablog\\bingpic')


@route("/download/image/<index:int>")
def download_image(index):
    return static_file(
        pic_names[index],
        root='C:\\Users\\gusto\\code\\blog\\ablog\\bingpic',
        download=True)


"""
return static_file(filename,root='C:\\Users\\gusto\\code\\blog\\ablog\\bingpic')
filename_or_index=None

"""
@route('/my_ip')
def show_ip():
    ip = request.environ.get('REMOTE_ADDR')
    # or ip = request.get('REMOTE_ADDR')
    # or ip = request['REMOTE_ADDR']
    return template("Your IP is: {{ip}}", ip=ip)


@error(404)
def error404(error):
    return "Nothing here,sorry!!"


@route("/fuck")
def fuck():
    return "Fuck Ya!"


run(host='localhost', port=8080, debug=True, reloader=True)
