from django import forms

class EmailForm(forms.Form):
    sender_mail_id = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    receiver_mail_id = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
