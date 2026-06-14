# DNS Exfiltration Detector

A defensive cybersecurity portfolio project that analyzes DNS logs for signs of DNS tunneling and DNS-based data exfiltration.

This first version is an offline command-line DNS log analyzer. It reads sample DNS logs, applies detection rules, scores suspicious activity, assigns severity levels, and prints alerts to the terminal.

## Project Goal

The goal of this project is to build a blue-team detection tool that can identify suspicious DNS activity commonly associated with DNS tunneling or DNS-based data exfiltration.

The project starts simple with offline log analysis and will later expand into SQLite storage, a Flask dashboard, Chart.js visualizations, and near real-time DNS monitoring.

## Current Version

**v0.1 - Offline DNS Log Analyzer**

Current features:

- Reads DNS logs from a sample log file
- Parses timestamp, source IP, domain, and DNS record type
- Detects suspicious DNS indicators
- Assigns alert scores
- Converts scores into severity levels
- Skips blank lines
- Skips malformed log lines
- Prints a summary of analyzed queries and generated alerts

## Detection Rules

The analyzer currently detects:

- Long subdomains
- Suspicious TXT record queries
- Base64-like encoded subdomains
- Hex-like encoded subdomains

## Technologies Used

Current version:

- Python
- Regular expressions
- Linux command line

Planned future technologies:

- SQLite
- Flask
- HTML
- CSS
- JavaScript
- Chart.js

## Project Structure

```text
dns-exfiltration-detector/
├── analyzer.py
├── README.md
├── data/
│   └── sample_dns.log
└── docs/
    └── roadmap.md
```

## Sample DNS Log Format

Each log line uses this format:

```text
timestamp,source_ip,domain,record_type
```

Example:

```text
2026-06-13 10:01:10,192.168.1.25,dGhpcyBpcyBleGZpbA.attacker-test.com,TXT
```

The analyzer parses each line into:

- Timestamp
- Source IP
- Domain
- DNS record type

## Detection Scoring

The analyzer uses a simple scoring system.

| Detection Rule | Score |
|---|---:|
| Long subdomain | +20 |
| Suspicious TXT record | +15 |
| Base64-like subdomain | +25 |
| Hex-like subdomain | +20 |

Severity levels:

| Score | Severity |
|---:|---|
| 1-29 | LOW |
| 30-59 | MEDIUM |
| 60+ | HIGH |

## How to Run

From the project folder, run:

```bash
python3 analyzer.py
```

## Example Output

```text
DNS Exfiltration Detector
-------------------------
Scanning DNS logs for suspicious activity...

[MEDIUM] dGhpcyBpcyBleGZpbA.attacker-test.com
  Timestamp: 2026-06-13 10:01:10
  Source IP: 192.168.1.25
  Record Type: TXT
  Score: 40
  Reasons: Suspicious TXT record, Base64-like subdomain

[MEDIUM] a9f83bc91d21ff45.attacker-test.com
  Timestamp: 2026-06-13 10:01:12
  Source IP: 192.168.1.25
  Record Type: A
  Score: 45
  Reasons: Base64-like subdomain, Hex-like subdomain

Summary
-------
Total queries analyzed: 7
Total alerts generated: 3
```

## Why DNS Exfiltration Matters

DNS is normally used to resolve domain names into IP addresses.

For example, when a user visits a website, the computer may ask a DNS resolver for the IP address of that domain.

Attackers can abuse DNS by hiding encoded data inside subdomains and sending DNS queries to domains they control.

Example suspicious DNS query:

```text
dGhpcyBpcyBleGZpbA.attacker-test.com
```

The first part of the domain may contain encoded or random-looking data. A defensive tool can look for suspicious patterns such as long subdomains, encoded strings, repeated unique subdomains, suspicious TXT records, and abnormal DNS query volume.

## Legal and Ethical Use

This project is for defensive cybersecurity learning and portfolio development only.

It should only be used with:

- Sample logs
- Generated test data
- DNS logs from systems or networks you own or have permission to analyze

This project does not perform attacks, does not exfiltrate data, and does not generate malicious DNS traffic.

## Planned Improvements

Future versions will add:

- SQLite database storage
- Storage for DNS queries and generated alerts
- Flask dashboard
- Alert filtering by severity
- Suspicious domain views
- Chart.js visualizations
- Query volume detection
- Repeated unique subdomain detection
- Abnormal DNS query frequency detection
- Near real-time log monitoring

## Version Roadmap

| Version | Focus | Status |
|---|---|---|
| v0.1 | Offline DNS log analyzer | Complete |
| v0.2 | SQLite database storage | Planned |
| v0.3 | Flask dashboard | Planned |
| v0.4 | Chart.js visualizations | Planned |
| v0.5 | Near real-time monitoring | Planned |