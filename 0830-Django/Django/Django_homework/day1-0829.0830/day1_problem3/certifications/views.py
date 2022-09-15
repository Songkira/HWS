from django.shortcuts import render
import random
# Create your views here.
def certification1(request): 
  age = range(25, 31)
  grade = ['a', 'b', 'c', 's']
  pick1 = random.choice(age)
  pick2 = random.choice(grade)

  context = {
    'age' : pick1,
    'grade' : pick2,
  }
  return render(request, 'certification1.html', context)

def certification2(request):
  age = range(25, 31)
  grade = ['a', 'b', 'c', 's']
  pick1 = random.choice(age)
  pick2 = random.choice(grade)

  context = {
    'age' : pick1,
    'grade' : pick2,
  }

  return render(request, 'certification2.html', context)

def certification3(request):
  age = range(25, 31)
  grade = ['a', 'b', 'c', 's']
  pick1 = random.choice(age)
  pick2 = random.choice(grade)

  context = {
    'age' : pick1,
    'grade' : pick2,
  }

  return render(request, 'certification3.html', context)