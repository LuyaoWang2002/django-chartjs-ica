from django.shortcuts import render
from django.db.models import Count
from .models import PITAirportTrainFact


def fact_chart(request):
    daily_counts = (
        PITAirportTrainFact.objects.values('dateAdded')
        .annotate(count=Count('id'))
        .order_by('dateAdded')
    )
    dates = [row['dateAdded'].isoformat() for row in daily_counts]
    counts = [row['count'] for row in daily_counts]

    return render(request, 'pittrain/fact_chart.html', {
        'dates': dates,
        'counts': counts,
        'daily_counts': daily_counts,
        'total': sum(counts),
    })
