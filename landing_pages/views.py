from django.shortcuts import render

# Create your views here.

def about_view(request):
    return render(request, 'about.html')

def help_view(request):
    return render(request, 'help/help.html')

def safety_view(request):
    return render(request, 'help/community_safety/safety.html')

def contact_view(request):
    return render(request, 'help/contact/contact.html')

def buyers_view(request):
    return render(request, 'help/for_buyers/buyers.html')

def sellers_view(request):
    return render(request, 'help/for_sellers/sellers.html')

def starting_view(request):
    return render(request, 'help/getting_started/starting.html')

def rules_view(request):
    return render(request, 'help/rules_and_policies/rules.html')

def your_account_view(request):
    return render(request, 'help/your_account/your_account.html')