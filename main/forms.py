from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Your Name'}),
        label='Your Name'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'glass-input', 'placeholder': 'Your Email'}),
        label='Your Email'
    )
    subject = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Subject'}),
        label='Subject'
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'glass-input', 'placeholder': 'Leave a message here', 'style':'height:100px'}),
        label='Message'
    )