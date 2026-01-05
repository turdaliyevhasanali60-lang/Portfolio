from .models import Skill

def get_skills(request):
    skills = Skill.objects.order_by('-level')

    left_skills = []
    right_skills = []

    for i, skill in enumerate(skills):
        if i % 2 == 0:
            left_skills.append(skill)
        else:
            right_skills.append(skill)

    return {
        'left_skills': left_skills,
        'right_skills': right_skills,
        'skills': skills,
    }