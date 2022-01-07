from email_validator import validate_email
from sqlalchemy.orm import Session

from src.model import QNA
from src.schema import CreateQNA


class CRUDQNA:
    def __init__(self, model: QNA) -> None:
        self.model = model
        
    async def create(self, db: Session, obj_in: CreateQNA):
        try: 
            validate_email(obj_in.email)
            
            instance = self.model(**obj_in.dict())
            db.add(instance)
            db.commit()
            
            return await db.flush()        
                            
        finally:
            db.close()
            
            
qna = CRUDQNA(model=QNA)