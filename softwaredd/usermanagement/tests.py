"""
Tests
"""

from django.test import Client, TestCase
from django.urls import reverse

# Create your tests here.


class TestIndexView(TestCase):
    """
    Tests for index view
    """

    def __init__(self, methodName: str = "runTest") -> None:
        self.client = Client()
        self.url = reverse("index-view")
        super().__init__(methodName)

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

    def __init__(self, methodName: str = "runTest") -> None:
        self.client = Client()
        self.url = reverse("show-webserver-view")
        super().__init__(methodName)

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

    def __init__(self, methodName: str = "runTest") -> None:
        self.client = Client()
        self.url = reverse("geschaeftsprozess-view")
        super().__init__(methodName)

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

    def __init__(self, methodName: str = "runTest") -> None:
        self.client = Client()
        self.url = reverse("notwendigedaten-view")
        super().__init__(methodName)

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

    def __init__(self, methodName: str = "runTest") -> None:
        self.client = Client()
        self.url = reverse("sequenz-view")
        super().__init__(methodName)

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

    def __init__(self, methodName: str = "runTest") -> None:
        self.client = Client()
        self.url = reverse("use-case-view")
        super().__init__(methodName)

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

    def __init__(self, methodName: str = "runTest") -> None:
        self.client = Client()
        self.url = reverse("copyright-view")
        super().__init__(methodName)

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

    def __init__(self, methodName: str = "runTest") -> None:
        self.client = Client()
        self.url = reverse("webserver-view")
        super().__init__(methodName)

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
