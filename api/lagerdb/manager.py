"""DB Managers"""

from .models.models import Layout, OfferFile, Customer, Offer, Hardware
from sqlalchemy.orm.session import Session
from typing import Tuple

class DBManager:
    """Manager for DB interaction"""

    def __init__(self, used_session: Session) -> None:
        self.used_session: Session = used_session
    
    def write_layout(self, layout: Layout)->None:
        """
        Takes a layout 
        Creates a layout in the Database
        """
        self.used_session.add(layout)
        self.used_session.commit()

    def remove_layout(self, layout_id:int)->None:
        """
        Takes a layout
        Removes a layout from DB
        """
        old_layout: Layout =self.used_session.query(Layout).get(layout_id)
        self.used_session.delete(old_layout)
        self.used_session.commit()

    def show_all_layout(self)->Tuple[Layout,...]:
        """
        Resturns all Layouts from database
        """
        return tuple(self.used_session.query(Layout).all())

    def show_all_customers(self)->Tuple[Customer,...]:
        """
        Resturns all Customers from Database
        """
        return tuple(self.used_session.query(Customer).all())

    def show_all_hardware(self)->Tuple[Hardware,...]:
        """
        Returns all Hardware from Database
        """
        return tuple(self.used_session.query(Hardware).all())
    
    def show_all_offer(self)->Tuple[Offer]:
        """
        Returns all offers from Database
        """
        return tuple(self.used_session.query(Offer).all())
    
    def write_customer(self,customer:Customer)->None:
        """
        Takes a customer
        Creates a Customer in the Database
        """
        self.used_session.add(customer)
        self.used_session.commit()
    
    def write_offer(self,offer:Offer)->None:
        """
        Takes a offer 
        Cresates a offer in the Database
        """
        self.used_session.add(offer)
        self.used_session.commit()

    def write_hardware(self,hardware:Hardware)->None:
        """
        Takes Hardware
        Creates hardware in Database
        """
        self.used_session.add(hardware)
        self.used_session.commit()

    def write_offer_file(self, offer:OfferFile)->None:
        """
        Takes a Offer
        Creates a Offerfile in the Database
        """
        self.used_session.add(offer)
        self.used_session.commit()

    def remove_offer_file(self, offer_id:int)->None:
        """
        Takes a offer
        Removes the offer in the database
        """
        old_offer: OfferFile = self.used_session.query(OfferFile).get(offer_id)
        self.used_session.delete(old_offer)
        self.used_session.commit()
    
    def show_all_offer_file(self)->Tuple[OfferFile]:
        """
        Returns all offers from the database
        """
        return tuple(self.used_session.query(OfferFile).all())