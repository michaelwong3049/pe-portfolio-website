import os
import datetime

from flask import Flask, render_template, request
from dotenv import load_dotenv

from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), host=os.getenv("MYSQL_HOST"), port=3306)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    work_experiences = [
        {
            "introduction": "I previously worked at as a software engineer intern. Here, I was able to work on two projects:",
            "company": "AuriStor",
            "description": "- Developed a Go backend server aimed to query over 70+ server statistics to monitor and display performance and server health using Prometheus and a Grafana dashboard",
            "description2": "- Worked on a frontend dashboard using React.js and TypeScript to display user's information about their AFS cells and volumes, allowing for ease of use and access compared to querying from a Linux backend via CLI",
            "image": "auristor.jpeg"
        },
        {
            "introduction": "I'm currently interning at Movement Vault as a software engineer intern on iOS developmenet!",
            "company": "Movement Vault",
            "description": "Currently, I'm programming in Swift developing an iOS application aimed at providing users the ability to scan product barcodes to learn more about the dangerous ingredients to avoid. Programming in Swift is quite different, but also an enjoyable experience being able to tackle and learn a new programming language.",
            "image": "movementvault.svg"
        }
    ]

    education = [
        {
            "school": "CUNY Hunter College",
            "description": "By being able to still live at home with my family, as well as having loads of opportunities by going to school in the heart of New York City, I find to love it here!",
            "image1": "hunter.jpg",
            "image2": "hunterlogo.png",
            "image3": "hawks.png"
        },
        {
            "school": "Midwood High School",
            "description": "I just recently graduated from Midwood last year, and created amazing friends and had great memories here!",
            "image1": "fieldday.jpeg",
            "image2": "graduation1.jpeg",
            "image3": "graduation2.jpeg"
        }
    ]

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), work_experiences=work_experiences, education=education)


@app.route('/hobbies')
def hobbies():
    hobbies = [
        {
            "description": "I used to play video games very passionately, and was one of the things that ate a lot of my time during my childhood, especially during quarantine...",
            "image1": "minecraft.avif",
            "image2": "valorant.webp",
            "image3": "roblox.png",
        },
        {
            "description": "When I decide to get some sunglight occasionally, I like to go play some pickup basketball with friends at my local park!",
            "image1": "lebron.jpeg",
            "image2": "basketball.webp",
        },
        {
            "description": "I also just like hanging out with friends, family and loved ones!",
            "image1": "pic1.jpeg",
            "image2": "rockclimbing.jpeg",
            "image3": "cousin.jpeg",
        }
    ]

    return render_template("hobbies.html", hobbies=hobbies)

@app.route("/timeline")
def timeline():
    timeline_posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return render_template(
        "timeline.html",
        title="Timeline",
        timeline_posts=timeline_posts
    )

@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

