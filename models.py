from extensions import db

class Project(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    owner = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    tasks = db.relationship("Task", backref="project", lazy=True)
    risks = db.relationship("Risk", backref="project", lazy=True)


class Task(db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    name = db.Column(db.String(100))
    status = db.Column(db.String(50))
    deadline = db.Column(db.Date)


class Risk(db.Model):
    __tablename__ = "risk"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    description = db.Column(db.String(255))
    severity = db.Column(db.String(50))