# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Mail, Content

from backend.settings.env_vars import SENDGRID_API_KEY
from utilities.constants import LUMOS_FROM_EMAIL_ID


def sendgrid_client():
    """
    Fetching a sendgrid client
        
    :return: Sendgrid client object 
    """
    sendgrid_client_obj = SendGridAPIClient(apikey=SENDGRID_API_KEY)
    return sendgrid_client_obj


def send_sendgrid_email(to_email, subject, content,
                        from_email=LUMOS_FROM_EMAIL_ID,
                        content_type="text/plain"):
    """
    Send an email using the sendgrid API
    
    
    :param to_email: to email
    :param subject: subject of the email
    :param content: content of the email body
    :param from_email: email sender
    :param content_type: "text/plain" or "text/html"
    :return: bool
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
    
    Single point for sending email from the Project. 
    
    Takes in a lumos_user object and checks if it has a verified email (by default)
    
    If we need to send verification independent emails (email sent to verify the email ID :p), 
    we bypass the verified email flag 
    
    :param lumos_user: LumosUser object
    :param subject: Subject of the email
    :param content: body of the email
    :param check_verified_email: flag to prevent sending emails to non verified accounts
    
    :return: bool
    """

    # lumos_user_email = lumos_user.email

    # if check_verified_email and not lumos_user.is_verified:
    #     return False

    lumos_user_email = "abhishek.juneja145+TO-USER@gmail.com"

    email_status = send_sendgrid_email(to_email=lumos_user_email,
                                       subject=subject,
                                       content=content)

    return email_status
