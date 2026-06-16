const severityChartElement = document.getElementById("severityChart");

if (severityChartElement) {
    new Chart(severityChartElement, {
        type: "bar",
        data: {
            labels: ["LOW", "MEDIUM", "HIGH"],
            datasets: [
                {
                    label: "Alert Count",
                    data: [
                        severityCounts.low,
                        severityCounts.medium,
                        severityCounts.high
                    ]
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                },
                title: {
                    display: true,
                    text: "Alerts by Severity"
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    });
}


const topDomainsChartElement = document.getElementById("topDomainsChart");

if (topDomainsChartElement) {
    new Chart(topDomainsChartElement, {
        type: "bar",
        data: {
            labels: topDomainLabels,
            datasets: [
                {
                    label: "Alert Count",
                    data: topDomainCounts
                }
            ]
        },
        options: {
            responsive: true,
            indexAxis: "y",
            plugins: {
                legend: {
                    display: false
                },
                title: {
                    display: true,
                    text: "Top Suspicious Domains"
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    });
}