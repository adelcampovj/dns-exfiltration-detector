import sqlite3


DB_FILE = "data/dns_events.db"


def create_tables():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dns_queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            source_ip TEXT NOT NULL,
            domain TEXT NOT NULL,
            record_type TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            source_ip TEXT NOT NULL,
            domain TEXT NOT NULL,
            record_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            score INTEGER NOT NULL,
            reasons TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def insert_dns_query(timestamp, source_ip, domain, record_type):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO dns_queries (timestamp, source_ip, domain, record_type)
        VALUES (?, ?, ?, ?)
    """, (timestamp, source_ip, domain, record_type))

    connection.commit()
    connection.close()


def insert_alert(timestamp, source_ip, domain, record_type, severity, score, reasons):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO alerts (timestamp, source_ip, domain, record_type, severity, score, reasons)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (timestamp, source_ip, domain, record_type, severity, score, reasons))

    connection.commit()
    connection.close()


def get_total_queries():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM dns_queries")
    total = cursor.fetchone()[0]

    connection.close()
    return total


def get_total_alerts():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM alerts")
    total = cursor.fetchone()[0]

    connection.close()
    return total


def get_recent_alerts(limit=10):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT timestamp, source_ip, domain, record_type, severity, score, reasons
        FROM alerts
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    alerts = cursor.fetchall()

    connection.close()
    return alerts


def get_alert_counts_by_severity():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT severity, COUNT(*)
        FROM alerts
        GROUP BY severity
    """)

    rows = cursor.fetchall()
    connection.close()

    counts = {
        "LOW": 0,
        "MEDIUM": 0,
        "HIGH": 0
    }

    for severity, count in rows:
        counts[severity] = count

    return counts

def get_root_domain(domain):
    parts = domain.split(".")

    if len(parts) >= 2:
        return ".".join(parts[-2:])

    return domain


def get_top_suspicious_domains(limit=5):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT domain, score
        FROM alerts
    """)

    rows = cursor.fetchall()
    connection.close()

    domain_stats = {}

    for domain, score in rows:
        root_domain = get_root_domain(domain)

        if root_domain not in domain_stats:
            domain_stats[root_domain] = {
                "alert_count": 0,
                "highest_score": 0
            }

        domain_stats[root_domain]["alert_count"] += 1

        if score > domain_stats[root_domain]["highest_score"]:
            domain_stats[root_domain]["highest_score"] = score

    sorted_domains = sorted(
        domain_stats.items(),
        key=lambda item: (item[1]["alert_count"], item[1]["highest_score"]),
        reverse=True
    )

    top_domains = []

    for root_domain, stats in sorted_domains[:limit]:
        top_domains.append((
            root_domain,
            stats["alert_count"],
            stats["highest_score"]
        ))

    return top_domains


if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully.")