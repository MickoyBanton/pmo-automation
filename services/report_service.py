from datetime import datetime

def generate_project_report(project, tasks, risks):
    total_tasks = len(tasks)
    completed_tasks = len([t for t in tasks if t["status"] == "done"])

    completion = (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    today = datetime.today().date()

    overdue_tasks = [
        t for t in tasks
        if datetime.strptime(t["deadline"], "%Y-%m-%d").date() < today
        and t["status"] != "done"
    ]

    return {
        "project": project["name"],
        "completion_percentage": round(completion, 2),
        "total_tasks": total_tasks,
        "overdue_tasks": len(overdue_tasks),
        "risk_count": len(risks)
    }