// This file manages the quiz-related JavaScript functionality.

document.addEventListener('DOMContentLoaded', function() {
    const quizForm = document.getElementById('quiz-form');
    const resultContainer = document.getElementById('result-container');
    const submitButton = document.getElementById('submit-button');

    submitButton.addEventListener('click', function(event) {
        event.preventDefault();
        const formData = new FormData(quizForm);
        const answers = {};
        
        formData.forEach((value, key) => {
            answers[key] = value;
        });

        fetch('/submit-quiz', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(answers),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                displayResults(data.score, data.total);
            } else {
                alert('Error submitting quiz: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    function displayResults(score, total) {
        resultContainer.innerHTML = `
            <h2>Your Score: ${score} out of ${total}</h2>
            <p>${(score / total * 100).toFixed(2)}% Correct</p>
        `;
        resultContainer.style.display = 'block';
    }
});