from flask import Flask, render_template, url_for
from funPars import get_data_xls, get_data_xls2

app = Flask(__name__)


@app.route('/')
def index():
    data = get_data_xls()
    data2 = get_data_xls2()
    return render_template('index.html', data=data, date2=data2)


if __name__ == '__main__':
    app.run(debug=True)
