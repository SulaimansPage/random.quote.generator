# Python Code to generate an HTML file with JavaScript that loads a new random quote on refresh

import random

# List of quotes
quotes = [
    "The best way to predict the future is to invent it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Act as if what you do makes a difference. It does.",
    "The stars whispered secrets to the moon, but only the dreamers could hear.",
    "In the chaos of the universe, find the stillness within yourself.",
    "She was poetry in a world still learning the alphabet.",
    "Lost in the haze of sunsets, she found herself again.",
    "You are the art that no gallery could ever contain.",
    "The ocean taught her to let go, and the sky taught her to rise.",
    "Even broken wings can create the most beautiful flight.",
    "In a world full of noise, her silence was her loudest scream.",
    "Let the rain kiss your soul and cleanse your chaos.",
    "The moon lives in the lining of your skin, glowing with untold stories."
]

# HTML template with embedded JavaScript for refreshing quotes on page load
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Quote Generator</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-color: #f0f8ff;
            color: #333;
        }}
        blockquote {{
            font-size: 1.5em;
            margin: 20px auto;
            line-height: 1.6;
            max-width: 600px;
            font-style: italic;
        }}
        p {{
            font-size: 1em;
            color: #666;
            margin-top: 20px;
        }}
    </style>
    <script>
        // List of quotes in JavaScript
        const quotes = {quotes};

        // Function to get a random quote
        function getRandomQuote() {{
            const randomIndex = Math.floor(Math.random() * quotes.length);
            return quotes[randomIndex];
        }}

        // Display the random quote when the page loads
        window.onload = function() {{
            document.getElementById('quote').innerText = getRandomQuote();
        }};
    </script>
</head>
<body>
    <h1>Random Quote Generator</h1>
    <blockquote id="quote"></blockquote>
    <p>Refresh the page to see a new quote!</p>
</body>
</html>
"""

# Save the HTML template to a file
with open("random_quote_with_js.html", "w", encoding="utf-8") as file:
    file.write(html_template)

print("HTML file generated! Open 'random_quote_with_js.html' in your browser.")
