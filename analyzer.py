import re
from database import create_tables, insert_dns_query, insert_alert

LOG_FILE = "data/sample_dns.log"


def is_long_subdomain(domain):
    first_part = domain.split(".")[0]

    if len(first_part) > 30:
        return True

    return False


def is_txt_record(record_type):
    if record_type.upper() == "TXT":
        return True

    return False


def is_base64_like(domain):
    first_part = domain.split(".")[0]

    pattern = r"^[A-Za-z0-9+/=]{12,}$"

    if re.match(pattern, first_part):
        return True

    return False


def is_hex_like(domain):
    first_part = domain.split(".")[0]

    pattern = r"^[a-fA-F0-9]{12,}$"

    if re.match(pattern, first_part):
        return True

    return False


def analyze_domain(domain, record_type):
    score = 0
    reasons = []

    if is_long_subdomain(domain):
        score += 20
        reasons.append("Long subdomain")

    if is_txt_record(record_type):
        score += 15
        reasons.append("Suspicious TXT record")

    if is_base64_like(domain):
        score += 25
        reasons.append("Base64-like subdomain")

    if is_hex_like(domain):
        score += 20
        reasons.append("Hex-like subdomain")

    return score, reasons


def get_severity(score):
    if score >= 60:
        return "HIGH"
    elif score >= 30:
        return "MEDIUM"
    elif score > 0:
        return "LOW"
    else:
        return "NONE"


def main():
    create_tables()

    total_queries = 0
    total_alerts = 0

    print("DNS Exfiltration Detector")
    print("-------------------------")
    print("Scanning DNS logs for suspicious activity...")

    with open(LOG_FILE, "r") as file:

        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split(",")

            if len(parts) != 4:
                print(f"Skipping malformed line: {line}")
                continue

            total_queries += 1

            timestamp, source_ip, domain, record_type = parts

            insert_dns_query(timestamp, source_ip, domain, record_type)

            score, reasons = analyze_domain(domain, record_type)
            severity = get_severity(score)

            if severity != "NONE":
                total_alerts += 1

                insert_alert(
                    timestamp,
                    source_ip,
                    domain,
                    record_type,
                    severity,
                    score,
                    ", ".join(reasons)
                )

                print()
                print(f"[{severity}] {domain}")
                print(f"  Timestamp: {timestamp}")
                print(f"  Source IP: {source_ip}")
                print(f"  Record Type: {record_type}")
                print(f"  Score: {score}")
                print(f"  Reasons: {', '.join(reasons)}")

    print()
    print("Summary")
    print("-------")
    print(f"Total queries analyzed: {total_queries}")
    print(f"Total alerts generated: {total_alerts}")


if __name__ == "__main__":
    main()