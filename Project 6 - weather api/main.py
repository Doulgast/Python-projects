

import pandas
from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/api/v1/<station>/<date>")
def about(station,date):
    df=pandas.read_csv("")
    temperature = df.station(date)
    return {"station:":station,
            "date: ": date,
            "temperature:":temperature}
app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)