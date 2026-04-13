from flask import Blueprint, jsonify
import json
from services.report_service import generate_project_report

project_bp = Blueprint("project_bp", __name__)

def load_data():
    with open("data/seed.json") as f:
        return json.load(f)


@project_bp.route("/projects", methods=["GET"])
def get_projects():
    data = load_data()
    return jsonify(data["projects"])


@project_bp.route("/report/<int:project_id>", methods=["GET"])
def get_report(project_id):
    data = load_data()

    project = next((p for p in data["projects"] if p["id"] == project_id), None)
    tasks = [t for t in data["tasks"] if t["project_id"] == project_id]
    risks = [r for r in data["risks"] if r["project_id"] == project_id]

    if not project:
        return jsonify({"error": "Project not found"}), 404

    report = generate_project_report(project, tasks, risks)
    return jsonify(report)

