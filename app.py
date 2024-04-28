import os
import secrets
from flask import Flask , render_template , request , session
from models.resnet import load_model
from prediction.predict import predict_image


app = Flask(__name__)

secret_key = secrets.token_hex(16)
app.secret_key = secret_key

model = load_model()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict' , methods = ['POST'])
def predict():
    file = request.files['file']
    session['file'] = file.read()
    prediction = predict_image(image_data=session['file'] , model=model)
    return render_template('predict.html' , file_name = file.filename , prediction = prediction)


if __name__ == '__main__':
    app.run(debug=True , host="0.0.0.0" , port=8080)




