from flask import Flask, render_template
from database import (
    create_tables,
    get_total_queries,
    get_total_alerts,
    get_recent_alerts,
    get_alert_counts_by_severity,
    get_top_suspicious_domains
)


app = Flask(__name__)


@app.route("/")
def index():
    create_tables()

    total_queries = get_total_queries()
    total_alerts = get_total_alerts()
    recent_alerts = get_recent_alerts()
    severity_counts = get_alert_counts_by_severity()
    top_domains = get_top_suspicious_domains()

    return render_template(
        "index.html",
        total_queries=total_queries,
        total_alerts=total_alerts,
        recent_alerts=recent_alerts,
        severity_counts=severity_counts,
        top_domains=top_domains
    )


if __name__ == "__main__":
    app.run(debug=True)