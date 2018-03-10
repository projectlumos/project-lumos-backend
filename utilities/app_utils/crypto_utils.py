import base64

from backend.settings.base import get_env_variable
from backend.settings.env_vars import LUMOS_ENCRYPTION_SEED

ENVIRONMENT_ENCRYPTION_SEED = get_env_variable('LUMOS_ENCRYPTION_SEED', LUMOS_ENCRYPTION_SEED)


from cryptography.fernet import Fernet
"""
https://www.blog.pythonlibrary.org/2016/05/18/python-3-an-intro-to-encryption/

extremely easy implementation | super long string

a = lumos_encryption_util_fernet(message='22', encrypt_mode=True)
lumos_encryption_util_fernet(message=a, encrypt_mode=False)

"""
def lumos_encryption_util_fernet(message, encryption_key=ENVIRONMENT_ENCRYPTION_SEED, encrypt_mode=False):
    cipher_key = str.encode(encryption_key)
    cipher = Fernet(cipher_key)
    message = str.encode(message)

    if encrypt_mode:
        result_text = cipher.encrypt(message)
    else:
        result_text = cipher.decrypt(message)

    return result_text.decode('utf-8')


