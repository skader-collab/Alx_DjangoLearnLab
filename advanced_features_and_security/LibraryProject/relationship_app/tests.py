from django.test import TestCase, Client
from django.contrib.auth.models import User
from django_models.models import UserProfile

class AdminViewTest(TestCase):
    def setUp(self):
        """Create test users with different roles."""
        self.client = Client()

        # Admin user
        self.admin_user = User.objects.create_user(username="admin", password="adminpass")
        self.admin_profile = UserProfile.objects.get(user=self.admin_user)
        self.admin_profile.role = "Admin"
        self.admin_profile.save()

        # Non-admin user
        self.member_user = User.objects.create_user(username="member", password="memberpass")
        self.member_profile = UserProfile.objects.get(user=self.member_user)
        self.member_profile.role = "Member"
        self.member_profile.save()

    def test_admin_access(self):
        """Ensure Admin users can access the view."""
        self.client.login(username="admin", password="adminpass")
        response = self.client.get("/admin-dashboard/")
        self.assertEqual(response.status_code, 200)

    def test_non_admin_access(self):
        """Ensure Non-Admin users get a 403 Forbidden response."""
        self.client.login(username="member", password="memberpass")
        response = self.client.get("/admin-dashboard/")
        self.assertEqual(response.status_code, 403)


