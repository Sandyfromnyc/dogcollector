from django.shortcuts import render

dogs = [
  {'name': 'Max', 'breed': 'Biewer', 'description': 'he swears he is human', 'age': 2},
  {'name': 'Benji', 'breed': 'Shitzhu', 'description': 'playful, gentle and loving', 'age': 0},
]
# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', {
    'dogs': dogs
  })