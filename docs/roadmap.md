# Project Roadmap

## v0.1 - Offline DNS Log Analyzer

**Status:** Complete

Features:

- Read sample DNS logs
- Parse DNS query fields
- Detect long subdomains
- Detect suspicious TXT records
- Detect Base64-like subdomains
- Detect hex-like subdomains
- Score suspicious activity
- Assign severity levels
- Skip blank and malformed log lines
- Print alert summary in the terminal

## v0.2 - SQLite Storage

**Status:** Complete

Features:

- Created SQLite database
- Created `dns_queries` table
- Created `alerts` table
- Added database helper functions
- Saved parsed DNS queries to SQLite
- Saved generated alerts to SQLite
- Prepared stored data for future Flask dashboard

## v0.3 - Flask Dashboard

**Status:** Complete

Planned features:

- Build Flask web app
- Display total DNS queries
- Display total alerts
- Show recent alerts
- Show suspicious domains
- Add basic dashboard pages

## v0.4 - Chart.js Visualizations

**Status:** In Progress

Completed features:

- Added JavaScript folder
- Added Chart.js to the dashboard
- Added alerts-by-severity bar chart
- Top suspicious domains chart

Planned features:

- DNS query volume chart
- Detection reasons chart

## v0.5 - Near Real-Time Monitoring

**Status:** Planned

Planned features:

- Watch DNS log files for new entries
- Analyze new DNS events as they appear
- Save new alerts to the database
- Update dashboard with recent suspicious activity