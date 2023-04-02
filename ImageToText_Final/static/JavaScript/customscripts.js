function Trigger() {
    location.href="https://google.com";
}


function FetchVal(event) {
    var reader = new FileReader();
    reader.onload = function(){
      var output = document.getElementById('inputGroupFileAddon04');
      output.src = reader.result;
    }
    reader.readAsDataURL(event.target.files[0]);

}

function DisplayImage() {
    var img = document.createElement("image");
    document.body.appendChild(img);
}

// Function to render the reCAPTCHA widget
function renderRecaptcha() {
  grecaptcha.render('recaptcha-container', {
    'sitekey': '6Le9QiklAAAAAPOTW30MyL2u1IsNne2qSsg52yoP', // Replace with your site key
    'callback': onRecaptchaSuccess,
    'expired-callback': onRecaptchaExpired,
    'error-callback': onRecaptchaError,
  });
}

// Callback function when reCAPTCHA is solved
function onRecaptchaSuccess(response) {
  document.getElementById('submit-button').disabled = false;
}

// Callback function when reCAPTCHA expires
function onRecaptchaExpired() {
  document.getElementById('submit-button').disabled = true;
}

// Callback function when reCAPTCHA encounters an error
function onRecaptchaError() {
  document.getElementById('submit-button').disabled = true;
}

// Function to submit the form or perform the desired action
function onSubmit() {
  // Your code to submit the form or perform the desired action
}

// Function to check the user by providing them a captcha before converting the file
function checkUser() {
  console.log("EXECUTED ON CLICK");
}

// Event listener for the submit button
document.getElementById('submit-button').addEventListener('click', onSubmit);


// Event Listener for Submission of Data
document.getElementById('submitButton').addEventListener('click', checkUser)

// Render the reCAPTCHA widget when the page has loaded
window.addEventListener('load', renderRecaptcha);
