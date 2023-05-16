from django.db.models import Sum
from .models import Journal, Publication, Hit

def get_journal_statistics():
    # Retrieve all journals
    journals = Journal.objects.all()

    # Create a dictionary to store the summary statistics
    summary = {}

    # Iterate over the journals
    for journal in journals:
        # Retrieve all publications for the current journal
        publications = Publication.objects.filter(journal=journal)

        # Calculate the total views and downloads for the publications
        total_views = Hit.objects.filter(publication__in=publications, action=Hit.PAGEVIEW).count()
        total_downloads = Hit.objects.filter(publication__in=publications, action=Hit.DOWNLOAD).count()

        # Update the summary dictionary with the statistics
        summary[journal.id] = (total_views, total_downloads)

    return summary