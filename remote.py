from flask import Flask

app = Flask(__name__)

@app.route('/run-python', methods=['GET'])
def run_script():
    # Your Python script logic here
    file1 = open("test.txt", "w")
    file1.write("Hello World")
    file1.close

    return "Hello World"

if __name__ == '__main__':
    # run_script()
    app.run(debug=True)