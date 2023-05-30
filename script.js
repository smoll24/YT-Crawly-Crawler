var json = '{"top_phrases": [["pona", 2610], ["toki", 1840], ["musi", 740], ["mute", 670], ["kalama", 630], ["tawa", 550], ["sina", 360], ["kute", 320], ["language", 310], ["jan", 260]]}';

var data = JSON.parse(json);
var top_phrases = data.top_phrases;

var phrases = [];
var frequencies = [];

// Extract phrases and frequencies from the top_phrases array
for (var i = 0; i < top_phrases.length; i++) {
  var phrase = top_phrases[i][0];
  var frequency = top_phrases[i][1];
  
  phrases.push(phrase);
  frequencies.push(frequency);
}

// Create a bar chart using Chart.js
var ctx = document.getElementById('chart').getContext('2d');
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: phrases,
        datasets: [{
            label: 'Toki Pona Trends',
            data: frequencies,
            backgroundColor: 'rgba(75, 192, 192, 0.8)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Frequency'
                }
            }
        }
    }
});
