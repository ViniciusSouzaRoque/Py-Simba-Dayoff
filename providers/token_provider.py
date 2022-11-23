from datetime import datetime, timedelta
from jose import jwt
from os import environ

SECRET_KEY = environ['SECRET_KEY']
ALGORITHM = 'HS256'
EXPIRES_IN_MINUTES = 3600


def create_access_token(self: dict):
    data = self.copy()
    expires = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MINUTES)

    data.update({'exp': expires})
    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verify_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    return payload.get('sub')
