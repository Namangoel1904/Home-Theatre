from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/bolly')
def bolly():
    return render_template('bolly.html')

@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=False, port=8000)