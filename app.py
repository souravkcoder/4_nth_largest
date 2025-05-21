from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def nth_largest():
    result = ""
    if request.method == "POST":
        numbers = request.form.get("numbers")
        n = request.form.get("n")

        try:
            num_list = list(map(int, numbers.strip().split(",")))
            n = int(n)
            if n <= 0 or n > len(num_list):
                result = f"❌ Please enter a valid N between 1 and {len(num_list)}"
            else:
                num_list.sort(reverse=True)
                nth = num_list[n - 1]
                result = f"✅ The {n}th largest number is: <b>{nth}</b>"
        except Exception as e:
            result = f"❌ Error: {str(e)}"

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Nth Largest Number</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #f2f6fc;
                display: flex;
                flex-direction: column;
                align-items: center;
                padding-top: 60px;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                width: 90%;
                max-width: 500px;
            }
            input[type="text"], input[type="number"] {
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            button {
                padding: 10px 20px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
            .result {
                margin-top: 20px;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Nth Largest Number Finder</h2>
            <p>Enter a list of comma-separated numbers and choose which largest number (N) you want to find.</p>
            <form method="POST">
                <label>Enter numbers (comma-separated):</label>
                <input type="text" name="numbers" required placeholder="e.g., 10, 50, 20, 5, 100">
                
                <label>Enter N:</label>
                <input type="number" name="n" required placeholder="e.g., 2">
                
                <button type="submit">Find Nth Largest</button>
            </form>
            <div class="result">{{ result|safe }}</div>
        </div>
    </body>
    </html>
    """, result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host="0.0.0.0", port=port)
