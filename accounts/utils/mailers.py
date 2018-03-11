import datetime
import json

from accounts.constants import ACCOUNT_VERIFICATION_URL
from utilities.datetime_utils import get_epoch, get_current_time
from utilities.app_utils.crpyto_utils import lumos_encryption_service
from utilities.app_utils.mailer_utils import send_lumos_email


def send_lumos_user_verification_email(lumos_user_obj=None):
    """
    
    :param lumos_user_obj: 
    :return: 
    """
    verification_payload = {}

    now = get_current_time()
    now_plus_30 = now + datetime.timedelta(minutes=10)
    epoch = get_epoch(now_plus_30)

    verification_payload['id'] = lumos_user_obj.id.id
    verification_payload['expiry'] = epoch

    verification_payload_json = json.dumps(verification_payload)

    encrypted_verification_payload_json = lumos_encryption_service(data=verification_payload_json,
                                                                   encrypt_mode=True)

    verification_url = ACCOUNT_VERIFICATION_URL.format(encrypted_verification_payload_json)

    subject = "Please verify your account"

    user_name = lumos_user_obj.id.first_name.title() if lumos_user_obj.id.first_name else ""

    body = """
                Hi {0}!
    
                Kindly click on the url below to confirm your account:
                
                {1}
                
                
                -
                
                Team Lumos
            """.format(user_name, verification_url)


    print(epoch)
    print(body)
    print(subject)

    email_success = send_lumos_email(lumos_user=lumos_user_obj,
                     subject=subject,
                     content=body,
                     check_verified_email=False)

    return email_success


