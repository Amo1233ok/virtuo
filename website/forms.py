from django import forms

class RequeteForm():
    
    Nom = forms.CharField(
        label='nom',
        widget=forms.Textarea(attrs={
            'placeholder': 'Entrez votre nom ici...',
             
             
        })
    )
    telephone = forms.CharField(
        label='telephone',
        widget=forms.Textarea(attrs={
            'placeholder': 'Entrez votre numero de telephone ici...',
             
             
        })
    )
    email = forms.EmailField(
        label='email',
        widget=forms.Textarea(attrs={
            'placeholder': 'Entrez votre email ici...',
             
             
        })
    )
    objet = forms.CharField(
        label='nom',
        widget=forms.Textarea(attrs={
            'placeholder': 'Entrez votre le sujet de votre message ici...',
             
             
        })
    )
    message = forms.CharField(
        label='mesage',
        widget=forms.Textarea(attrs={
            'placeholder': 'Entrez votre message ici...',
             
             
        })
    )