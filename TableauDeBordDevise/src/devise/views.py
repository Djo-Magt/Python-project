from django.shortcuts import render, redirect
import api

def redirect_index(request):
    return redirect("home", days_range=30, symb='IBM,AAPL,GOOGL,')

# Create your views here.
def dashboard(request, days_range=30, symb=''):
    days, rates = api.get_rates(symbols = symb.split(","), days=days_range)
    if '' in rates:
        del rates[''] 
    
    page_label = {7:"Semaine", 30:"Mois", 365:"Année"}.get(days_range, "Personnalisée")
    return render(request, "devise/index.html", context={"data": rates,
                                                         "days_labels": days,
                                                         "symb": symb,
                                                         "page_label": page_label})
    