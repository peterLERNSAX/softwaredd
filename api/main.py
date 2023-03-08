"""API"""
from fastapi import FastAPI, HTTPException
from lagerdb.manager import DBManager
from lagerdb.main import session
from lagerdb.models.models import Layout, OfferFile
from pydantic import BaseModel

app = FastAPI()
db_manager = DBManager(used_session=session)

class Permission(BaseModel):
    """Class for permission"""
    usermanagement:bool
    layout:bool
    database:bool
    offer:bool
    offer_file:bool

def check_permission(perm_obj:Permission,perm:int)->bool:
    """
    Checks for permission
    """
    if perm == 1:
        return perm_obj.usermanagement
    if perm == 2:
        return perm_obj.layout
    if perm == 3:
        return perm_obj.database
    if perm == 4:
        return perm_obj.offer
    if perm == 5:
        return perm_obj.offer_file
    return False

def return_403():
    """
    build return dict
    """
    raise HTTPException(status_code=403,detail="Permission denied")

@app.post("/dbApi/v1/post/customer/all/")
async def get_all_customers(perms:Permission):
    """
    Route for getting all customers from db
    """
    if not check_permission(perms,4):
        return return403()
    customers = 

@app.post("/dbApi/v1/post/layout/all/")
async def get_all_layout(perms:Permission):
    """
    Route for getting all layouts from db
    """
    if not check_permission(perms,2):
        return return_403()
    layouts = db_manager.show_all_layout()
    return {"response":layouts}

@app.post("/dbApi/v1/post/offer/file/all/")
async def get_all_offer_file(perms:Permission):
    """
    Route for getting all offers from db
    """
    if not check_permission(perms,5):
        return return_403()
    offers = db_manager.show_all_offer_file()
    return {"response":offers}

@app.post("/dbApi/v1/post/layout/new/")
async def post_new_layout(pdf_text:str,perms:Permission):
    """
    Route for creating a new layout
    """
    if not check_permission(perms,2):
        return return_403()
    layout = Layout(pdf_text=pdf_text)
    db_manager.write_layout(layout)
    return {"response":1}

@app.post("/dbApi/v1/post/offer/file/new/")
async def post_new_offer_file(pdf_text:str,perms:Permission):
    """
    Route for creating new offer file
    """
    if not check_permission(perms,5):
        return return_403()
    offer = OfferFile(pdf_text=pdf_text)
    db_manager.write_offer_file(offer)
    return {"response":1}

@app.delete("/dbApi/v1/delete/layout/new/")
async def delete_layout(layout_id:int,perms:Permission):
    """
    Route for deleting layout
    """
    if not check_permission(perms,2):
        return return_403()
    db_manager.remove_layout(layout_id=layout_id)
    return {"response":1}

@app.delete("/dbApi/v1/delete/offer/file/new/")
async def delete_offer_file(offer_id:int,perms:Permission):
    """
    Route for deleting offer
    """
    if not check_permission(perms,5):
        return return_403()
    db_manager.remove_offer_file(offer_id=offer_id)
    return {"response":1}