from flask import Flask
app=Flask(__name__)
@app.route("/")
def Hello_world():
    return "<p>My name is Arpan and you</p>"
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)