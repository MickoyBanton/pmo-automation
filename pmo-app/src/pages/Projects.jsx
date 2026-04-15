import { useEffect, useState } from "react";
import { getProjects } from "../services/api";
import ProjectCard from "../components/ProjectCard";

export default function Projects() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    getProjects().then(setProjects);
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="text-center mb-4">Projects</h2>

      <div className="row">
        {projects.map((p) => (
          <div className="col-md-4 mb-3" key={p.id}>
            <ProjectCard project={p} />
          </div>
        ))}
      </div>
    </div>
  );
}