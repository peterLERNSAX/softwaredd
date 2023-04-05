"""
Tests
"""

from django.contrib.messages import get_messages
from django.test import Client, TestCase
from django.urls import reverse

from .models import Employee

# Create your tests here.


class TestIndexView(TestCase):
    """
    Tests for index view
    """

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("index-view")

    def test_get_response(self) -> None:
        """
        Tests for a get response
        """
        response = self.client.get(self.url)
        self.assertNotEqual(response, None)

    def test_get_statuscode_200(self) -> None:
        """
        Checks if statuscode of response is 200
        Method GET
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_no_other_methods_status_code_405(self) -> None:
        """
        Checks if statuscode of response is 405
        Other methods
        """
        with self.subTest("POST"):
            response = self.client.post(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PUT"):
            response = self.client.put(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("DELETE"):
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("TRACE"):
            response = self.client.trace(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PATCH"):
            response = self.client.patch(self.url)
            self.assertEqual(response.status_code, 405)

    def test_template_rendered(self) -> None:
        """
        Checks if the correct template was rendered
        """
        response = self.client.get(self.url)
        self.assertEqual(
            response.templates[0].name, "usermanagement/index.html"
        )


class TestDocsView(TestCase):
    """
    Tests for DocsView
    """

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("show-webserver-view")

    def test_get_response(self) -> None:
        """
        Tests for a get response
        """
        response = self.client.get(self.url)
        self.assertNotEqual(response, None)

    def test_get_statuscode_200(self) -> None:
        """
        Checks if statuscode of response is 200
        Method GET
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_no_other_methods_status_code_405(self) -> None:
        """
        Checks if statuscode of response is 405
        Other methods
        """
        with self.subTest("POST"):
            response = self.client.post(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PUT"):
            response = self.client.put(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("DELETE"):
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("TRACE"):
            response = self.client.trace(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PATCH"):
            response = self.client.patch(self.url)
            self.assertEqual(response.status_code, 405)

    def test_template_rendered(self) -> None:
        """
        Checks if the correct template was rendered
        """
        response = self.client.get(self.url)
        self.assertEqual(
            response.templates[0].name, "usermanagement/index_webserver.html"
        )


class TestGeschaeftsprozessView(TestCase):
    """
    Tests for GeschaeftsprozessView
    """

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("geschaeftsprozess-view")

    def test_get_response(self) -> None:
        """
        Tests for a get response
        """
        response = self.client.get(self.url)
        self.assertNotEqual(response, None)

    def test_get_statuscode_200(self) -> None:
        """
        Checks if statuscode of response is 200
        Method GET
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_no_other_methods_status_code_405(self) -> None:
        """
        Checks if statuscode of response is 405
        Other methods
        """
        with self.subTest("POST"):
            response = self.client.post(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PUT"):
            response = self.client.put(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("DELETE"):
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("TRACE"):
            response = self.client.trace(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PATCH"):
            response = self.client.patch(self.url)
            self.assertEqual(response.status_code, 405)

    def test_template_rendered(self) -> None:
        """
        Checks if the correct template was rendered
        """
        response = self.client.get(self.url)
        self.assertEqual(
            response.templates[0].name, "usermanagement/geschaeftsprozess.html"
        )


class TestNotwendigedatenView(TestCase):
    """
    Tests for NotwendigedatenView
    """

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("notwendigedaten-view")

    def test_get_response(self) -> None:
        """
        Tests for a get response
        """
        response = self.client.get(self.url)
        self.assertNotEqual(response, None)

    def test_get_statuscode_200(self) -> None:
        """
        Checks if statuscode of response is 200
        Method GET
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_no_other_methods_status_code_405(self) -> None:
        """
        Checks if statuscode of response is 405
        Other methods
        """
        with self.subTest("POST"):
            response = self.client.post(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PUT"):
            response = self.client.put(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("DELETE"):
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("TRACE"):
            response = self.client.trace(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PATCH"):
            response = self.client.patch(self.url)
            self.assertEqual(response.status_code, 405)

    def test_template_rendered(self) -> None:
        """
        Checks if the correct template was rendered
        """
        response = self.client.get(self.url)
        self.assertEqual(
            response.templates[0].name, "usermanagement/notwendigedaten.html"
        )


class TestSequenzView(TestCase):
    """
    Tests for SequenzView
    """

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("sequenz-view")

    def test_get_response(self) -> None:
        """
        Tests for a get response
        """
        response = self.client.get(self.url)
        self.assertNotEqual(response, None)

    def test_get_statuscode_200(self) -> None:
        """
        Checks if statuscode of response is 200
        Method GET
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_no_other_methods_status_code_405(self) -> None:
        """
        Checks if statuscode of response is 405
        Other methods
        """
        with self.subTest("POST"):
            response = self.client.post(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PUT"):
            response = self.client.put(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("DELETE"):
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("TRACE"):
            response = self.client.trace(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PATCH"):
            response = self.client.patch(self.url)
            self.assertEqual(response.status_code, 405)

    def test_template_rendered(self) -> None:
        """
        Checks if the correct template was rendered
        """
        response = self.client.get(self.url)
        self.assertEqual(
            response.templates[0].name, "usermanagement/sequenz.html"
        )


class TestUseCaseView(TestCase):
    """
    Tests for UseCaseView
    """

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("use-case-view")

    def test_get_response(self) -> None:
        """
        Tests for a get response
        """
        response = self.client.get(self.url)
        self.assertNotEqual(response, None)

    def test_get_statuscode_200(self) -> None:
        """
        Checks if statuscode of response is 200
        Method GET
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_no_other_methods_status_code_405(self) -> None:
        """
        Checks if statuscode of response is 405
        Other methods
        """
        with self.subTest("POST"):
            response = self.client.post(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PUT"):
            response = self.client.put(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("DELETE"):
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("TRACE"):
            response = self.client.trace(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PATCH"):
            response = self.client.patch(self.url)
            self.assertEqual(response.status_code, 405)

    def test_template_rendered(self) -> None:
        """
        Checks if the correct template was rendered
        """
        response = self.client.get(self.url)
        self.assertEqual(
            response.templates[0].name, "usermanagement/use-case.html"
        )


class TestCopyrightView(TestCase):
    """
    Tests for CopyrightView
    """

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("copyright-view")

    def test_get_response(self) -> None:
        """
        Tests for a get response
        """
        response = self.client.get(self.url)
        self.assertNotEqual(response, None)

    def test_get_statuscode_200(self) -> None:
        """
        Checks if statuscode of response is 200
        Method GET
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_no_other_methods_status_code_405(self) -> None:
        """
        Checks if statuscode of response is 405
        Other methods
        """
        with self.subTest("POST"):
            response = self.client.post(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PUT"):
            response = self.client.put(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("DELETE"):
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("TRACE"):
            response = self.client.trace(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PATCH"):
            response = self.client.patch(self.url)
            self.assertEqual(response.status_code, 405)

    def test_template_rendered(self) -> None:
        """
        Checks if the correct template was rendered
        """
        response = self.client.get(self.url)
        self.assertEqual(
            response.templates[0].name, "usermanagement/copyright.html"
        )


class TestWebserverView(TestCase):
    """
    Tests for WebserverView
    """

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("webserver-view")

    def test_get_response(self) -> None:
        """
        Tests for a get response
        """
        response = self.client.get(self.url)
        self.assertNotEqual(response, None)

    def test_get_statuscode_200(self) -> None:
        """
        Checks if statuscode of response is 200
        Method GET
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_no_other_methods_status_code_405(self) -> None:
        """
        Checks if statuscode of response is 405
        Other methods
        """
        with self.subTest("POST"):
            response = self.client.post(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PUT"):
            response = self.client.put(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("DELETE"):
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("TRACE"):
            response = self.client.trace(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PATCH"):
            response = self.client.patch(self.url)
            self.assertEqual(response.status_code, 405)

    def test_template_rendered(self) -> None:
        """
        Checks if the correct template was rendered
        """
        response = self.client.get(self.url)
        self.assertEqual(
            response.templates[0].name, "usermanagement/webserver.html"
        )


class TestLoginView(TestCase):
    """
    Tests for the Login view
    """

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("login-view")

    def test_statuscode_200_get(self) -> None:
        """
        Tests that the statuscode is 200 in get
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_statuscode_200_post(self) -> None:
        """
        Tests that te statuscode is 200 in post
        """
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_get(self) -> None:
        """
        Tests that the correct template was loaded
        """
        response = self.client.get(self.url)
        self.assertEqual(
            response.templates[0].name,
            "usermanagement/login.html",
        )


class TestLogoutView(TestCase):
    """
    Tests for the LogoutView
    """

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("logout-view")
        self.user = Employee.objects.create(username="te")
        self.user.set_password("123")
        self.client.login(username="te", password="123")

    def test_statuscode_302_get(self) -> None:
        """
        Tests if statuscode is 302 in get
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_statuscode_200_get_after_redirect(self) -> None:
        """
        Tests if statuscode is 200 after the redirect
        """
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_if_user_is_logged_in(self) -> None:
        """
        Checks if the user is authenticated without logout view
        """
        self.assertTrue(self.user.is_authenticated)

    def test_user_is_logged_out(self) -> None:
        """
        Checks is the user is logged out after the request
        """
        response = self.client.get(self.url, follow=True)
        self.user.refresh_from_db()
        self.assertFalse(response.context["user"].is_authenticated)

    def test_logout_message(self) -> None:
        """
        Checks if the logout message is displayed correctly
        """
        response = self.client.get(self.url, follow=True)
        # Black magic to get messages
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertEqual(len(messages), 1)
        self.assertIn("Erfolgreich abgemeldet", messages)

    def test_no_other_methods_status_code_405(self) -> None:
        """
        Checks if statuscode of response is 405
        Other methods
        """
        with self.subTest("POST"):
            response = self.client.post(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PUT"):
            response = self.client.put(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("DELETE"):
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("TRACE"):
            response = self.client.trace(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PATCH"):
            response = self.client.patch(self.url)
            self.assertEqual(response.status_code, 405)


class TestDeleteEmployeeView(TestCase):
    """
    Tests for DeleteEmployee
    """

    def setUp(self) -> None:
        self.client = Client()
        self.user = Employee.objects.create(username="username")
        self.url = reverse("delete-employee-view", args=[self.user.pk])

    def test_statuscode_302_post_no_perms(self) -> None:
        """
        Checks if the statuscode is 302 in post
        """
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)

    def test_statuscode_302_post_perms(self) -> None:
        """
        Checks if the statuscode is 302 in post
        """
        admin = Employee.objects.create(username="admin")
        assert isinstance(admin, Employee)
        self.client.force_login(admin)
        admin.perm_usermanagement = True
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)

    def test_statuscode_200_post_after_redirect_no_perms(self) -> None:
        """
        Checks if the statuscode is 200 after the redirect in post
        """
        response = self.client.post(self.url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_statuscode_200_post_after_redirect_perms(self) -> None:
        """
        Checks if the statuscode is 200 after the redirect in post
        """
        admin = Employee.objects.create(username="admin")
        assert isinstance(admin, Employee)
        self.client.force_login(admin)
        admin.perm_usermanagement = True
        response = self.client.post(self.url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_employee_was_not_deleted(self) -> None:
        """
        Checks if the employee was not deleted because of missing perms
        """
        self.assertIn(self.user, Employee.objects.all())
        _ = self.client.post(self.url, follow=True)
        self.user.refresh_from_db()
        self.assertIn(self.user, Employee.objects.all())

    def test_employee_was_deleted(self) -> None:
        """
        Checks if the employee was deleted
        """
        admin = Employee.objects.create(username="admin")
        assert isinstance(admin, Employee)
        self.client.force_login(admin)
        admin.perm_usermanagement = True
        self.assertIn(self.user, Employee.objects.all())
        _ = self.client.post(self.url, follow=True)
        self.assertNotIn(self.user, Employee.objects.all())

    def test_message_no_perms(self) -> None:
        """
        Checks if the logout message is displayed correctly
        """
        response = self.client.post(self.url, follow=True)
        # Black magic to get messages
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertEqual(len(messages), 1)
        self.assertIn("Unzureichende Berechtigungen", messages)

    def test_message_perms(self) -> None:
        """
        Checks if the logout message is displayed correctly
        """
        admin = Employee.objects.create(username="admin")
        assert isinstance(admin, Employee)
        self.client.force_login(admin)
        admin.perm_usermanagement = True
        response = self.client.post(self.url, follow=True)
        # Black magic to get messages
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertEqual(len(messages), 1)
        self.assertIn("Nutzer erfolgreich gelöscht", messages)

    def test_no_other_methods_status_code_405_no_perms(self) -> None:
        """
        Checks if statuscode of response is 405
        Other methods
        """
        admin = Employee.objects.create(username="admin")
        assert isinstance(admin, Employee)
        self.client.force_login(admin)
        admin.perm_usermanagement = True
        with self.subTest("GET"):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PUT"):
            response = self.client.put(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("DELETE"):
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("TRACE"):
            response = self.client.trace(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PATCH"):
            response = self.client.patch(self.url)
            self.assertEqual(response.status_code, 405)

    def test_no_other_methods_status_code_405_perms(self) -> None:
        """
        Checks if statuscode of response is 405
        Other methods
        """
        with self.subTest("GET"):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PUT"):
            response = self.client.put(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("DELETE"):
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("TRACE"):
            response = self.client.trace(self.url)
            self.assertEqual(response.status_code, 405)
        with self.subTest("PATCH"):
            response = self.client.patch(self.url)
            self.assertEqual(response.status_code, 405)
