from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_recaptcha import ReCaptcha
import requests
import json

app = Flask(__name__)

app.config['RECAPTCHA_PUBLIC_KEY'] = '6Le9QiklAAAAAPOTW30MyL2u1IsNne2qSsg52yoP'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Le9QiklAAAAAGxJaKFkNIBlR9ArEJJ5jxET6lhR'
recaptcha = ReCaptcha(app)

API_KEY = "b02f653768e3426e80977533f2c8d229"
ENDPOINT = "https://imageprocessor1761.cognitiveservices.azure.com/"

OCR_URL = f"{ENDPOINT}vision/v3.2/ocr"



@app.route("/", methods=["GET", "POST"])
def index():
    pageIcon = './static/Images/Paper.svg'
    
    if request.method == "POST":
        if recaptcha.verify():
            message = 'Thanks for filling out the form well'
        else:
            message = 'Incorrect Job filling out the captcha'
        # Get the image from the form
        image = request.files["image"]

        # Prepare the request headers
        headers = {
            "Content-Type": "application/octet-stream",
            "Ocp-Apim-Subscription-Key": API_KEY,
        }

        #Check if the captcha was solved correctly
        
        # Send the request to Azure OCR
        response = requests.post(OCR_URL, headers=headers, data=image.read())

        # Parse the response JSON
        data = response.json()

        # Extract the text
        text = ""
        for region in data["regions"]:
            for line in region["lines"]:
                for word in line["words"]:
                    text += word["text"] + " "
                text += "\n"

        return render_template("result.html", text=text)

    return render_template('index.html', pageIcon=pageIcon)

if __name__ == "__main__":
    app.run(debug=True)