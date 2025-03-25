from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Web Interface</title>
    </head>
    <body>
        <h1>Welcome to the Local Web Interfaceeee</h1>
        <p>This is a simple web interface running locally.</p>
        <input type="text" placeholder="Enter text here">
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)