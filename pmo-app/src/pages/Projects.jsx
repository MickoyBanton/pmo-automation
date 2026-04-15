import { useEffect, useState } from "react";
import { getProjects } from "../services/api";
import { useNavigate } from "react-router-dom";

export default function Projects() {
  const [projects, setProjects] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    getProjects().then(setProjects);
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4 text-center">Projects</h2>

      <div className="list-group">
        {projects.map((p) => (
          <button
            key={p.id}
            className="list-group-item list-group-item-action"
            onClick={() => navigate(`/project/${p.id}`)}
          >
            <strong>{p.name}</strong> — {p.owner}
          </button>
        ))}
      </div>
    </div>
  );
}