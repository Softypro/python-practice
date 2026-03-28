Python Adventure Part 2: Building Your First Website
By: Your Computer Science Teacher

Welcome Back, Web Developer!
You've mastered the basics of Python—variables, loops, decisions, and even made a text-based game. Now it's time to take your skills to the internet! In this book, you'll learn how to build interactive websites that people can visit from anywhere in the world.

We'll start with Flask, a lightweight web framework that's perfect for beginners. Think of Flask as the engine that lets your Python code talk to a web browser.

Chapter 1: How Websites Work (The Big Picture)
Before we build, let's understand what happens when you visit a website.

text
Your Browser (Chrome/Safari)  <---->  Internet  <---->  A Server (Running Python)
You type a website address (like awesomegame.com) into your browser.

Your browser sends a request across the internet.

A server (a special computer) receives the request.

The server runs Python code (using Flask) to figure out what to send back.

The server sends back a response—usually an HTML page.

Your browser displays that page.

Flask's Job: To handle the requests, run your Python code, and generate the responses.

Chapter 2: Setting Up Your Web Workshop
We need to install Flask and organize our project.

Step 1: Install Flask
Open your terminal (Command Prompt on Windows, Terminal on Mac). Type this command:

bash
pip install flask
pip is Python's package installer. It downloads and installs extra tools (like Flask) that aren't included with basic Python.

Step 2: Create Your Project Folder
Create a new folder on your desktop called my_first_website. Inside it, create a file called app.py. This is where your main Python code will live.

Your folder should look like this:

text
my_first_website/
└── app.py
Chapter 3: Your First Flask Website
Let's build a website that says "Hello, World!" but this time, it will appear in your web browser.

Open app.py and type this:

python
from flask import Flask  # Import the Flask toolkit

# Create the Flask application object
app = Flask(__name__)

# This is a "route" - it connects a URL to a function
@app.route('/')
def home():
    return "Hello, World! This is my first website!"

# This tells the computer how to run the app
if __name__ == '__main__':
    app.run(debug=True)
What's happening here?

Code	What It Does
from flask import Flask	Imports the Flask framework
app = Flask(__name__)	Creates your web application
@app.route('/')	A decorator that says: "When someone visits the homepage ('/'), run the next function"
def home():	The function that runs when someone visits the homepage
return "..."	The text that gets sent to the browser
app.run(debug=True)	Starts the web server. debug=True means it automatically restarts when you change your code
Run Your Website!
Save app.py.

In your terminal, navigate to your project folder:

bash
cd Desktop/my_first_website
Run the file:

bash
python app.py
You'll see output like:

text
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Open your web browser and go to: http://127.0.0.1:5000/

You should see: "Hello, World! This is my first website!"

Congratulations! You just ran a web server from your own computer!

Chapter 4: Adding Multiple Pages (Routes)
A real website has many pages: Home, About, Contact, etc. Let's add more routes.

Update your app.py:

python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to My Site!</h1>
    <p>This is the homepage.</p>
    <a href="/about">About Me</a> | <a href="/fun_fact">Fun Fact</a>
    """

@app.route('/about')
def about():
    return """
    <h1>About Me</h1>
    <p>Hi! I'm a 7th grader who loves Python and building websites.</p>
    <a href="/">Back Home</a>
    """

@app.route('/fun_fact')
def fun_fact():
    return """
    <h1>Fun Fact</h1>
    <p>Did you know? The first website ever made is still online at info.cern.ch!</p>
    <a href="/">Back Home</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
Notice: We're returning HTML code now! The browser understands <h1> for headings, <p> for paragraphs, and <a href="..."> for links.

Your Turn: Add a new route called /hobby that displays your favorite hobby with a heading and description.

Chapter 5: Using HTML Templates
Putting HTML directly inside Python strings gets messy fast. Let's separate our design from our logic using templates.

Step 1: Create a Templates Folder
Inside my_first_website, create a new folder called templates. This is where Flask looks for HTML files.

Your folder structure:

text
my_first_website/
├── app.py
└── templates/
    └── (HTML files will go here)
Step 2: Create Your First Template
Inside the templates folder, create a file called home.html:

html
<!DOCTYPE html>
<html>
<head>
    <title>My Awesome Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #3366cc;
        }
        .button {
            background-color: #3366cc;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Welcome, {{ name }}!</h1>
    <p>You are visitor number {{ visit_count }}.</p>
    <a href="/about" class="button">Learn About Me</a>
</body>
</html>
What's {{ name }}? That's a placeholder. Flask will replace it with a value we send from Python!

Step 3: Update app.py to Use the Template
python
from flask import Flask, render_template

app = Flask(__name__)

# Let's create a simple counter
visit_counter = 0

@app.route('/')
def home():
    global visit_counter
    visit_counter += 1
    
    # Render the template and pass data to it
    return render_template('home.html', 
                          name="Python Explorer",
                          visit_count=visit_counter)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
Step 4: Create about.html
In your templates folder, create about.html:

html
<!DOCTYPE html>
<html>
<head>
    <title>About Me</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #3366cc;
        }
    </style>
</head>
<body>
    <h1>About Me</h1>
    <p>I'm a 7th grader who learned Python and built this website!</p>
    <p>I love coding because it lets me turn ideas into real things people can use.</p>
    <a href="/">← Back Home</a>
</body>
</html>
Now run it! Your website now has clean, separate HTML files and Python logic.

Chapter 6: Handling User Input (Forms)
Let's make our website interactive. We'll create a page where users can send you messages.

Step 1: Create a Form Template
Create templates/contact.html:

html
<!DOCTYPE html>
<html>
<head>
    <title>Contact Me</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
            padding: 50px;
        }
        input, textarea {
            padding: 10px;
            margin: 10px;
            width: 300px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        button {
            background-color: #3366cc;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .message {
            background-color: #d4edda;
            color: #155724;
            padding: 10px;
            border-radius: 5px;
            margin: 20px auto;
            width: 80%;
        }
    </style>
</head>
<body>
    <h1>Contact Me</h1>
    
    {% if message_sent %}
    <div class="message">
        Thanks, {{ name }}! Your message has been sent.
    </div>
    {% endif %}
    
    <form method="POST">
        <input type="text" name="name" placeholder="Your Name" required><br>
        <input type="email" name="email" placeholder="Your Email" required><br>
        <textarea name="message" placeholder="Your Message" rows="5" required></textarea><br>
        <button type="submit">Send Message</button>
    </form>
    
    <br>
    <a href="/">← Back Home</a>
</body>
</html>
Notice: {% if message_sent %} is a Jinja2 template tag. It lets us conditionally show parts of the HTML.

Step 2: Update app.py to Handle Form Data
Add this to your app.py:

python
from flask import Flask, render_template, request

# ... (keep your existing code) ...

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # This runs when the form is submitted
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # For now, just print it to the terminal
        print(f"New message from {name} ({email}): {message}")
        
        # Show the template with a success message
        return render_template('contact.html', 
                              message_sent=True,
                              name=name)
    
    # This runs when the user first visits the page (GET request)
    return render_template('contact.html', message_sent=False)
What's new?

methods=['GET', 'POST'] allows the route to handle both viewing the form (GET) and submitting it (POST)

request.form['name'] gets the data the user typed into the form

We pass message_sent to the template to show the success message

Chapter 7: Adding a Simple Game
Let's make a number guessing game on your website!

Create templates/game.html:

html
<!DOCTYPE html>
<html>
<head>
    <title>Number Guessing Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
            padding: 50px;
        }
        input {
            padding: 10px;
            font-size: 18px;
            width: 100px;
        }
        button {
            background-color: #3366cc;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .feedback {
            font-size: 24px;
            margin: 20px;
            padding: 20px;
            border-radius: 10px;
        }
        .correct {
            background-color: #d4edda;
            color: #155724;
        }
        .wrong {
            background-color: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <h1>Number Guessing Game</h1>
    <p>I'm thinking of a number between 1 and 20.</p>
    
    <form method="POST">
        <input type="number" name="guess" min="1" max="20" required>
        <button type="submit">Guess!</button>
    </form>
    
    {% if feedback %}
    <div class="feedback {{ 'correct' if correct else 'wrong' }}">
        {{ feedback }}
        {% if correct %}
        <br><br>
        <a href="/game">Play Again?</a>
        {% endif %}
    </div>
    {% endif %}
    
    <br>
    <a href="/">← Back Home</a>
</body>
</html>
Now add the game logic to app.py:

python
import random

# Add a new route for the game
@app.route('/game', methods=['GET', 'POST'])
def game():
    # We'll store the secret number in a special variable called a "session"
    # For now, let's use a simple approach without sessions
    if 'secret_number' not in game.__dict__:
        game.secret_number = random.randint(1, 20)
    
    if request.method == 'POST':
        guess = int(request.form['guess'])
        
        if guess == game.secret_number:
            feedback = f"Correct! {guess} was the number!"
            correct = True
            game.secret_number = random.randint(1, 20)  # New number for next game
        elif guess < game.secret_number:
            feedback = f"{guess} is too low! Try again."
            correct = False
        else:
            feedback = f"{guess} is too high! Try again."
            correct = False
        
        return render_template('game.html', 
                              feedback=feedback, 
                              correct=correct)
    
    return render_template('game.html', feedback=None, correct=False)
Chapter 8: Making Your Website Public
Right now, your website only works on your computer. To share it with the world, you need to deploy it.

Option 1: PythonAnywhere (Easiest for Beginners)
Go to pythonanywhere.com and create a free account.

Upload your app.py and templates folder.

They give you a free subdomain like yourname.pythonanywhere.com

Option 2: Replit (No Installation Needed)
Go to replit.com

Create a new "Flask" project

Copy your code and run it—Replit gives you a public URL instantly

Chapter 9: Leveling Up to Django
Flask is great for small projects. When you're ready to build bigger websites (like a blog, a social network, or an e-commerce site), Django is your next step.

What Django Adds:
Feature	What It Does
Database	Saves user accounts, posts, comments automatically
Admin Panel	A built-in interface to manage your data
User Authentication	Login, signup, passwords handled for you
Security	Protects against common web attacks
To start with Django:
bash
pip install django
django-admin startproject myproject
cd myproject
python manage.py runserver
Django has a steeper learning curve, but it's incredibly powerful. Start with the official Django tutorial when you're ready!

Chapter 10: Your Project Ideas
Here are some websites you can build with Flask:

Project	What You'll Learn
Personal Portfolio	Show your projects, add a contact form
Mad Libs Generator	Users fill in words, you generate a funny story
Quiz App	Multiple-choice questions with a score
Weather App	Use an API to show real weather data
To-Do List	Let users add and check off tasks
Digital Diary	Save entries to a file (or database)
Final Challenge: Build Your Own Website!
Your mission, should you choose to accept it:

Create a website with at least 3 different pages

Use at least one HTML template

Include a form that accepts user input

Add one interactive feature (like a game, quiz, or calculator)

Deploy it so a friend or family member can visit it

Congratulations!
Every professional programmer started exactly where you are now. They typed their first print("Hello, World!") and built from there. You've already done that—and so much more!

You are now a Web Developer. Go build something amazing and share it with the world!

Happy Coding,
Your Computer Science Teacher

Appendix: Quick Reference
Python Basics
Concept	Example
Print	print("Hello")
Variable	name = "Alex"
If Statement	if age >= 13:
For Loop	for i in range(5):
While Loop	while game_running:
List	fruits = ["apple", "banana"]
Function	def my_function():
Flask Commands
Command	Purpose
pip install flask	Install Flask
python app.py	Run your app
@app.route('/')	Create a route
render_template()	Load an HTML file
request.form['name']	Get form data
Useful Resources
Official Python Tutorial: docs.python.org

Flask Documentation: flask.palletsprojects.com

Django Documentation: djangoproject.com

W3Schools Python: w3schools.com/python

Replit: replit.com (code in your browser)

📁 GitHub Repository Structure Suggestion:

text
python-adventure-book/
├── README.md           # Overview of the book
├── part1-python-basics.md
├── part2-flask-websites.md
├── full-book.md        # This file
├── code-examples/
│   ├── hello.py
│   ├── adventure_game.py
│   └── flask_app/
│       ├── app.py
│       └── templates/
│           ├── home.html
│           ├── about.html
│           ├── contact.html
│           └── game.html
└── projects/
    └── (student project ideas and starter code)
License: Feel free to share, modify, and use this book to teach others! Knowledge is meant to be shared.

text

---

This Markdown file is ready to be saved as `README.md` or `python-adventure-book.md` and uploaded to GitHub. It features:

- **Proper heading hierarchy** (H1 for main title, H2 for chapters, H3 for sections)
- **Syntax-highlighted code blocks** with language identifiers
- **Clean tables** for quick reference
- **Organized structure** that's easy to navigate
- **A suggested repository structure** at the end
- **All formatting** that renders beautifully on GitHub

You can copy this entire content, save it as a `.md` file, and push it to your GitHub repository. It will display perfectly!


