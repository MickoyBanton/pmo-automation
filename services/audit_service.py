from datetime import datetime

def run_audit(project, tasks, risks):
    issues = []
    today = datetime.today().date()

    # Project-level checks
    if not project.owner:
        issues.append("Project has no assigned owner")

    if project.end_date and project.end_date < today:
        incomplete_tasks = [t for t in tasks if t.status != "done"]
        if incomplete_tasks:
            issues.append("Project deadline passed but tasks are still incomplete")

    # Task-level checks
    for task in tasks:
        if not task.deadline:
            issues.append(f"Task '{task.name}' has no deadline")
        elif task.deadline < today and task.status != "done":
            issues.append(f"Task '{task.name}' is overdue")

    # Governance checks
    if len(tasks) == 0:
        issues.append("Project has no tasks defined")

    if len(risks) == 0:
        issues.append("No risks have been logged for this project")

    # Compliance Score
    total_checks = 5
    score = max(0, 100 - (len(issues) * (100 // total_checks)))

    return {
        "project": project.name,
        "compliance_score": score,
        "issue_count": len(issues),
        "issues": issues
    }