// Define the API endpoint
const apiUrl = 'http://localhost:8000/api/getfeedback';

// Function to create the pie chart
function createPieChart(data) {
    const ctx = document.getElementById('pieChart').getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: Object.keys(data.feedback),
            datasets: [{
                data: Object.values(data.feedback),
                backgroundColor: ['#4caf50', '#f44336'], // Example colors
                hoverOffset: 4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            const label = tooltipItem.label || '';
                            const value = tooltipItem.raw || 0;
                            return `${label}: ${value}`;
                        }
                    }
                }
            }
        }
    });
    console.log('Pie chart created successfully.');
}

// Fetch data from the API and create the chart
fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json(); // Parse the JSON from the response
    })
    .then(data => {
        createPieChart(data);
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });
