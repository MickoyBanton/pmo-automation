from flask import Blueprint, jsonify
from models import Project, Task, Risk
from services.audit_service import run_audit
from services.report_service import generate_project_report

project_bp = Blueprint("project_bp", __name__)


@project_bp.route("/projects", methods=["GET"])
def get_projects():
    projects = Project.query.all()

    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "owner": p.owner
        } for p in projects
    ])


@project_bp.route("/full-report/<int:project_id>", methods=["GET"])
def full_report(project_id):
    project = Project.query.get(project_id)

    if not project:
        return jsonify({"error": "Project not found"}), 404

    tasks = Task.query.filter_by(project_id=project_id).all()
    risks = Risk.query.filter_by(project_id=project_id).all()

    # 🔹 Report Data
    tasks_data = [
        {"status": t.status, "deadline": str(t.deadline)}
        for t in tasks
    ]
    risks_data = [{} for _ in risks]

    report = generate_project_report(
        {"name": project.name},
        tasks_data,
        risks_data
    )

    # 🔹 Audit Data
    audit = run_audit(project, tasks, risks)

    # 🔥 Combined Response
    return jsonify({
        "project": project.name,
        "report": report,
        "audit": audit
    })