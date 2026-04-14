from app import create_app
from extensions import db
from models import Project, Task, Risk
from datetime import date

app = create_app()

with app.app_context():
    project = Project(
        name="Website Upgrade",
        owner="Alice",
        start_date=date(2026, 4, 1),
        end_date=date(2026, 5, 1)
    )

    db.session.add(project)
    db.session.commit()

    tasks = [
        Task(project_id=project.id, name="Design UI", status="done", deadline=date(2026, 4, 5)),
        Task(project_id=project.id, name="Build Backend", status="in_progress", deadline=date(2026, 4, 10)),
        Task(project_id=project.id, name="Testing", status="todo", deadline=date(2026, 4, 8))
    ]

    db.session.add_all(tasks)
    db.session.commit()

    print("Seeded!")