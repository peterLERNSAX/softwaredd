"""API"""
from typing import Any, Optional

from fastapi import FastAPI, HTTPException
from lagerdb.main import session
from lagerdb.manager import DBManager
from lagerdb.models.models import Customer, Hardware, Layout, Offer, OfferFile
from sqlalchemy import ForeignKey

# pylint:disable=no-name-in-module
from pydantic import BaseModel

app = FastAPI()
db_manager = DBManager(used_session=session)


# pylint:disable=too-few-public-methods
class Permission(BaseModel):
    """Class for permission"""

    usermanagement: bool
    layout: bool
    database: bool
    offer: bool
    offer_file: bool


def check_permission(perm_obj: Permission, perm: int) -> bool:
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


def return_403() -> Any:
    """
    build return dict
    """
    raise HTTPException(status_code=403, detail="Permission denied")


@app.post("/dbApi/v1/post/customer/all/")
async def get_all_customers(perms: Permission) -> Any:
    """
    Route for getting all customers from db
    """
    if not check_permission(perms, 3):
        return return_403()
    customers = db_manager.show_all_customers()
    return {"response": customers}


@app.post("/dbApi/v1/post/offer/all/")
async def get_all_offer(perms: Permission) -> Any:
    """
    Route for getting all offers from db
    """
    if not check_permission(perms, 4):
        return return_403()
    if not check_permission(perms, 3):
        return return_403()
    offers = db_manager.show_all_offer()
    return {"response": offers}


@app.post("/dbApi/v1/post/hardware/all/")
async def get_all_hardware(perms: Permission) -> Any:
    """
    Route for getting all hardware from db
    """
    if not check_permission(perms, 4):
        return return_403()
    hardware = db_manager.show_all_hardware()
    return {"response": hardware}


@app.post("/dbApi/v1/post/layout/all/")
async def get_all_layout(perms: Permission) -> Any:
    """
    Route for getting all layouts from db
    """
    if not check_permission(perms, 2):
        return return_403()
    if not check_permission(perms,3):
        return return_403()
    layouts = db_manager.show_all_layout()
    return {"response": layouts}


@app.post("/dbApi/v1/post/offer/file/all/")
async def get_all_offer_file(perms: Permission) -> Any:
    """
    Route for getting all offers from db
    """
    if not check_permission(perms, 5):
        return return_403()
    if not check_permission(perms,3):
        return return_403()
    offers = db_manager.show_all_offer_file()
    return {"response": offers}


@app.post("/dbApi/v1/post/layout/new/")
async def post_new_layout(pdf_text: str, perms: Permission) -> Any:
    """
    Route for creating a new layout
    """
    if not check_permission(perms, 2):
        return return_403()
    if not check_permission(perms,3):
        return return_403()
    layout = Layout(pdf_text=pdf_text)
    db_manager.write_layout(layout)
    return {"response": 1}


@app.post("/dbApi/v1/post/customer/new/")
async def post_new_customer(
    firstname: str,
    sirname: str,
    email: str,
    perms: Permission,
    company_name: Optional[str] = None,
) -> Any:
    """Route for creating new customer"""
    if not check_permission(perms,3):
        return return_403()
    customer = Customer(
        firstname=firstname,
        sirname=sirname,
        email=email,
        company_name=company_name,
    )
    db_manager.write_customer(customer)
    return {"response": 1}


# pylint:disable=too-many-arguments
@app.post("/dbApi/v1/post/hardware/new/")
async def post_new_hardware(
    perms: Permission,
    name: str,
    description: Optional[str] = None,
    size: Optional[str] = None,
    weight: Optional[float] = None,
    cable_length: Optional[float] = None,
    power_consumption: Optional[float] = None,
    workplace_ergonomics: Optional[str] = None,
) -> Any:
    """
    Route for creating new hardware
    """
    if not check_permission(perms, 4):
        return return_403()
    if not check_permission(perms,3):
        return return_403()
    hardware = Hardware(
        name=name,
        description=description,
        size=size,
        weight=weight,
        cable_length=cable_length,
        power_consumption=power_consumption,
        workplace_ergonomics=workplace_ergonomics,
    )
    db_manager.write_hardware(hardware)
    return {"response": 1}


@app.post("/dbApi/v1/post/offer/new/")
async def post_new_offer(
    perms: Permission,
    customer: Optional[int] = None,
    offer_file: Optional[int] = None,
    layout: Optional[int] = None,
    description: Optional[str] = None,
    hardware: Optional[list[int]] = None,
) -> Any:
    """
    Route for creating new offer
    """
    if not check_permission(perms, 4):
        return return_403()
    if not check_permission(perms,3):
        return return_403()
    offer = Offer(
        customer=customer,
        offer_file=offer_file,
        layout=layout,
        description=description,
        hardwware = hardware,
    )
    db_manager.write_offer(offer)
    return {"response": 1}


@app.post("/dbApi/v1/post/offer/file/new/")
async def post_new_offer_file(pdf_text: str, perms: Permission) -> Any:
    """
    Route for creating new offer file
    """
    if not check_permission(perms, 5):
        return return_403()
    if not check_permission(perms,3):
        return return_403()
    offer = OfferFile(pdf_text=pdf_text)
    db_manager.write_offer_file(offer)
    return {"response": 1}


@app.delete("/dbApi/v1/delete/customer/")
async def delete_cutomer(customer_id: int, perms: Permission) -> Any:
    """
    Route for deleting customer
    """
    if not check_permission(perms, 3):
        return return_403()
    db_manager.remove_customer(customer_id)
    return {"response": 1}


@app.delete("/dbApi/v1/delete/offer/")
async def delete_offer(offer_id: int, perms: Permission) -> Any:
    """
    Route for deleting offers
    """
    if not check_permission(perms, 4):
        return return_403()
    if not check_permission(perms,3):
        return return_403()
    db_manager.remove_offer(offer_id)
    return {"response": 1}


@app.delete("/dbApi/v1/delete/hardware/")
async def delete_hardware(hardware_id: int, perms: Permission) -> Any:
    """
    Route for deleting hardware
    """
    if not check_permission(perms, 3):
        return return_403()
    if not check_permission(perms,4):
        return return_403()
    db_manager.remove_hardware(hardware_id)
    return {"response": 1}


@app.delete("/dbApi/v1/delete/layout/")
async def delete_layout(layout_id: int, perms: Permission) -> Any:
    """
    Route for deleting layout
    """
    if not check_permission(perms, 2):
        return return_403()
    if not check_permission(perms,3):
        return return_403()
    db_manager.remove_layout(layout_id=layout_id)
    return {"response": 1}


@app.delete("/dbApi/v1/delete/offer/file/new/")
async def delete_offer_file(offer_id: int, perms: Permission) -> Any:
    """
    Route for deleting offer
    """
    if not check_permission(perms, 5):
        return return_403()
    if not check_permission(perms,3):
        return return_403()
    db_manager.remove_offer_file(offer_id=offer_id)
    return {"response": 1}
