from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import  crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
	db = SessionLocal
	try:
		yield db
	finally:
		db.close()

@app.post('/users/',response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
	db_user = await crud.get_user_by_email(db=db, emial=user.email)
	if db_user:
		raise HTTPException(status_code=400,detail='Given email exists')

	return await crud.create_user(db=db,user=user)

@app.get('/users/',response_model=List[schemas.User])
async def read_users(skip:int = 0,limit: int = 100, db: Session=Depends(get_db)):
	users = await crud.get_users(db=db,skip=skip,limit=limit)
	return users

@app.get('/users/{user_id}',response_model=schemas.User)
async def read_user(user_id: int, db: Session=Depends(get_db)):
	db_user = await curd.get_user(db=db, user_id=user_id)
	if not db_user:
		raise HTTPException(status_code=400,detail='user with id: {} does not exist!'.format(user_id))
	return db_user

@app.post('/users/{user_id}/items/', response_model=schemas.Item)
async def create_item_for_user(user_id:int,item:schemas.ItemCreate,db:Session=Depends(get_db)):
	return await crud.create_user_item(db=db, item=item, user_id=user_id)

@app.get('/items/',response_model=List[schemas.Item])
async def read_tems(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
	items = await crud.get_items(db=db,skip=skip,limit=limit)
	return items

