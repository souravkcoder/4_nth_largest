from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = []
    message = ""
    input_val = ""

    if request.method == "POST":
        input_val = request.form["number"]
        try:
            n = int(input_val)
            result = [2 * i for i in range(1, n + 1)]
        except ValueError:
            message = "❌ Please enter a valid integer."

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Even Number Generator</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background-color: #f8f9fa;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                width: 90%;
                max-width: 500px;
                text-align: center;
            }
            input[type=number] {
                width: 80%;
                padding: 10px;
                font-size: 16px;
                margin-top: 10px;
                margin-bottom: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
            .result, .error {
                margin-top: 20px;
                font-size: 16px;
            }
            .error {
                color: red;
            }
            .result {
                background: #e9f5ff;
                padding: 10px;
                border-radius: 5px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Generate First N Even Numbers</h2>
            <form method="POST">
                <input name="number" type="number" placeholder="Enter a positive integer" value="{{ input_val }}">
                <br>
                <button type="submit">Generate</button>
            </form>

            {% if message %}
                <div class="error">{{ message }}</div>
            {% elif result %}
                <div class="result">
                    <strong>Even Numbers:</strong><br>{{ result }}
                </div>
            {% endif %}
        </div>
    </body>
    </html>
    """, result=result, message=message, input_val=input_val)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host="0.0.0.0", port=port)
