import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    work_experiences = [
        {
            "company": "AuriStor",
            "description": "- Developed a Go backend server aimed to query over 70+ server statistics to monitor and display performance and server health using Prometheus and a Grafana dashboard",
            "description2": "- Worked on a frontend dashboard using React.js and TypeScript to display user's information about their AFS cells and volumes, allowing for ease of use and access compared to querying from a Linux backend via CLI",
            "image": "auristor.jpeg"
        },
        {
            "company": "Movement Vault",
            "description": "Currently, I'm programming in Swift developing an iOS application aimed at providing users the ability to scan product barcodes to learn more about the dangerous ingredients to avoid. Programming in Swift is quite different, but also an enjoyable experience being able to tackle and learn a new programming language.",
            "image": "movementvault.svg"
        }
    ]

    hobbies = [
        {
            "description": "I used to play video games very passionately, and was one of the things that ate a lot of my time during my childhood, especially during quarantine...",
            "image1": "minecraft.avif",
            "image2": "roblox.png",
            "image3": "valorant.webp",
        },
        {
            "description": "When I decide to get some sunglight occasionally, I like to go play some pickup basketball with friends at my local park!",
            "image1": "lebron.jpeg",
            "image2": "basketball.jpeg",
            "image3": "anotherimage.jpeg"
        },
        {
            "description": "I also just like hanging out with friends, family and loved ones!",
            "image1": "pic1.jpeg",
            "image2": "rockclimbing.jpeg",
            "image3": "cousin.jpeg",
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

    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), work_experiences=work_experiences, hobbies=hobbies, education=education)

