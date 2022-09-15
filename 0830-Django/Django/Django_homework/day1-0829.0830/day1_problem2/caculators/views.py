from django.shortcuts import render

# Create your views here.
def calculation(request):

  return render(request, 'calculation.html')

def result(request):
  one = int(request.GET.get('num1'))
  two = int(request.GET.get('num2'))
  if two != 0:
    divide = one / two
  else:
    divide = '계산할 수 없습니다'

  context = {
    'one' : one ,
    'two' : two , 
    'minus' : one - two,
    'multi' : one * two,
    'divide' : divide,
  }
  
  return render(request, 'result.html', context)

