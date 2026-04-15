import { useNavigate } from "react-router-dom";

export default function ProjectCard({ project }) {
  const navigate = useNavigate();

  const getStatusColor = () => {
    if (project.status === "Healthy") return "success";
    if (project.status === "At Risk") return "warning";
    return "danger";
  };

  return (
    <div
      className="card p-3 shadow-sm h-100"
      style={{ cursor: "pointer" }}
      onClick={() => navigate(`/project/${project.id}`)}
    >
      <h5>{project.name}</h5>
      <p className="text-muted">Owner: {project.owner}</p>

      <span className={`badge bg-${getStatusColor()} mb-2`}>
        {project.status}
      </span>

      <p>Start Date: {project.start_date}</p>

      <small>
        End Date: {project.end_date}
      </small>
    </div>
  );
}