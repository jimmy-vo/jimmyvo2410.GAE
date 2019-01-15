import mailjet_rest
import requests_toolbelt.adapters.appengine
from flask_mail import Mail, Message


class JetEmail:
    def __init__(self, api_key, api_secret):
        requests_toolbelt.adapters.appengine.monkeypatch()
        self.client = mailjet_rest.Client(
            auth=(api_key, api_secret), version='v3.1')

    def send(self, recipients='', recipients_name='unknown', sender='',sender_name='unknown', subject='', body=''):
        try:
            data = {
                'Messages': [{
                    "From": {
                        "Email": sender,
                        "Name": sender_name
                    },
                    "To": [{
                            "Email": recipients,
                            "Name": recipients_name
                    }],
                    "Subject": subject,
                    "TextPart": body
                }]
            }
            result = self.client.send.create(data=data).status_code
            if result == 200:
                return True
            else:
                return False
        except:
            return False


class FlaskEmail:
    def __init__(self, app, username, password):
        app.config.update(
                            DEBUG=True,
                            MAIL_SERVER='smtp.gmail.com',
                            MAIL_PORT=465,
                            MAIL_USE_TLS=False,
                            MAIL_USE_SSL=True,
                            MAIL_USERNAME = username,
                            MAIL_PASSWORD = password)
        self.mail = Mail(app)

    def send(self, recipients='', reply_to='', sender='', subject='', body=''):
        try:
            self.mail.send(Message(recipients=recipients.split(),
                              sender=sender,
                              subject=subject,
                              body=body))
            return True
        except:
            return False