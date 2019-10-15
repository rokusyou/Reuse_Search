from flask import Flask ,render_template, request

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def hello_world():
    search_words='Medarot'
    search_words=request.args.get('search_words')
    return render_template('reuse_search.html',search_words=search_words)


@app.route('/index',methods=['post'])
def post():
    search_words = request.form['search_words']
    return render_template('reuse_search.html', search_words=search_words)



if __name__ == '__main__':
    app.run()