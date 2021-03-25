#!/usr/bin/python
#
# CS162 Assignment 2 - Web Application
# author: Austin Perzben
# created: 2021-03-24 | 21:45:27

from flask import Flask, render_template
import requests

kanban = Flask(__name__)


@kanban.route('/')
def index():
    return render_template("index.html")


@kanban.route('/example', methods=['GET', 'POST'])
def example():
    return render_template("example.html")


if __name__ == "__main__":
    kanban.run()
