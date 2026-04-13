class Project:
    def __init__(self, id, name, owner, start_date, end_date):
        self.id = id
        self.name = name
        self.owner = owner
        self.start_date = start_date
        self.end_date = end_date


class Task:
    def __init__(self, id, project_id, name, status, deadline):
        self.id = id
        self.project_id = project_id
        self.name = name
        self.status = status
        self.deadline = deadline


class Risk:
    def __init__(self, id, project_id, description, severity):
        self.id = id
        self.project_id = project_id
        self.description = description
        self.severity = severity