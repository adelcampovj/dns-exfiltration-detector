from flask import Flask, render_template
from database import (
    create_tables,
    get_total_queries,
    get_total_alerts,
    get_recent_alerts,
    get_alert_counts_by_severity,
    get_top_suspicious_domains,
    get_detection_reason_counts
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
    reason_counts = get_detection_reason_counts()

    top_domain_labels = [domain[0] for domain in top_domains]
    top_domain_counts = [domain[1] for domain in top_domains]
    reason_labels = [reason[0] for reason in reason_counts]
    reason_values = [reason[1] for reason in reason_counts]

    return render_template(
        "index.html",
        total_queries=total_queries,
        total_alerts=total_alerts,
        recent_alerts=recent_alerts,
        severity_counts=severity_counts,
        top_domains=top_domains,
        top_domain_labels=top_domain_labels,
        top_domain_counts=top_domain_counts,
        reason_counts=reason_counts,
        reason_labels=reason_labels,
        reason_values=reason_values
    )


if __name__ == "__main__":
    app.run(debug=True)