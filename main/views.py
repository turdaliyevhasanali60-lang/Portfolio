from django.shortcuts import render
from django.views import View
from main.models import *
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

class Home(View):
    def get(self, request):
        profile = Profile.objects.first()
        result = Results.objects.first()
        services = Service.objects.all()
        projects = Project.objects.all()
        members = TeamMember.objects.all()
        clients = Testimonial.objects.filter(best=True)
        education = Education.objects.order_by('-year')
        form = ContactForm()
        context = {
            'profile': profile,
            'result': result,
            'services': services,
            'projects': projects,
            'members': members,
            'clients': clients,
            'education': education,
            'form': form,
        }
        return render(request, 'index.html', context)

    def post(self, request):
        form = ContactForm(request.POST)
        success = False
        if form.is_valid():
            cd = form.cleaned_data

            # Save to DB
            ContactMessage.objects.create(
                name=cd['name'],
                phone=cd['phone'],
                subject=cd['subject'],
                message=cd['message']
            )

            # Optional: send email
            send_mail(
                f"{cd['subject']} - from {cd['name']}",
                cd['message'],
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,  # keep it safe
            )

            success = True
            form = ContactForm()  # clear form

        profile = Profile.objects.first()
        result = Results.objects.first()
        services = Service.objects.all()
        projects = Project.objects.all()
        members = TeamMember.objects.all()
        clients = Testimonial.objects.filter(best=True)
        education = Education.objects.order_by('-year')
        context = {
            'profile': profile,
            'result': result,
            'services': services,
            'projects': projects,
            'members': members,
            'clients': clients,
            'education': education,
            'form': form,
            'success': success,
        }
        return render(request, 'index.html', context)