from flask import Flask, jsonify, render_template
from flask_cors import CORS
import random

app = Flask(__name__)

# Enabling cors
CORS(app, resources={r"/*": {"origins": "*"}})

# List of sentences for typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed tests are a fun way to improve your typing.",
    "Programming in Python can be very enjoyable.",
    "Practice typing to increase your typing speed.",
    "Coding challenges can help sharpen your problem-solving skills.",
    "JavaScript is a versatile language used for both frontend and backend development.",
    "The Java programming language is known for its portability and security features.",
    "Python is a popular language for web development, data science, and machine learning.",
    "Spring Boot makes it easy to create stand-alone, production-grade Spring-based applications.",
    "Node.js is built on the V8 JavaScript engine and allows you to build scalable applications.",
    "Express.js is a lightweight web framework that helps build fast and secure applications with Node.js.",
    "SQL is essential for managing and manipulating relational databases.",
    "Laravel is a PHP framework that makes web development easy and enjoyable.",
    "TypeScript is a superset of JavaScript that adds static typing for better code quality.",
    "Asynchronous programming in JavaScript allows for better performance in web applications.",
    "RESTful APIs are widely used in web development to enable communication between different systems.",
    "Spring Boot supports microservices architecture and helps create cloud-native applications.",
    "JavaScript closures are powerful tools for creating private variables and functions.",
    "Node.js uses non-blocking I/O to handle requests in a highly efficient manner.",
    "Writing unit tests for your code ensures that it behaves as expected and helps with debugging.",
    "SQL joins allow you to combine data from multiple tables for more complex queries.",
    "In Laravel, Eloquent ORM provides an easy-to-use way to interact with your database using models.",
    "TypeScript's strict mode catches errors early during development, improving reliability."
]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-sentence")
def get_sentence():
    # Send a random sentence from the list
    sentence = random.choice(sentences)
    return jsonify({"sentence": sentence})

if __name__ == "__main__":
    app.run(debug=True)
