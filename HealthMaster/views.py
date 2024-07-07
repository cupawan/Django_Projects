from django.shortcuts import render
from django.conf import settings
from .forms import DailyActivityForm
from Scripts.GoogleSheetAutomation import GoogleSheetsAutomation


def daily_activity_view(request):
    if request.method == "POST":
        form = DailyActivityForm(request.POST)
        if form.is_valid():
            data = {
                'date': form.cleaned_data['date'].strftime('%A, %d %b %Y'),
                'learning': form.cleaned_data['learning'],
                'meditation': form.cleaned_data['meditation'],
                'physical_activity': form.cleaned_data['physical_activity'],
                'sudoku': form.cleaned_data['sudoku'],
                'reading_writing': form.cleaned_data['reading_writing'],
                'comments': form.cleaned_data['comments'],
            }
            gs = GoogleSheetsAutomation()
            ws = gs.select_worksheet(sheet_name="CUPAWAN", worksheet_index=0)
            gs.insert_values(sheet = ws, append_row= list(data.values()))
            return render(request, 'success.html')

    else:
        form = DailyActivityForm()

    return render(request, 'daily_activity_form.html', {'form': form})
