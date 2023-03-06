"""API"""
from fastapi import FastAPI
from lagerdb.manager import DBManager
from lagerdb.main import session
from lagerdb.models.models import Layout
app = FastAPI()
db_manager = DBManager(used_session=session)

@app.get("/dbApi/v1/get/layout/all/")
async def get_all_layout():
    """
    Route for getting all layouts from db
    """
    layouts = db_manager.show_all_layout()
    return {"response":layouts}

@app.get("/dbApi/v1/get/offer/all/")
async def get_all_offer():
    """
    Route for getting all offers from db
    """
    offers = db_manager.show_all_offer()
    return {"response":offers}

@app.post("/dbApi/v1/post/layout/new")
async def post_new_layout(pdf_text:str):
    """
    Route for creating a new layout
    """
    layout = Layout(pdf_text=pdf_text)
    db_manager.write_layout(layout)
    return {"response":1}
