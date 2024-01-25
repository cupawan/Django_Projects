from django import forms

class NewsForm(forms.Form):
    state = forms.CharField(label='State', max_length=100)
    city = forms.CharField(label='City', max_length=100)
    category = forms.ChoiceField(label='Category', choices=[
        ('', 'Choose Category'),
        ('career', 'Career'),
        ('ayodhya-ram-mandir', 'Ayodhya Ram Mandir'),
        ('db-original', 'DB Original'),
        ('sports/cricket', 'Sports/Cricket'),
        ('entertainment', 'Entertainment'),
        ('lifestyle', 'Lifestyle'),
        ('israel-hamas-war', 'Israel-Hamas War'),
        ('women', 'Women'),
        ('national', 'National'),
        ('international', 'International'),
        ('business', 'Business'),
        ('tech-auto', 'Tech-Auto'),
        ('jeevan-mantra', 'Jeevan Mantra'),
        ('sports', 'Sports'),
        ('no-fake-news', 'No Fake News'),
        ('opinion', 'Opinion'),
        ('madhurima', 'Madhurima'),
        ('magazine', 'Magazine'),
        ('happylife', 'Happy Life'),
        ('utility', 'Utility'),
    ])
