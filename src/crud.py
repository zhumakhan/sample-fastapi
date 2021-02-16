from sqlalchemy.orm import Session
import models, schemas

async def get_user(db: Session, user_id: int):
	return await db.query(models.User).filter(models.User.id == user_id).first()

async def get_user_by_email(db: Session, email: str):
	return await db.query(models.User).filter(models.User.email == email).first()

async def get_users(db: Session, skip: int = 0, limit: int = 100):
	return await db.query(models.User).offset(skip).limit(limit).order_by(models.User.id).all()

async def create_user(db: Session, user: schemas.UserCreate):
	db_user = models.User(email=user.email, password=user.password)
	await db.add(db_user)
	await db.commit()
	await db.refresh(db_user)
	return db_user

async def get_items(db: Session, skip: int = 0, limit: int = 100):
	return await db.query(models.Item).offset(skip).limit(limit).order_by(models.Item.id).all()

async def create_user_item(db: Session,item: schemas.ItemCreate,user_id: int):
	db_item = models.Item(**item.dict(),owner_id=user_id)
	await db.add(db_item)
	await db.commit()
	await db.refresh(db_item)
	return db_item
