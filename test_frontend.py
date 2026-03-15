from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def handle(path):    
    return render_template(request.path)



if __name__ == '__main__':
    app.run(debug=True)