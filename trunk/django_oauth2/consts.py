#-*- coding: utf-8 -*-

RESPONSE_TYPE_TOKEN = 'token'
RESPONSE_TYPE_CODE = 'code'
RESPONSE_TYPE_CODE_AND_TOKEN = 'code_and_token'

RESPONSE_TYPES = [
    RESPONSE_TYPE_TOKEN,
    RESPONSE_TYPE_CODE,
    RESPONSE_TYPE_CODE_AND_TOKEN,
    ]

RESPONSE_TYPE_CHOICES = [ (response_type, response_type) for response_type in RESPONSE_TYPES ]

RESPONSE_TYPE_BITS = {
    RESPONSE_TYPE_TOKEN: 1,
    RESPONSE_TYPE_CODE: 2,
    RESPONSE_TYPE_CODE_AND_TOKEN: 4,           
    }

AUTHORIZED_RESPONSE_TYPE_CHOICES = []
for a in [ RESPONSE_TYPE_TOKEN, None, ]:
    for b in [ RESPONSE_TYPE_CODE, None, ]:
        for c in [ RESPONSE_TYPE_CODE_AND_TOKEN, None, ]:
            AUTHORIZED_RESPONSE_TYPE_CHOICES.append(
                (
                RESPONSE_TYPE_BITS.get(a, 0) | RESPONSE_TYPE_BITS.get(b, 0) | RESPONSE_TYPE_BITS.get(c, 0),
                ' | '.join([ s for s in [a, b, c, ] if s ]) or '-'
                )
            )

ACCESS_GRANT_TYPE_AUTHORIZATION_CODE = 'authorization_code'
ACCESS_GRANT_TYPE_PASSWORD = 'password'
ACCESS_GRANT_TYPE_ASSERTION = 'assertion'
ACCESS_GRANT_TYPE_REFRESH_TOKEN = 'refresh_token'
ACCESS_GRANT_TYPE_NONE = 'none'

ACCESS_GRANT_TYPES = [
    ACCESS_GRANT_TYPE_AUTHORIZATION_CODE,
    ACCESS_GRANT_TYPE_PASSWORD,
    ACCESS_GRANT_TYPE_ASSERTION,
    ACCESS_GRANT_TYPE_REFRESH_TOKEN,
    ACCESS_GRANT_TYPE_NONE,
    ]

ACCESS_GRANT_TYPE_CHOICES = [ (grant_type, grant_type) for grant_type in ACCESS_GRANT_TYPES ]


ACCESS_GRANT_TYPE_BITS = {
    ACCESS_GRANT_TYPE_AUTHORIZATION_CODE: 1,
    ACCESS_GRANT_TYPE_PASSWORD: 2,
    ACCESS_GRANT_TYPE_ASSERTION: 4,
    ACCESS_GRANT_TYPE_REFRESH_TOKEN: 8,
    ACCESS_GRANT_TYPE_NONE: 16,           
    }

CLIENT_KEY_LENGTH = 10
CLIENT_SECRET_LENGTH = 10

AUTHORIZATION_REQUEST_KEY_LENGTH = 10

CODE_KEY_LENGTH = 10

ACCESS_TOKEN_LENGTH = 10
REFRESH_TOKEN_LENGTH = 10

AUTHENTICATION_BACKEND_CORE = 'django_oauth2.authentication.core.Backend'