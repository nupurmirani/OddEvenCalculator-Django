from django.shortcuts import render
def oddEven(request):
    
    n=int(request.POST.get('number'))
    ans=None
    if request.method =='POST':
        try:
            if n % 2 == 0:
                ans="Even"
            else:
                ans="Odd"
        except:
            ans="Invalid Input"
    else:
        print("Invalid! Request Method Not Identified \n Try Again ")
    return render(request,"oddEven.html", {'ans': ans})