from flask import Flask, request, escape
from flask_cors import CORS, cross_origin

app = Flask(__name__)


@app.route("/c2k", methods=['GET', 'POST'])
@cross_origin(origin="*")
def c2k():
    if request.method == 'GET':
        c = request.args.get('c')
    else:
        c = request.form.get('c')

    c = float(escape(c))
    return f'{c}C -> {c + 273.15:.6f}K'


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()