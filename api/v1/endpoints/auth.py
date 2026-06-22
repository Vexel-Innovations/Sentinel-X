from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sentinel_x.core.auth import create_access_token, verify_password, get_password_hash
from sentinel_x.db.mongodb import get_database

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Stateless login endpoint.
    """
    db = get_database()
    user = await db.users.find_one({"username": form_data.username})
    
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
async def register(username: str, password: str):
    db = get_database()
    hashed_password = get_password_hash(password)
    await db.users.insert_one({"username": username, "hashed_password": hashed_password})
    return {"message": "User created successfully"}
