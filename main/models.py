
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    years_experience = models.PositiveIntegerField()
    profile_image = models.ImageField(upload_to="profile/")
    cv = models.FileField(upload_to="cv/", blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    telegram_link = models.URLField(blank=True, help_text="Link to your Telegram channel/blog")

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    def __str__(self):
        return self.name


class Service(models.Model):
    ICON_CHOICES = [
        ('fa-paint-brush', 'Creative / Design'),
        ('fa-pencil-alt', 'Editing / Writing'),
        ('fa-vector-square', 'Graphic Design'),
        ('fa-images', 'Photography / Visuals'),
        ('fa-laptop-code', 'Programming / Software'),
        ('fa-cogs', 'Engineering / Tech Solutions'),
        ('fa-server', 'IT / Hosting'),
        ('fa-lightbulb', 'Innovation / Ideas'),
        ('fa-briefcase', 'Business / Consultancy'),
        ('fa-chart-line', 'Analytics / Growth'),
        ('fa-handshake', 'Partnerships / Deals'),
        ('fa-users', 'Team Services / HR'),
        ('fa-star', 'Quality / Premium'),
        ('fa-check-circle', 'Reliability / Completion'),
        ('fa-gem', 'Luxury / Value'),
        ('fa-award', 'Recognition / Top Service'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    price_from = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    project_url = models.URLField(blank=True)
    best = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="team/")

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    message = models.TextField()
    photo = models.ImageField(upload_to="testimonials/")
    best = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Results(models.Model):
    happy_clients = models.PositiveIntegerField(default=0)
    completed_projects = models.PositiveIntegerField(default=0)
    comment1 = models.TextField(blank=True, null=True)
    comment2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.happy_clients)

class Education(models.Model):
    degree = models.CharField(max_length=150)
    school = models.CharField(max_length=150)
    year = models.CharField(max_length=50) # e.g. "2018 - 2022"
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} at {self.school}"