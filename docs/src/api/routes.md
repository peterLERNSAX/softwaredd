# Routes

[Back](../api.md)

## Content

- [Route /dbApi/v1/post/customer/all/](#route-dbapiv1postcustomerall)

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
