from django import forms

class DailyActivityForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    learning = forms.BooleanField(required=False, label="Learning")
    meditation = forms.BooleanField(required=False, label="Meditation")
    physical_activity = forms.BooleanField(required=False, label="Physical Activity")
    sudoku = forms.BooleanField(required=False, label="Sudoku")
    reading_writing = forms.BooleanField(required=False, label="Reading & Writing")
    comments = forms.CharField(widget=forms.Textarea, required=False, label="Comments")
