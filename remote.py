from flask import Flask

app = Flask(__name__)

@app.route('/run-python', methods=['GET'])
def run_script():
    # Your Python script logic here
    print("Hello World")
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)