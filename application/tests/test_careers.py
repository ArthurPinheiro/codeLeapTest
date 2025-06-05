import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from application.models import Career

@pytest.mark.django_db
class TestCareerAPI:

    def setup_method(self):
        self.client = APIClient()
        self.url = "/careers/"
        self.career = Career.objects.create(
            username="TestUser",
            title="Dev",
            content="Python",
            created_datetime="2025-06-05"
        )

    def test_create_career(self):
        payload = {
            "username": "Arthur",
            "created_datetime": "2025-05-06",
            "title": "Backend Developer",
            "content": "Python"
        }
        response = self.client.post(self.url, payload, format='json')
        assert response.status_code == 201
        assert Career.objects.filter(username="Arthur").exists()

    def test_list_careers(self):
        response = self.client.get(self.url)
        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert any(career["username"] == "TestUser" for career in response.data)

    def test_patch_career_valid(self):
        response = self.client.patch(f"{self.url}{self.career.id}/", {
            "title": "Software Engineer",
            "content": "Python"
        }, format='json')
        assert response.status_code == 200
        assert response.data["title"] == "Software Engineer"

    def test_patch_career_invalid_field(self):
        response = self.client.patch(f"{self.url}{self.career.id}/", {
            "username": "Pinheiro",
            "title": "Software Engineer"
        }, format='json')
        assert response.status_code == 400
        assert "username" in response.data

    def test_patch_career_invalid_field(self):
        response = self.client.patch(f"{self.url}{self.career.id}/", {
            "created_datetime": "2025-06-09"
        }, format='json')
        assert response.status_code == 400
        assert "created_datetime" in response.data

    def test_delete_career(self):
        response = self.client.delete(f"{self.url}{self.career.id}/")
        assert response.status_code == 204
        assert not Career.objects.filter(id=self.career.id).exists()
