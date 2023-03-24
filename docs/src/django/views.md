# Views

[Back](../django.md)

## Content

- [Additional functions](#additional-functions)
- [IndexView](#indexview)
- [DocsView](#docsview)
- [GeschaeftsprozesseView](#geschaeftsprozessview)
- [NotwendigedatenView](#notwendigedatenview)
- [SequenzView](#sequenzview)

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

- Checks if the current user is authenticated and returns the current user
- Otherwise returns `None`

[go up](#views)

---
---

### IndexView

```python
class IndexView(View):
    """Indexview"""
```

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
