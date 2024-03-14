from django.shortcuts import render

people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person(username=username, password=password)
        people.append(person)
        return render(request, 'add.html', {'message': 'Person added successfully!'})
    return render(request, 'add.html')

def show_people(request):
    return render(request, 'show_people.html', {'people': people})