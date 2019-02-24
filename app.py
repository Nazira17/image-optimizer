import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from tempmail import TempMail

# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)


def allowed_file(file):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_img_from_api(file):
    if request.method == 'GET':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            else:
                uploaded_file = request.files['file']
                # if uploaded_file:
                # return '.' in filename and \
                # filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def send_img_to_api():
    pass


def get_mail():
    tm = TempMail()
    email = tm.get_email_address()  # v5gwnrnk7f@gnail.pw  создаем почту
    key = tm.get_mailbox(email)  # list of emails получаем письма из почты


def post_tinyjpg(file):
    tinify.key = "YOUR_API_KEY"
    source = tinify.from_file(uploaded_file)
    source.to_file(uploaded_file)
    compressions_this_month = tinify.compression_count
    pass


def get_tinyjpg(file):
    pass


def patch_db():
    pass


@app.route('/', methods=['GET', 'POST'])
    img = get_img_from_api()
    mail = get_mail()
    tinyjpg = post_tinyjpg()
    key = patch_db()
    send_img = send_img_to_api()









# def compress_image(file):
#     """Compress image size via API"""

#     # keep track how many times API have been used
#     if tinify.key == "ZPF88NBkpcTy9m2Bsz1qRq4ZRMf4H9WP":
#         db.execute("UPDATE api_count SET count1 = count1 + 1")
#     else:
#         db.execute("UPDATE api_count SET count2 = count2 + 1")

#     counter = db.execute("SELECT * FROM api_count")[0]

#     # don't compress image if API request limit is reached
#     if counter["count1"] == 495 or counter["count2"] == 495:
#         return "Limit reached"











    if __name__ == '__main__':
        app.run(debug=True)
