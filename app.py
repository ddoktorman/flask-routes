from flask import Flask

my_app = Flask(__name__)


@my_app.route('/sorites')
def sorites():
    return "<h1> You are faced with a mound of sand. Remove one grain of sand from the mound, and it remains a mound. Remove two grains of sand from the mound, and it still remains a mound. How many grains of sand must one remove for the mound to no longer be a mound?<h1>"
@my_app.route('/meno')
def root2():
    return "<h1> You cannot search either for what you know or for what you do not know. One cannot search for what one knows--since he knows it, there is no need to search--nor for what one does not know, for he does not know what to look for. Thus, inquiry is either impossible or unnecessary.<h2>"
@my_app.route('/zeno')
def root3():
    return "<h1> To go anywhere, you must go halfway first, and then you must go half of the remaining distance, and half of the remaining distance, and so forth to infinity: thus, motion is impossible because it necessitates traversing an infinite number of spaces in a finite amount of time.<h1>"

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()