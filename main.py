import os
import mw_email
from flask import Flask, render_template, request
from mw_email import FlaskEmail, JetEmail


# 20190113
var_emailtarget = 'jimmy.vo.2410@gmail.com'
var_emailuser = 'jimmy.vo.2410.gae@gmail.com'
var_password = 'dsadasdsadsadsadasdasd!@#$%^&dasdasdasdas'

app = Flask(__name__)
# email_app = MwEmail(app, var_emailuser, var_password)
email_app = JetEmail(api_key='34d299191b225ca4fe1670cd4cb251ba',
                     api_secret='b26bbefb2b727a49619e4019b3c3fdbe')


@app.route('/')
@app.route('/index.html')
@app.route('/index')
@app.route('/resume')
@app.route('/resume.html')
@app.route('/profile')
@app.route('/profile.html')
def profile():
    return render_template('profile.html')


@app.route('/contact', methods=['POST', 'GET'])
@app.route('/contact.html', methods=['POST', 'GET'])
def contact(script='', fullname='', address='', number='', email='', textarea=''):
    if request.method == 'POST':
        fullname = request.form['fullname']
        address = request.form['address']
        number = request.form['number']
        email = request.form['email']
        textarea = request.form['textarea']

        info = 'information:\n'
        info += ' - Full Name: ' + fullname + '\n'
        info += ' - Email: ' + email + '\n'
        info += ' - Address: ' + address + '\n'
        info += ' - Phone Number: ' + number + '\n'
        info += ' - Message: ' + textarea + '\n'

        # Try to send an email for verification
        if not email_app.send(recipients=email,
                              recipients_name=fullname,
                              sender=var_emailuser,
                              sender_name='Js bot',
                              subject='[jimmyvo2410.appspot.com] - Confirmation: ' + fullname,
                              body='Dear ' + fullname + ', \n\nWe have received your ' + info + '\n\nThis is an automated message do not reply.\n\nThanks,'):
            script = '$(document).ready(function() { ' \
                     'alert(\'There was a problem while validating your email. ' \
                     'Please make sure that your info is correct and try again. ' \
                     '});'

        elif not email_app.send(recipients=var_emailtarget,
                                recipients_name='Jimmy Vo',
                                sender=var_emailuser,
                                sender_name='Js bot',
                                subject='[jimmyvo2410.appspot.com] - ' + fullname,
                                body='Hello Jimmy,\n\nYou have a message from ' + fullname + ' with their ' + info):
            script = '$(document).ready(function() { ' \
                     'alert(\'There was an unexpected problem while sending message. ' \
                     'Please make sure that your info is correct and try again. ' \
                     '});'
        else:
            script = '$(document).ready(function() { alert(\'your message has been sent successfully !\');});'
            fullname = ''
            address = ''
            number = ''
            email = ''
            textarea = ''

    return render_template('_contact.html', script=script,
                                            fullname=fullname,
                                            address=address,
                                            number=number,
                                            email=email,
                                            textarea=textarea)


@app.route('/project')
@app.route('/project.html')
def project():
    return render_template('project.html')


@app.route('/_t_header')
@app.route('/_t_header.html')
def header():
    return render_template('_t_header.html')


@app.route('/_t_footer')
@app.route('/_t_footer.html')
def footer():
    return render_template('_t_footer.html')


@app.errorhandler(Exception)
def error_internal_server(e):
    return render_template("_error.html", errorCode=e)


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run()
else:
    print("is being imported into another module")
