# Views

[Back](../django.md)

## Content

- [Additional functions](#additional-functions)
- [IndexView](#indexview)
- [DocsView](#docsview)
- [GeschaeftsprozesseView](#geschaeftsprozessview)
- [NotwendigedatenView](#notwendigedatenview)
- [SequenzView](#sequenzview)
- [UseCaseView](#usecaseview)
- [CopyrightView](#copyrightview)
- [WebserverView](#webserverview)
- [EmployeeLogin](#employeelogin)
- [LogoutView](#logoutview)
- [DeleteEmployee](#deleteemployee)
- [ListEmployee](#listemployee)
- [ListLayoutView](#listlayoutview)
- [ListCustomerView](#listcustomerview)
- [ListHardwareView](#listhardwareview)

---
---

### Additional functions

#### get_employee

```python
def get_employee(request: HttpRequest) -> Optional[Employee]:
    """gets an employee"""
    if request.user.is_authenticated:
        employ: Employee = Employee.objects.get(username=request.user.username)
        return employ
    return None
```

Test coverage: `no`

- Checks if the current user is authenticated and returns the current user
- Otherwise returns `None`

#### employee_authentication

```python
    def employee_authentication(user: Employee, check_value: str) -> bool:
        """check permissions of employee"""
        check_user: Employee = Employee.objects.get(username=user.username)
        if check_value == "usermanagement":
            if not check_user.perm_usermanagement:
                return False
            return True
```

Test coverage: `no`

- Takes user of type [Employee](models.md#employee) and check_value of type `str` as argument
- Gets employee model from db
- checks if user has permission
- returns `bool`

[go up](#views)

---
---

### IndexView

```python
class IndexView(View):
    """Indexview"""
```

Test coverage: `yes`

- View for the `index` page

#### IndexView get

```python
def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(request, "usermanagement/index.html", {"employ": employ})
```

- Renders page `index.html` with the current user

[go up](#views)

---
---

### DocsView

```python
class DocsView(View):
    """Docs"""
```

Test coverage: `yes`

- View for the `index_webserver` page

#### DocsView get

```python
    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request, "usermanagement/index_webserver.html", {"employ": employ}
        )
```

- Returns page `index_webserver.html` with the current user

[go up](#views)

---
---

### GeschaeftsprozessView

```python
    class GeschaeftsprozessView(View):
        """Geschäftsprozesse"""
```

Test coverage: `yes`

- View for the `geschaeftsprozess` page

#### GeschaeftsprozessView get

```python
    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request,
            "usermanagement/geschaeftsprozess.html",
            {"employ": employ},
        )
```

- Renders page `geschaeftsprozess.html` with the current user

[go up](#views)

---
---

#### NotwendigedatenView

```python
    class NotwendigedatenView(View):
        """Notwendigedaten"""
```

Test coverage: `yes`

- View for the `notwendigedaten` page

#### NotwendigedatenView get

```python
    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request, "usermanagement/notwendigedaten.html", {"employ": employ}
        )
```

- Renders page `notwendigedaten.html` with the current user

[go up](#views)

---
---

### SequenzView

```python
    class SequenzView(View):
        """Sequenz"""
```

Test coverage: `yes`

- View for the `sequenz` page

#### SequenzView get

```python
    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request, "usermanagement/sequenz.html", {"employ": employ}
        )
```

- Renders page `sequenz.html` with the current user

[go up](#views)

---
---

### UseCaseView

```python
    class UseCaseView(View):
        """Use-Case"""
```

Test coverage: `yes`

- View for the `use-case` page

#### UseCaseView get

```python
    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request, "usermanagement/use-case.html", {"employ": employ}
        )
```

- Renders page `use-case.html` with the current user

[go up](#views)

---
---

### CopyrightView

```python
    class CopyrightView(View):
        """Copyright"""
```

Test coverage: `yes`

- View for `Copyright` page

#### CopyrightView get

```python
    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request, "usermanagement/copyright.html", {"employ": employ}
        )    
```

- Renders page `copyright.html` with the current user

[go up](#views)

---
---

### WebserverView

```python
    class WebserverView(View):
        """Webserver"""
```

Test coverage: `yes`

- View for the `webserver` page

#### WebserverView get

```python
    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        employ = get_employee(request)
        return render(
            request, "usermanagement/webserver.html", {"employ": employ}
        )
```

- Renders the page `webserver.html` with the current user

[go up](#views)

---
---

### EmployeeLogin

```python
    class EmployeeLogin(LoginView):
        """Login"""

        template_name = "usermanagement/login.html"
        success_url = "{% url 'index-view'%}"
```

Test coverage: `partly`

- View for the employee login
- Uses djangos built-in [LoginView](https://docs.djangoproject.com/en/4.0/topics/auth/default/) [Django Docs]

#### EmployeeLogin form_invalid

```python
    def form_invalid(self, form) -> HttpResponse:
        messages.warning(self.request,"Benutzerdaten nicht richtig!")
        return super().form_invalid(form)
```

- overwrites the built-in `form_invalid`
- adds a `waring` message

[go up](#views)

---
---

### LogoutView

```python
    class LogoutView(View):
        """Logout"""
```

Test coverage: `yes`

- View for employee logout

#### LogoutView get

```python
    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        logout(request)
        messages.info(request, "Erfolgreich abgemeldet")
        return redirect("index-view")
```

- Logs the current employee out
- Redirects to [IndexView](#indexview)

[go up](#views)

---
---

### DeleteEmployee

```python
    class DeleteEmployee(View):
        """Delete Employee"""
```

Test coverage: `no`

- View for deleting employees

#### DeleteEmployee post

```python
    def post(self, request: HttpRequest, uid: int) -> HttpResponse:
        """post"""
        if not request.user.is_authenticated:
            messages.error(request, "Unzureichende Berechtigungen")
            return redirect("index-view")
        employee = Employee.objects.get(pk=uid)
        employee.delete()
        messages.success(request, "Nutzer erfolgreich gelöscht")
        return redirect("list-employee-view")
```

- Takes uid of type `int` as parameter (userid of an employee)
- Checks if current user is authenticated
  - Shows `error` message if not
  - Redirects to [IndexView](#indexview) if not
- Deletes the choosen employee
- Shows `succes` message
- Redirects to [ListEmployee](#listemployee)

[go up](#views)

---
---

### ListEmployee

```python
    class ListEmployee(View):
        """List all Employees"""    
```

Test coverage: `no`

- View for listing all employees

#### ListEmployee get

```python
    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        all_employee = Employee.objects.all()
        employ = get_employee(request)
        return render(
            request,
            "usermanagement/list_employee.html",
            {"employees": all_employee, "employ": employ},
        )    
```

- Gets all employees
- Renders page `list_eployee.html` with all employees

[go up](#views)

---
---

### ListLayoutView

```python
    class ListLayoutView(View):
        """View for listing layouts"""
```

Test coverage: `no`

- View for listing all layouts

#### ListLayoutView get

```python
    def get(self,request:HttpRequest)->HttpResponse:
        """get"""
        url = API_URL+"/dbApi/v1/post/layout/all/"
        employee:Employee = Employee.objects.get(pk=request.user.pk)
        content:Response=requests.post(url,json=employee.get_permission_dict())
        content_dict = (json.loads(content.content))
        employ = get_employee(request)
        return render(request,"usermanagement/list_layout.html",{"content":content_dict["response"],"employ":employ})
```

- sets api url
- gets current employee
- creates dict with employee permissions
- sends `post` Request to the [API](../api.md)
  - [Route](../api/routes.md#route-dbapiv1postlayoutall)
- Renders page `list_layout.html`

[go up](#views)

---
---

### ListCustomerView

```python
    class ListCustomerView(View):
        """View for listing customers"""
```

Test coverage: `no`

- View for listing all customers

#### ListCustomerView get

```python
    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        if not request.user.is_authenticated:
            messages.warning(request, "Nicht Authentifiziert!")
            return redirect("index-view")
        url = API_URL + "/dbApi/v1/post/customer/all/"
        employee = Employee.objects.get(pk=request.user.pk)
        assert isinstance(employee, Employee)
        content: Response = requests.post(
            url, json=employee.get_permission_dict(), timeout=10
        )
        content_dict = json.loads(content.content)
        employ = get_employee(request)
        return render(
            request,
            "usermanagement/list_customer.html",
            {"content": content_dict["response"], "employ": employ},
        )
```

- sets api url
- gets current employee
- creates dict with employee permissions
- sends `post` Request to the [API](../api.md)
  - [Route](../api/routes.md#route-dbapiv1postcustomerall)
- Renders page `list_customer.html`

[go up](#views)

---
---

### ListHardwareView

```python
    class ListHardwareView(View):
        """View for listing hardware"""
```

Test coverage: `no`

- View for listing all hardware

#### ListHardwareView get

```python
    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        if not request.user.is_authenticated:
            messages.warning(request, "Nicht Authentifiziert!")
            return redirect("index-view")
        url = API_URL + "/dbApi/v1/post/hardware/all/"
        employee = Employee.objects.get(pk=request.user.pk)
        assert isinstance(employee, Employee)
        content: Response = requests.post(
            url, json=employee.get_permission_dict(), timeout=10
        )
        content_dict = json.loads(content.content)
        employ = get_employee(request)
        return render(
            request,
            "usermanagement/list_hardware.html",
            {"content": content_dict["response"], "employ": employ},
        )
```

- sets api url
- gets current employee
- creates dict with employee permissions
- sends `post` Request to the [API](../api.md)
  - [Route](../api/routes.md#route-dbapiv1posthardwareall)
- Renders page `list_hardware.html`

[go up](#views)

---
---

### CreateOfferView

```python
    class CreateOfferView(View):
        """View for creating an offer"""
```

Test coverage: `no`

- View for creating an offer

#### CreateOfferView get

```python
    def get(self, request: HttpRequest) -> HttpResponse:
        """get"""
        if not request.user.is_authenticated:
            messages.warning(request, "Nicht Authentifiziert!")
            return redirect("index-view")
        employee = Employee.objects.get(pk=request.user.pk)
        assert isinstance(employee, Employee)
        if not employee.perm_offer:
            messages.warning(request, "Unzureichende Berechtigungen")
            return redirect("index-view")
        url_customer = API_URL + "/dbApi/v1/post/customer/all/"
        customers: Response = requests.post(
            url_customer, json=employee.get_permission_dict(), timeout=10
        )
        customer_dict = json.loads(customers.content)

        url_layout = API_URL + "/dbApi/v1/post/layout/all/"
        layouts: Response = requests.post(
            url_layout, json=employee.get_permission_dict(), timeout=10
        )
        layout_dict = json.loads(layouts.content)

        url_offer_files = API_URL + "/dbApi/v1/post/offer/file/all/"
        offer_files: Response = requests.post(
            url_offer_files, json=employee.get_permission_dict(), timeout=10
        )
        offer_files_dict = json.loads(offer_files.content)
        form = CreateOfferForm()
        employ = get_employee(request)
        return render(
            request,
            "usermanagement/create_offer.html",
            {
                "form": form,
                "employ": employ,
                "customers": customer_dict["response"],
                "layouts": layout_dict["response"],
                "offer_files": offer_files_dict["response"],
            },
        )
```

- checks if user is logged in
- checks user permissions
- sets api url
- gets current employee
- creates dict with employee permissions
- sends `post` Request to the [API](../api.md)
  - [Route](../api/routes.md#route-dbapiv1postoffernew)
- Renders page `create_offer.html`

[go up](#views)

---
---
