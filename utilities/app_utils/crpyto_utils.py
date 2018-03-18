import base64
from simplecrypt import encrypt, decrypt

from backend.settings.env_vars import SECRET_KEY


def lumos_encryption_service(data, encrpytion_key=SECRET_KEY, url_encode=True, encrypt_mode=True):
    """
    Encrpytion service function which takes in a str and encrpytion/decrpytion flag and return a st
    
    :param data: plaintext/ciphertext str 
    :param encrpytion_key: key used for encrpytion services
    :return: str
    """

    if encrypt_mode:
        service_data = encrypt(encrpytion_key, data)

        if url_encode:
            service_data = base64.urlsafe_b64encode(service_data)

        service_data = service_data

    else:
        if url_encode:
            data = base64.urlsafe_b64decode(data)

        service_data = decrypt(encrpytion_key, data)

    service_data = str(service_data, 'utf-8')
    return service_data
