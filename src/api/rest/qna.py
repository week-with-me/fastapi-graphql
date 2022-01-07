import traceback

from email_validator import EmailNotValidError
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from src.crud import qna
from src.database import get_db
from src.schema import CreateQNA

router = APIRouter()


@router.post(
    path = '/',
    responses = {
        
    },       
    name = 'qna:create-qna'
)
async def create_qna(qna_data: CreateQNA, db: Session = Depends(get_db)):
    try:
        result = await qna.create(db=db, obj_in=qna_data)
        
        return JSONResponse(
            status_code = status.HTTP_201_CREATED,
            content     = {'data': [], 'message': 'success'}
        )
        
    except EmailNotValidError:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content     = {'detail': 'email invalid'}
        )
    
    except Exception as error:
        print(traceback.print_exc(error))
        return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content     = {'detail': error}
        )