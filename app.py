from flask import Flask, request, render_template_string
import pandas as pd

app = Flask(__name__)

# Load your CSV file
df = pd.read_csv("materials.csv")

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Study Recommender</title>
    <style>
    body {
        background-color: #40E0D0; /* turquoise */
        color: #222;
        font-family: Arial;
        text-align: center;
        padding: 50px;
    }

    h1 {
        color: #ff69b4; /* pink */
        text-shadow: 2px 2px 8px rgba(255,105,180,0.5);
    }

    input {
        padding: 10px;
        width: 250px;
        border-radius: 8px;
        border: none;
        outline: none;
    }

    button {
        padding: 10px 20px;
        background-color: #ff69b4; /* pink button */
        border: none;
        color: white;
        border-radius: 8px;
        cursor: pointer;
        font-weight: bold;
    }

    .card {
        background: white;
        margin: 15px auto;
        padding: 15px;
        width: 60%;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    }

    .level {
        color: #ff1493; /* deeper pink */
        font-weight: bold;
    }
</style>
</head>
<body>

<h1>📚 Smart Study Roadmap</h1>

<form method="POST">
    <input name="subject" placeholder="Enter subject (python, ai, web)">
    <br><br>
    <button type="submit">Show Roadmap</button>
</form>

{% for item in data %}
    <div class="card">
        <div class="level">Level {{item.level}}</div>
        <h3>{{item.topic}}</h3>
        <p>{{item.content}}</p>
    </div>
{% endfor %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    data = []

    if request.method == "POST":
        subject = request.form["subject"].lower()

        # filter subject
        filtered = df[df['subject'].str.lower() == subject]

        # sort by level (1 → 3)
        filtered = filtered.sort_values(by="level")

        data = filtered.to_dict(orient="records")

    return render_template_string(HTML, data=data)


app.run(debug=True)