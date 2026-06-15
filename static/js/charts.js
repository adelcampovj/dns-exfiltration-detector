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