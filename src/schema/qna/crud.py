from pydantic import BaseModel

from src.model import QNACategory


class QNABase(BaseModel):
    
    class Config:
        
        pass
        
        
class CreateQNA(QNABase):
    category: QNACategory
    title: str
    content: str
    company: str
    name: str
    phone: str
    email: str
    
    class Config:
        schema_extra = {
            'example': {
                'category': 'ESTIMATION',
                'title': '문의사항입니다.',
                'content': 'FastAPI를 잘하고 싶은데 도대체 어떻게 해야하죠?',
                'company': 'weekwith.me',
                'name': '홍길동',
                'phone': '010-1234-5678',
                'email': 'leedobby@weekwith.me'
            }
        }