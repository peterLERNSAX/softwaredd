# Routes

[Back](../api.md)

## Content

- [Route /dbApi/v1/post/customer/all/](#route-dbapiv1postcustomerall)
- [Route /dbApi/v1/post/customer/new/](#route-dbapiv1postcustomernew)
- [Route /dbApi/v1/delete/customer/](#route-dbapiv1deletecustomer)
- [Route /dbApi/v1/post/offer/all/](#route-dbapiv1postofferall)
- [Route /dbApi/v1/post/offer/new/](#route-dbapiv1postoffernew)
- [Route /dbApi/v1/post/hardware/all/](#route-dbapiv1posthardwareall)
- [Route /dbApi/v1/post/hardware/new/](#route-dbapiv1posthardwarenew)
- [Route /dbApi/v1/post/layout/all/](#route-dbapiv1postlayoutall)
- [Route /dbApi/v1/post/layout/new/](#route-dbapiv1postlayoutnew)
- [Route /dbApi/v1/post/offer/file/all/](#route-dbapiv1postofferfileall)
- [Route /dbApi/v1/post/offer/file/new/](#route-dbapiv1postofferfilenew)

---
---

## Route /dbApi/v1/post/customer/all/

```python
    @app.post("/dbApi/v1/post/customer/all/")
    async def get_all_customers(perms:Permission):
        """
        Route for getting all customers from db
        """
        if not check_permission(perms,4):
            return return_403()
        customers = db_manager.show_all_customers()
        return {"response":customers}
```

Test coverage: `no`

- Route for getting all custmers from the database
- Method: `post`
- Arguments:
  - perms of type: [Permission](models.md#permission)
- Gets all customers from db
- Returns all customers

[go up](#routes)

---
---

## Route /dbApi/v1/post/customer/new/

```python
    @app.post("/dbApi/v1/post/customer/new/")
    async def post_new_customer(firstname:str,sirname:str,email:str,
                            perms:Permission,company_name:Optional[str]=None):
        """Route for creating new customer"""
        if not check_permission(perms,4):
            return return_403()
        customer = Customer(firstname=firstname,sirname=sirname,email=email,company_name=company_name)
        db_manager.write_customer(customer)
        return {"response":1}  
```

Test coverage: `no`

- Route for adding a new customer to the database
- Method: `post`
- Arguments:
  - firstname of type: `str`
  - sirname of type: `str`
  - email of type: `str`
  - perms of type: [Permission](models.md#permission)
  - company_name of type: `Optional[str]` with default `None`
- Returns [return_403](functions.md#return_403) if permissions are missing
- Returns 1 if everything worked

[go up](#routes)

---
---

## Route /dbApi/v1/delete/customer/

```python
    @app.delete("/dbApi/v1/delete/customer/")
    async def delete_cutomer(customer_id:int,perms:Permission):
        """
        Route for deleting customer
        """
        if not check_permission(perms,3):
            return return_403()
        db_manager.remove_customer(customer_id)
        return {"response":1}
```

Test coverage: `no`

- Route for deleting customer to the database
- Method: `post`
- Arguments:
  - customer_id of type: `int`
  - perms of type: [Permission](models.md#permission)
  - company_name of type: `Optional[str]` with default `None`
- Returns [return_403](functions.md#return_403) if permissions are missing
- Returns 1 if everything worked

[go up](#routes)

---
---

## Route /dbApi/v1/post/offer/all/

```python
    @app.post("/dbApi/v1/post/offer/all/")
    async def get_all_offer(perms:Permission):
        """
        Route for getting all offers from db
        """
        if not check_permission(perms,4):
            return return_403()
        offers = db_manager.show_all_offer()
        return {"response":offers}
```

Test coverage: `no`

- Route for getting all offers from Database
- Method: `post`
- Arguments:
  - perms of type: [Permission](models.md#permission)
- Gets all offers from db
- Returns all offers

[go up](#routes)

---
---

## Route /dbApi/v1/post/offer/new/

```python
    @app.post("/dbApi/v1/post/offer/new/")
    async def post_new_offer(perms:Permission,
                         customer:Optional[int]=None,
                         offer_file:Optional[int]=None,
                         layout:Optional[int]=None,
                         description:Optional[str]=None):
        """
        Route for creating new offer
        """
        if not check_permission(perms,4):
            return return_403()
        offer = Offer(customer=customer,offer_file=offer_file,layout=layout,description=description)
        db_manager.write_offer(offer)
        return {"response":1}
```

Test coverage: `no`

- Route for adding a new offer to the database
- Method: `post`
- Arguments:
  - perms of type: [Permission](models.md#permission)
  - customer (FK) of type: `Optional[int]` with default `None`
  - offer_file (FK) of type: `Optional[int]` with default `None`
  - layout (FK) of type: `Optional[int]` with default `None`
  - description of type: `Optional[str]` with default `None`
- Returns [return_403](functions.md#return_403) if permissions are missing
- Returns 1 if everything worked

[go up](#routes)

---
---

## Route /dbApi/v1/post/hardware/all/

```python
    @app.post("/dbApi/v1/post/hardware/all/")
    async def get_all_hardware(perms:Permission):
        """
        Route for getting all hardware from db
        """
        if not check_permission(perms,4):
            return return_403()
        hardware = db_manager.show_all_hardware()
        return {"response":hardware}
```

Test coverage: `no`

- Route for getting all hardware from Database
- Method: `post`
- Arguments:
  - perms of type: [Permission](models.md#permission)
- Gets all hardware from db
- Returns all hardware

[go up](#routes)

---
---

## Route /dbApi/v1/post/hardware/new/

```python
    @app.post("/dbApi/v1/post/hardware/new/")
async def post_new_hardware(perms:Permission,name:str,
                            description:Optional[str]=None,
                            size:Optional[str]=None,
                            weight:Optional[float]=None,
                            cable_length:Optional[float]=None,
                            power_consumption:Optional[float]=None,
                            workplace_ergonomics:Optional[str]=None):
    """
    Route for creating new hardware
    """
    if not check_permission(perms,4):
        return return_403()
    hardware = Hardware(name=name,
                        description=description,
                        size=size,
                        weight=weight,
                        cable_length=cable_length,
                        power_consumption=power_consumption,
                        workplace_ergonomics=workplace_ergonomics)
    db_manager.write_hardware(hardware)
    return {"response":1}
```

Test coverage: `no`

- Route for adding a new hardware to the database
- Method: `post`
- Arguments:
  - perms of type: [Permission](models.md#permission)
  - description of type: `Optional[str]` with default `None`
  - size of type: `Optional[str]` with default `None`
  - weight of type: `Optional[float]` with default `None`
  - cable_length of type: `Optional[float]` with default `None`
  - power_consumption of type: `Optional[float]` with default `None`
  - workplace_ergonomics of type: `Optional[str]` with default `None`
- Returns [return_403](functions.md#return_403) if permissions are missing
- Returns 1 if everything worked

[go up](#routes)

---
---

## Route /dbApi/v1/post/layout/all/

```python
    @app.post("/dbApi/v1/post/layout/all/")
    async def get_all_layout(perms:Permission):
        """
        Route for getting all layouts from db
        """
        if not check_permission(perms,2):
            return return_403()
        layouts = db_manager.show_all_layout()
        return {"response":layouts}
```

Test coverage: `no`

- Route for getting all layouts from Database
- Method: `post`
- Arguments:
  - perms of type: [Permission](models.md#permission)
- Gets all layouts from db
- Returns all layouts

[go up](#routes)

---
---

## Route /dbApi/v1/post/layout/new/

```python
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
```

Test coverage: `no`

- Route for adding a new layout to the database
- Method: `post`
- Arguments:
  - pdf_text of type: `str`
  - perms of type: [Permission](models.md#permission)
- Returns [return_403](functions.md#return_403) if permissions are missing
- Returns 1 if everything worked

[go up](#routes)

---
---

## Route /dbApi/v1/post/offer/file/all/

```python
    @app.post("/dbApi/v1/post/offer/file/all/")
    async def get_all_offer_file(perms:Permission):
        """
        Route for getting all offers from db
        """
        if not check_permission(perms,5):
            return return_403()
        offers = db_manager.show_all_offer_file()
        return {"response":offers}
```

Test coverage: `no`

- Route for getting all offer files from Database
- Method: `post`
- Arguments:
  - perms of type: [Permission](models.md#permission)
- Gets all offer files from db
- Returns all offer files

[go up](#routes)

---
---

## Route /dbApi/v1/post/offer/file/new/

```python
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
```

Test coverage: `no`

- Route for adding a new offer file to the database
- Method: `post`
- Arguments:
  - pdf_text of type: `str`
  - perms of type: [Permission](models.md#permission)
- Returns [return_403](functions.md#return_403) if permissions are missing
- Returns 1 if everything worked

[go up](#routes)

---
---
