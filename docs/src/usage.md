# On the usage of SoftwareDD

[back](../docs.md)

## Content

- [Getting started](#getting-started)
- [Webserver](#webserver)
- [API](#api)

## Getting started

- To use everything you need to set up a virtual environment
- It is clever to do that outside of your repository

```bash
    python -m venv .env
```

- Now activate the virtual environment

```bash
    source .env/bin/activate
```

- Go to your repository

```bash
    cd softwaredd
```

- Install all requirements

```bash
    pip install -r req.txt
```

- Got to the `manage.py` file

```bash
    cd softwaredd
```

- Start the webserver on port 7000

```bash
    python manage.py runserver 7000
```

- Open a new `shell` with `strg` + `shift` + `5`
- Go to `api`

```bash
    cd ..
    cd api
```

- Make sure that your `.env` is activated, otherwise activate it
- Run the API

```bash
    uvicorn main:app --reload
```

- Now you cam reach your services
  - Webserver: [127.0.0.1:7000](http://127.0.0.1:7000)
  - API: [127.0.0.1:8000](http://127.0.0.1:8000)
  - API Gui: [127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

[go up](#on-the-usage-of-softwaredd)

---
---

## Webserver

- Your `.env` should be activated for all actions
- Starting the webserver

```bash
    python manage.py runserver <portnumber>
```

- Make migrations

```bash
    python manage.py makemigrations
```

- Migrate

```bash
    python manage.py migrate
```

- Run tests

```bash
    python manage.py test
```

- Create a superuser

```bash
    python manage.py createsuperuser
```

- For more information see the [webserver docs](django.md)

[go up](#on-the-usage-of-softwaredd)

---
---

## API

- Your `.env` should be activated for all actions
- Starting the API

```bash
    uvicorn main:app --reload
```

- For more information see the [API docs](api.md)

[go up](#on-the-usage-of-softwaredd)

---
---
