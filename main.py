import os

import werkzeug
from flask import Flask, render_template, request, redirect, url_for, session, abort

app = Flask(__name__)
<<<<<<< HEAD
# email_app = MwEmail(app, var_emailuser, var_password)
email_app = JetEmail(api_key='34d299191b225ca4fe1670cd4cb251ba',
                     api_secret='b26bbefb2b727a49619e4019b3c3fdbe',
                     email_host=var_emailtarget)
=======
>>>>>>> parent of caf7af0... 20190114


@app.route('/')
@app.route('/index.html')
@app.route('/resume.html')
@app.route('/profile.html')
def profile():
    return render_template('profile.html')


<<<<<<< HEAD
global email_list


@app.route('/contact', methods=['POST', 'GET'])
@app.route('/contact.html', methods=['POST', 'GET'])
def contact(notification='', fullname='', address='', number='', email='', message=''):
    if request.method == 'POST':
        fullname = request.form['fullname']
        number = request.form['number']
        email = request.form['email']
        message = request.form['message']

        info = 'information:\n'
        info += ' - Full Name: ' + fullname + '\n'
        info += ' - Email: ' + email + '\n'
        info += ' - Phone Number: ' + number + '\n'
        info += ' - Message: ' + message + '\n'

        sent_count = email_app.count_sent(email)
        trial_count = email_app.count_trial(email)

        email_app.mark_email_trial(email)

        if sent_count > 0:
            notification = "<p class=\'failure\'>" \
                           "Your message was sent! If you insist, please come back tomorrow to send another one." \
                           "</p>"
        elif trial_count > 3:
            notification = "<p class=\'failure\'>" \
                           "You have tried " + str(trial_count) + " times but it didn't work out. " \
                           "Please send me an email to " + \
                           var_emailtarget + "." \
                           "</p>"
        # Try to send an email for verification
        elif not email_app.send(recipients=email,
                              recipients_name=fullname,
                              sender=var_emailuser,
                              sender_name='Js bot',
                              subject='[jimmyvo2410.appspot.com] - Confirmation: ' + fullname,
                              body='Dear ' + fullname + ', \n\nWe have received your ' + info +
                                   '\n\nThis is an automated message do not reply.\n\nThanks,'):
            notification = "<p class=\'failure\'>" \
                           "There was a problem while validating your email. " \
                           "Please make sure that your info is correct." \
                           "</p>"
        elif not email_app.send(recipients=var_emailtarget,
                                recipients_name='Jimmy Vo',
                                sender=var_emailuser,
                                sender_name='Js bot',
                                subject='[jimmyvo2410.appspot.com] - ' + fullname,
                                body='Hello Jimmy,\n\nYou have a message from ' + fullname + ' with their ' + info):
            notification = "<p class=\'failure\'>" \
                           "There was an unexpected problem while sending message. Please send me an email to " + \
                           var_emailtarget + "." \
                           "</p>"
        else:
            notification = "<p class=\'succeed\'>Your message has been sent successfully !</p>"
            email_app.mark_email_sent(email)
            fullname = ''
            address = ''
            number = ''
            email = ''
            message = ''

    return render_template('_contact.html', notification=notification,
                                            fullname=fullname,
                                            address=address,
                                            number=number,
                                            email=email,
                                            message=message)


@app.route('/project')
=======
@app.route('/contact.html')
def contact():
    return render_template('contact.html')


>>>>>>> parent of caf7af0... 20190114
@app.route('/project.html')
def project():
    return render_template('project.html')


<<<<<<< HEAD
@app.route('/header')
@app.route('/header.html')
=======
@app.route('/_t_header.html')
>>>>>>> parent of caf7af0... 20190114
def header():
    return render_template('header.html')


<<<<<<< HEAD
@app.route('/footer')
@app.route('/footer.html')
=======
@app.route('/_t_footer.html')
>>>>>>> parent of caf7af0... 20190114
def footer():
    return render_template('footer.html')


@app.errorhandler(Exception)
def error_internal_server(e):
    return render_template("_error.html", errorCode=e)
<<<<<<< HEAD
=======


@app.route('/e404')
def e404():
    abort(404)


@app.route('/e500')
def e500():
    abort(500)
>>>>>>> parent of caf7af0... 20190114


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run()
else:
    print("is being imported into another module")
