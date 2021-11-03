import os
import sys

import src.util as util
from src.db import db
from src.context import webauthn
#from src.models import User # the name of the database

user_name = 'test'
user_display_name = 'Eusden'

challenge = util.generate_challenge(32)
ukey = util.generate_ukey()

print(len(challenge))
print(len(ukey))

challenge = challenge.rstrip('=')
make_credential_options = webauthn.WebAuthnMakeCredentialOptions(challenge, 'localhost', 'webauthn demo localhost',  ukey, user_name, user_display_name, 'https://localhost:5000')
print(make_credential_options, type(make_credential_options))
