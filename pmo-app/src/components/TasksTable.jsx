import { useEffect, useState } from "react";
import { getFullReport } from "../services/api";

export default function TasksTable() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    getFullReport(1).then(data => setTasks(data.tasks));
  }, []);

  const getStatusBadge = (status) => {
    if (status === "done") return "green";
    if (status === "in_progress") return "orange";
    return "red";
  };

  return (
    <div className="card p-3">
      <h4 style={{ textAlign: "center", marginBottom: "15px" }}>Tasks</h4>

      <table className="table table-bordered">
        <thead>
          <tr>
            <th style={{ textAlign: "center" }}>Name</th>
            <th style={{ textAlign: "center" }}>Status</th>
            <th style={{ textAlign: "center" }}>Deadline</th>
          </tr>
        </thead>

        <tbody>
          {tasks.map((t, i) => (
            <tr key={i}>
              <td style={{ textAlign: "center" }}>{t.name}</td>

              <td style={{ textAlign: "center", color: getStatusBadge(t.status) }}>
                {t.status}
              </td>

              <td style={{ textAlign: "center" }}>{t.deadline}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}