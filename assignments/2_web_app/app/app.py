#!/usr/bin/python
#
# CS162 Assignment 2 - Web Application
# author: Austin Perzben
# created: 2021-03-24 | 21:45:27

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

kanban = Flask(__name__)

kanban.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kanban.db"

db = SQLAlchemy(kanban)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String(250))
    panel = db.Column(db.String())


@kanban.route("/", methods=["GET", "POST"])
def index():
    todos = Task.query.filter_by(panel='todo')
    doings = Task.query.filter_by(panel='doing')
    dones = Task.query.filter_by(panel='done')
    return render_template("index.html", todos=todos, doings=doings, dones=dones, task=None)


@kanban.route("/new_task", methods=["GET", "POST"])
def new_task():
    if request.method == "POST":
        task = Task(
            title=request.form['title'], content=request.form['content'], panel=request.form['panel'])
        db.session.add(task)
        db.session.commit()

    return redirect(url_for('index'))


@kanban.route("/del_task", methods=["POST"])
def del_task():
    task_id = request.form['task_id']
    # print(task_id)
    task = Task.query.filter_by(id=task_id)
    task.delete()
    db.session.commit()
    return redirect(url_for('index'))


@kanban.route("/move_task", methods=["POST"])
def move_task():
    task_id = request.form['task_id']
    task = Task.query.filter_by(id=task_id).first_or_404()
    task.panel = request.form['panel']
    db.session.add(task)
    db.session.commit()
    print(task.panel)

    return redirect(url_for('index'))

# @kanban.route("/edit_task/<task_id>", methods=["GET", "POST"])
# def edit_task(task_id):
#     task = Task.query.filter_by(id=task_id).first_or_404()

#     return redirect(url_for('index'),
#                     task=task)


@kanban.route("/notImplemented/<prev>", methods=["GET", "POST"])
def notImplemented(prev):
    return f"<h1>Not Implemented!</h1><p>{prev}</p>"


if __name__ == "__main__":
    kanban.run(debug=True)
