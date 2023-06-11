from jose import jwt, JWTError
from starlette import status
from typing import Optional, Annotated

from config.database import get_db
from sqlalchemy.orm import Session

from config.settings import settings
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from apps.accounts.schemas import CreateUserRequest
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db())]
oauth_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=[settings.ALGORITHM])
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth_bearer)]):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username = payload.get('sub')
        user_id = payload.get('id')
        role = payload.get('role')

        if username or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='could not validate user.')
        return {'username': username, 'id': user_id, 'role': role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='could not validate')


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    pass
