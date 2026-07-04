# Study Tracker
### Track your study sessions effectively

## Uses:
- Flask for Backend
- SQL (sqlite3) for database
- HTML, CSS, JS, Python
- and some python modules

## Features:
- Logger: to log everything you do
- ToDo: include and check tasks of as you go
- Timer: a simple timer (you can however use it as a Pomodoro, but that functionality isn't built in, yet™)
###### for a guide on how to use the Features check out the [how-to page](./how-to.md)
---

## A short explaination of the features:

### Logger:
Logger, is used to log everything you do in the study session, please note that logs are temporary, they don't get stored in database and they might disappear, exporting would give you a .txt file of the said logs.

##### Examples:
```
> completed chapter 1
> taking break
> came back
```

### ToDo:
Just a simple ToDo program built with Flask and SQL, it remembers all the tasks in the database. 


### Timer:
"Timer" is a simple timer program with JS for the timer logic.

---

### Running locally:

1. Clone the repo
```bash
git clone https://github.com/xperiandev/StudyTracker
```

2. Install the [requirements](./requirements.txt) (create a virtual environment if needed)
```bash
pip install -r requirements.txt
```

3. Run the program using Flask
```bash
flask run --debug
```

---

#### File structure:
```
StudyTracker/
    static/
        images/
            background.jpg
            favicon.ico
        style.css
    templates/
        apology.html
        dashboard.html
        index.html
        layout.html
        logs.html
        tasks.html
        timer.html
    app.py
    credits.md
    database.db
    README.md
    requirements.txt
```

---
## License:

Licensed under [GPLv3](choosealicense.com/licenses/gpl-3.0/)
