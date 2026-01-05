from django.test import TestCase, Client
from django.urls import reverse
from .models import Profile, Results, Skill

class PortfolioTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(
            full_name="John Doe",
            title="Full Stack Developer",
            bio="Test Bio",
            years_experience=5,
            email="john@example.com",
            phone="123456789",
            address="Test Address",
            profile_image="profile/test.jpg"
        )
        self.results = Results.objects.create(
            happy_clients=10,
            completed_projects=20,
            comment1="Good",
            comment2="Job"
        )
        self.skill = Skill.objects.create(name="Python", level=90)

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertContains(response, "Python")

    def test_contact_form_submission(self):
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message'
        }
        response = self.client.post(reverse('home'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Thank you! Your message has been sent.")
