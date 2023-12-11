from fastapi import Depends, File,APIRouter,UploadFile
from fastapi.responses import FileResponse
from auth.oauth2 import get_curr_user
import shutil
from schemas import UserBase

router = APIRouter(tags=['Files'])


@router.post('/file')
def get_file(file : bytes = File(...), current_user : UserBase = Depends(get_curr_user)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return {'File lines' : lines}

@router.post('/uploadfile')
def get_file(file : UploadFile = File(...), current_user : UserBase = Depends(get_curr_user)):
    #files/mahmoud.{file.content_type.split('/')[1]}
    path = f'files/{file.filename}'
    with open(path,'w+b') as buffer:
        shutil.copyfileobj(file.file,buffer)
    return {'file path' : path,
            'file type': file.content_type}

@router.get('/donloadfile/{name}',response_class=FileResponse)
def get_file(name : str, current_user : UserBase = Depends(get_curr_user)):
    #files/mahmoud.{file.content_type.split('/')[1]}
    path = f'files/{name}'
    return path
            