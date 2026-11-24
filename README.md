# Django + Chart.js ICA

I added a Chart.js bar chart to my Django train facts project. It shows how
many facts were added on each date. The dates and counts come from the
SQLite database, not from fixed values in the chart.

The sample data has one fact added on November 17, 2026. After adding more
facts to the database, refresh the page to update the chart.

## Run locally

Use Python 3.14 and run these commands from the project folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata sample_facts
python manage.py runserver 127.0.0.1:8001
```

Open http://127.0.0.1:8001/ to see the chart and its data table.
Load the sample fixture into a fresh database; it represents the sample
record used for this ICA. The local database and virtual environment are
not included in GitHub.

## Files

- `pittrain/models.py`: fact text and date added.
- `pittrain/views.py`: group facts by date and count them.
- `pittrain/templates/pittrain/fact_chart.html`: chart and data table.
- `pittrain/static/pittrain/chart.umd.min.js`: Chart.js library (4.6.1, MIT).
- `pittrain/fixtures/sample_facts.json`: sample record for viewing the chart.

This is a local classroom project, not a production deployment.
