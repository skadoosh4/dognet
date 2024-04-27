import os
from flask import Flask , render_template , request
from models.resnet import load_model
from prediction.predict import predict_image


app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = load_model()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict' , methods = ['POST'])
def predict():
    file = request.files['file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'] , file.filename)
    file.save(file_path)
    prediction = predict_image(image_path=file_path , model=model)
    return render_template('predict.html' , file_name = file.filename , prediction = prediction)


if __name__ == '__main__':
    app.run(debug=True)




