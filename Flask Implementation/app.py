import flask
from flask import request
from functions import *

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def predict():
   
    print(request.args)
    if(request.args):
        x_input, pred_class= make_prediction(request.args['chat_in'])
        print(x_input)
        return flask.render_template('predictor.html',
                                chat_in=x_input,
                                prediction_class=pred_class,
                                )
    
    else: 
        return flask.render_template('predictor.html',
                                     chat_in=" ",
                                     prediction_class=" ",
                                     )


if __name__=="__main__":
    app.run(debug=True)
    