from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)  # typed text
    bio = models.TextField()
    years_experience = models.PositiveIntegerField()
    profile_image = models.ImageField(upload_to="profile/")
    cv = models.FileField(upload_to="cv/", blank=True)

    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)


class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.PositiveIntegerField()

class TimelineItem(models.Model):
    EXPERIENCE = "experience"
    EDUCATION = "education"

    TYPE_CHOICES = [
        (EXPERIENCE, "Experience"),
        (EDUCATION, "Education"),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price_from = models.DecimalField(max_digits=6, decimal_places=2)
    icon = models.CharField(max_length=50)

class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to="projects/")
    project_url = models.URLField(blank=True)

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="team/")

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to="testimonials/")

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)