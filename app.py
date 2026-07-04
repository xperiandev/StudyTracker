# Modules
from cs50 import SQL
from datetime import datetime
from flask import Flask, send_file, redirect, request, render_template
import io
import time

# Application
app = Flask(__name__)

# Database
db = SQL("sqlite:///database.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", user="dummy", streak=0)

logText = []
logText.append(f"{datetime.now().replace(microsecond=0)}: log initiated")
@app.route("/logs", methods=["GET", "POST"])
def logs():
    if request.method == "POST":
        if request.form.get("submit"):
            logValue = request.form.get("log")
            logText.append(f"{datetime.now().replace(microsecond=0)}: {logValue}")

        elif request.form.get("clear"):
            logText.clear()
            logText.append(f"{datetime.now().replace(microsecond=0)}: log initiated")

        elif request.form.get("export"):
            time = datetime.now().replace(microsecond=0)
            time = time.strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{time}-log-export.txt"

            data = io.BytesIO()
            content = "\n".join(logText)
            data.write(content.encode("utf-8"))
            data.seek(0)

            return send_file(
                data,
                mimetype='text/plain',
                as_attachment=True,
                download_name=filename
            )

        return render_template("logs.html", logText=logText)
    else:
        return render_template("logs.html", logText=logText)


@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        task = request.form.get("task")
        status = "uncomplete"

        if not task:
            return render_template("apology.html", message="Insert the task")

        db.execute("INSERT INTO tasks (task, status, timestamp) VALUES (?, ?, ?)",
                    task, status, datetime.now().replace(microsecond=0))

        return redirect("/tasks")
    else:
        tasks = db.execute("SELECT * FROM tasks WHERE status = ?", "uncomplete")
        completed = db.execute("SELECT * FROM tasks WHERE status = ?", "completed")

        tableData = []
        for data in tasks:
            id = data["id"]
            task = data["task"]
            status = data["status"]
            timestamp = data["timestamp"]

            tableData.append({
                "id": id,
                "task": task,
                "status": status,
                "timestamp": timestamp
            })

        tableCompleted = []
        for data in completed:
            id = data["id"]
            task = data["task"]
            status = data["status"]
            timestamp = data["timestamp"]

            tableCompleted.append({
                "id": id,
                "task": task,
                "status": status,
                "timestamp": timestamp
            })

        return render_template("tasks.html", tableData=tableData, tableCompleted=tableCompleted)


@app.route("/tasks/check", methods=["POST"])
def tasks_check():
    id = request.form.get("id")

    if not id:
        return render_template("apology.html", message="Unable to Complete")

    if not id.isnumeric():
        return render_template("apology.html", message="Unable to Complete")

    db.execute("UPDATE tasks SET status = ? WHERE id = ?", "completed", id)
    return redirect("/tasks")


@app.route("/tasks/delete", methods=["POST"])
def tasks_delete():
    id = request.form.get("id")

    if not id:
        return render_template("apology.html", message="Unable to delete")

    if not id.isnumeric():
        return render_template("apology.html", message="Unable to delete")

    db.execute("DELETE FROM tasks WHERE id = ?", id)
    return redirect("/tasks")


@app.route("/timer", methods=["POST", "GET"])
def timer():
    if request.method == "POST":
        hour = request.form.get("hour")
        minute = request.form.get("minute")
        second = request.form.get("second")

        if not hour:
            return render_template("apology.html", message="Input valid time (hour)")
        if not minute:
            return render_template("apology.html", message="Input valid time (minute)")
        if not second:
            return render_template("apology.html", message="Input valid time (second)")

        try:
            hour = int(hour)
        except ValueError:
            return render_template("apology.html", message="Invalid hour")
        try:
            minute = int(minute)
        except ValueError:
            return render_template("apology.html", message="Invalid minute")
        try:
            second = int(second)
        except ValueError:
            return render_template("apology.html", message="Invalid second")

        if not hour >= 0:
            return render_template("apology.html", message="Input valid time (hour)")
        if not minute >= 0 and minute <= 59:
            return render_template("apology.html", message="Input valid time (minute)")
        if not second >= 0 and second <= 59:
            return render_template("apology.html", message="Input valid time (second)")

        hour = "0" + str(hour) if hour < 10 else hour
        minute = "0" + str(minute) if minute < 10 else minute
        second = "0" + str(second) if second < 10 else second

        return render_template("timer.html", hour=hour, minute=minute, second=second)
    else:
        return render_template("timer.html", hour="00", minute="00", second="00")
