from typing import TYPE_CHECKING,List
import fastapi as _fastapi
import schemas as _schemas

import sqlalchemy.orm as _orm
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()

@app.post("/api/contacts/", response_model=_schemas.Contact)
async def create_cotact(
    contact:_schemas.CreateContact,
    db:_orm.Session = _fastapi.Depends(_services.get_db)
):
    return await _services.create_contact(contact=contact, db=db)

@app.get("/api/contacts/", response_model=List[_schemas.Contact])
async def get_contacts(db:_orm.Session =_fastapi.Depends(_services.get_db)):
    return await _services.get_all_contacts(db=db)