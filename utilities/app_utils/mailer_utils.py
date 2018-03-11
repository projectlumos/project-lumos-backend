# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Mail, Content

from backend.settings.env_vars import SENDGRID_API_KEY
from utilities.constants import LUMOS_FROM_EMAIL_ID

# sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
# from_email = "abhishek.juneja145+from@gmail.com"
# to_email = "abhishek.juneja145+to@gmail.com"
# subject = "Sending with SendGrid is Fun"
# content = "APples are yum"
# mail = Mail(from_email, subject, to_email, content)
# response = sg.client.mail.send.post(request_body=mail.get())
# print(response.status_code)
# print(response.body)
# print(response.headers)


def sendgrid_client():
    """
    
    :return: 
    """
    sendgrid_client_obj = SendGridAPIClient(apikey=SENDGRID_API_KEY)
    return sendgrid_client_obj


def send_sendgrid_email(to_email, subject, content,
                        from_email=LUMOS_FROM_EMAIL_ID,
                        content_type="text/plain"):
    """
    
    :param to_email: 
    :param subject: 
    :param content: 
    :param from_email: 
    :param content_type: 
    :return: 
    """

    if not all([to_email, from_email, subject, content]):
        return False

    sendgrid_client_object = sendgrid_client()

    sendgrid_to_email = Email(to_email)
    sendgrid_from_email = Email(from_email)

    sendgrid_content = Content(content_type, content)

    mail = Mail(sendgrid_from_email, subject, sendgrid_to_email, sendgrid_content)
    response = sendgrid_client_object.client.mail.send.post(request_body=mail.get())

    if response.status_code != 202:
        return False
    else:
        return True


def send_lumos_email(lumos_user, subject, content, check_verified_email=True):
    """
    
    :param lumos_user: 
    :param subject: 
    :param content: 
    :param check_verified_email: 
    :return: 
    """

    # lumos_user_email = lumos_user.email

    # if check_verified_email and not lumos_user.is_verified:
    #     return False

    lumos_user_email = "abhishek.juneja145+TO-USER@gmail.com"

    email_status = send_sendgrid_email(to_email=lumos_user_email,
                                       subject=subject,
                                       content=content)

    return email_status
