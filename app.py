
from flask import Flask, request, render_template_string
import os
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def nth_largest():
    result = ""
    if request.method == "POST":
        try:
            nums = list(map(int, request.form["numbers"].split(",")))
            n = int(request.form["n"])
            nums.sort(reverse=True)
            result = f"{n}th largest number is: {nums[n-1]}"
        except:
            result = "Invalid input"
    return render_template_string("""
    <html><head><title>Nth Largest</title><style>
    body { font-family: Arial; margin: 40px; }
    input { margin: 5px; padding: 5px; }
    </style></head><body>
    <h2>Nth Largest Number Finder</h2>
    <form method="POST">
        List (comma-separated): <input name="numbers"><br>
        N: <input name="n" type="number"><br>
        <button type="submit">Find</button>
    </form>
    <p>{{ result }}</p>
    </body></html>
    """, result=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host="0.0.0.0", port=port)