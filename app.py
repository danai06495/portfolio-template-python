from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    profile = {
        "name": "Name",
        "title": "Full-Stack Developer",
        "bio": "Passionate about building digital experiences with modern technologies.",
        "skills": ["Python", "JavaScript", "React", "SQL", "FastAPI"],
        "projects": [
            {"name": "Inventory Manager", "desc": "Backend with FastAPI and PostgreSQL"},
            {"name": "Travel Booking Site", "desc": "Frontend with React and Firebase"}
        ],
        "contacts": {
            "email": "you@example.com",
            "linkedin": "https://linkedin.com/in/yourname",
            "github": "https://github.com/yourname"
        }
    }
    return render_template("index.html", profile=profile)

if __name__ == "__main__":
    app.run(debug=True)
