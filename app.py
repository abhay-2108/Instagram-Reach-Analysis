from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('instagram.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        followers = float(request.form['followers'])
        caption_length = float(request.form['caption_length'])
        hashtags_length = float(request.form['hashtags_length'])

        features = np.array([[followers, caption_length, hashtags_length]])
        prediction = model.predict(features)

        return render_template('index.html', prediction=round(float(prediction.item()), 2))

    except ValueError:
        return render_template('index.html', prediction="Invalid input values.")

if __name__ == "__main__":
    app.run(debug=True)
