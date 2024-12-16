from django.http import JsonResponse
from .scraper import scrape_work_ua, scrape_rabota_ua

def search_vacancies(request):
    query = request.GET.get("query", "")

    if not query:
        return JsonResponse({"error": "Query parameter is required."}, status=400)

    work_ua_results = scrape_work_ua(query)
    rabota_ua_results = scrape_rabota_ua(query)

    return JsonResponse({
        "source": {
            "work_ua": work_ua_results,
            "rabota_ua": rabota_ua_results
        }
    })