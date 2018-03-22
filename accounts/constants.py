DJANGO_USERNAME_LIMIT = 150


ACCOUNT_VERIFICATION_URL = "http://127.0.0.1:8000/accounts/verify_user/?token={0}"

HOME_PAGE_URL = "http://127.0,0.1/?s={0}"


# mailer body

USER_VERIFICATION_EMAIL_BODY = """
                Hi {0}!
    
                Kindly click on the url below to confirm your account:
                
                {1}
                
                
                -
                
                Team Lumos
            """