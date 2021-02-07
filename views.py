from django.shortcuts import render
from LoanApp.models import UserDetails,UserLoan
from LoanApp.forms import UserDetailsForm,UserLoanForm

# Create your views here.
money=0
def Register(request):
   
    form=UserDetailsForm()
    if request.method=="POST":
        form=UserDetailsForm(data=request.POST)
        
        if form.is_valid():
            money=form.cleaned_data['Allot']
            print(money)
            form.save(commit=True)
            print("stored")
            return Success(request)
        else:
            print("invalid")
    return render(request,'register.html',{'form':form})
def Success(request):
    return render(request,"RegSuccess.html")
def LoanGrant(request):
    form=UserLoanForm()
    
    
    form=UserLoanForm(data=request.POST)
    if form.is_valid():
        
        amount=form.cleaned_data['Amount']
        intrest=form.cleaned_data['rate']
        intrest=int(intrest)/100
        date=form.cleaned_data['Duration']
        year=(date/30)
        prince=amount*intrest*year
        print(money)
        if(100000>amount):
            form.save(commit=True)
            print("Granted")
            return final(request,prince)
        else:
            print("insufficiant")
    else:
        print("cant give loan")
    return render(request,"GrantLoan.html",{'form':form})

def final(request,prince):
    return render(request,"loanSuccess.html",{'prince':prince})
def Search(request):
    
    pan=request.POST.get('pan',False)
    query=UserLoan.objects.filter(Pan=pan).values().first()
    return render(request,"search.html",{'query':query})