from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db
from ..dependencies import get_current_user

router = APIRouter()

@router.post("/signup", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return crud.login_user(db, user.email, user.password)

@router.post("/addpost", response_model=schemas.Post)
def add_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return crud.create_post(db=db, post=post, user_id=current_user.id)

@router.get("/getposts", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return crud.get_posts_by_user(db, user_id=current_user.id)

@router.delete("/deletepost/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    crud.delete_post(db, post_id=post_id, user_id=current_user.id)
    return {"detail": "Post deleted"}
