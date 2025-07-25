from django.shortcuts import render
from .models import Dataset, Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from .hive_client import fetch_hive_data
from .models import *

def home_view(request):
    recent_datasets = Dataset.objects.order_by('-created_at')[:5]
    categories = Category.objects.all()
    return render(request, 'marketplace/home.html', {
        'recent_datasets': recent_datasets,
        'categories': categories,
    })


def instant_market_place(request):


    return render(request,"marketplace/test.html")


def sales_view(request):
    return render(request, 'marketplace/sales.html')




# def home(request):
#     return render(request, 'index.html')

# def get_sample_data(request):
#     query = "SELECT * FROM your_table LIMIT 100"  # change `your_table`
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         columns = [col[0] for col in cursor.description]
#         rows = cursor.fetchall()
#     return JsonResponse({'columns': columns, 'rows': rows})

# def custom_query(request):
#     if request.method == 'POST':
#         query = request.POST.get('query')
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute(query + " LIMIT 100")  # enforce limit
#                 columns = [col[0] for col in cursor.description]
#                 rows = cursor.fetchall()
#             return JsonResponse({'columns': columns, 'rows': rows, 'error': None})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})



# ========= FAKER Sample Data ===========


"""
def get_sample_data(request):
    records = CustomerEligibility.objects.all()[:100]  # fetch first 100
    columns = ["Customer ID", "Name", "Credit Score", "Eligibility Status", "Created At"]
    rows = [
        [
            r.customer_id,
            r.name,
            r.credit_score,
            r.eligibility_status,
            r.created_at.strftime("%Y-%m-%d %H:%M")
        ]
        for r in records
    ]
    return JsonResponse({"columns": columns, "rows": rows})

"""

#  ============== Fetch Hive Data ============

def get_sample_data(request):
    columns, data = fetch_hive_data()
    rows = [list(row) for row in data]  # convert tuples to lists for JSON

    return JsonResponse({
        "columns": columns,
        "rows": rows
    })
