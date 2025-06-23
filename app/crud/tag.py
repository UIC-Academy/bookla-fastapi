from sqlalchemy.orm import Session
from app.models.tag import Tag
from app.schemas.tag import TagCreate

def create_tag(db: Session, tag: TagCreate):
    db_tag = Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_all_tags(db: Session):
    return db.query(Tag).all()

def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()

def update_tag(db: Session, tag_id: int, tag: TagCreate):
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if db_tag:
        db_tag.name = tag.name
        db.commit()
        db.refresh(db_tag)
    return db_tag

def delete_tag(db: Session, tag_id: int):
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if db_tag:
        db.delete(db_tag)
        db.commit()
    return db_tag
