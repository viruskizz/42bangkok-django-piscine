import os

from django.shortcuts import render
from django import forms
from datetime import datetime
from django.conf import settings

LOG_FILE = "ex02/history.log"

def read_data() -> dict:
    data = {}
    filename = settings.EX02_LOG_FILE or LOG_FILE
    if not os.path.exists(os.path.dirname(filename)):
        return data
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip("\n")
            kv = line.split(',')
            data[kv[0]] = kv[1]
        f.close()
    return data

def save_file(data: dict) -> None:
    filename = settings.EX02_LOG_FILE or LOG_FILE
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        for key,value in data.items():
            line = f'{key},{value}\n'
            f.write(line)
        f.close()

class HistoryForm(forms.Form):
    history = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input history', 'class': 'form-control m-2'}))

# Create your views here.
def index(request):
    data = read_data()
    if request.method == "POST":
        print(request)
        form = HistoryForm(request.POST)
        now = datetime.now()
        dt = now.isoformat()
        data[dt] = form.data['history']
        save_file(data)
        if form.is_valid():
            return render(request, "ex02/index.html", {"form": form, "data": data})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HistoryForm()
        return render(request, "ex02/index.html", {"form": form, "data": data})