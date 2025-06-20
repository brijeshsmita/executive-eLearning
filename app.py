from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data
user_name = "Rachel"
daily_focus = "Here's our leadership focus today..."
meetings = [
    {"time": "10:00 AM", "title": "Meet the CFO"},
    {"time": "01:00 PM", "title": "Leadership Forum"},
    {"time": "04:00 PM", "title": "1:1 with Lisa Wang"}
]
team_snapshot = [
    {"name": "Alex Patel", "status": "✅ Negotiation course completed"},
    {"name": "Sam Jones", "status": "⚠️ Low engagement"},
    {"name": "Lisa Meir", "status": "🎉 Birthday"}
]
recap = {
    "wins": [
        "Successful leadership presentation",
        "Carved out time for mentoring a peer"
    ],
    "challenges": [
        "Scheduled a follow-up meeting to proceed with your sales strategy next quarter"
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    coach_response = ""
    if request.method == "POST":
        user_input = request.form.get("coach_input")
        coach_response = f"Google AI Coach says: Great question, {user_name}! Let's explore: '{user_input}'"
    return render_template("index.html",
                           user_name=user_name,
                           daily_focus=daily_focus,
                           meetings=meetings,
                           team_snapshot=team_snapshot,
                           recap=recap,
                           coach_response=coach_response)

if __name__ == "__main__":
    app.run(debug=True,port=5050)
