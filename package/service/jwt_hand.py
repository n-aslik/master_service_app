from fastapi import HTTPException, status, Request, Depends
from jose import jwt
from datetime import datetime,timedelta
from os import getenv
from.config import Keys 
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from pydantic import BaseModel
from ..schemas import schema
import time


ACCESS_TOKEN_EXPIRATION = 360  * 24
REFRESH_TOKEN_EXPIRATION = 360 * 24 * 30
TOKEN_TYPES = {
    1:{"token_type": "access_token", "expiration": ACCESS_TOKEN_EXPIRATION},
    2:{"token_type": "refresh_token", "expiration": REFRESH_TOKEN_EXPIRATION}
}

secret = Keys()
# access_expire_token=30


class  JWTTokenBearer(HTTPBearer):
    def __init__(self, auto_error: bool = False):
        super(JWTTokenBearer, self).__init__(auto_error=auto_error)
    async def __call__(self, request:Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTTokenBearer, self).__call__(request)
        if credentials:
            if not self.verify_jwt(credentials.credentials, request):
                raise HTTPException(status_code=403, detail="Invalid token")
            return credentials.credentials
        else:
            return HTTPException(status_code=401, detail="Not authentificated")
            
    def verify_jwt(self, jwt_token: str, request: Request) -> bool:
        IsValidToken: bool = False
        try:
            payload = jwt.decode(jwt_token, secret.public_key)
            if time.time() < payload["expires"]:
                IsValidToken = True
            else:
                raise HTTPException(status_code=403, detail="JWT token is expired")
            
        except Exception as e :
            print(f"Token verification error{str(e)}")
            payload = None
        
        return IsValidToken
            
        
    


def generate_jwt_token (token_type:int, user_id:str, phone: str, role: str)->dict:
    token = TOKEN_TYPES.get(token_type)
    if not token:
        raise ValueError(f"Unknown token type {token_type}")
    payload = {
       "token_type" : token["token_type"],
        "user_id" : user_id,
        "phone" : phone,
        "role" : role,
        "expires" : time.time()+token["expiration"]
    }
    header = {"alg" : "RS256"}
    encoded_token=jwt.encode(payload, secret.private_key)
    return encoded_token

def access_token (credentials: str = Depends(JWTTokenBearer()))->dict:
    try:
        decoded_token = jwt.decode(credentials, secret.public_key)
        if decoded_token.get("token_type") != "access":
            raise HTTPException(status_code=403, detail="Invalid token type: must be access token")
        if time.time() > decoded_token["expires"]:
            raise HTTPException(status_code=401, detail="Token expired")
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=403, detail="JWT payload error: {}".format(e))


def refresh_token (credentials: str = Depends(JWTTokenBearer()))->dict:
    try:
        decoded_token = jwt.decode(credentials, secret.public_key)
        if decoded_token.get("token_type") != "refresh":
            raise HTTPException(status_code=403, detail="Invalid token type: must be refresh token")
        if time.time() > decoded_token["expires"]:
            raise HTTPException(status_code=401, detail="Token expired")
        return decoded_token
    except Exception as e:
        raise HTTPException(status_code=403, detail="JWT payload error {}".format(e))


def parse_token (token:str)->dict:
    try:
        decoded_token=jwt.decode(token,secret.private_key)
        return decoded_token
    except :
        raise HTTPException(status_code=403, detail="JWT decode error")



