export default function MetricsCards({ report }) {
  return (
    <div className="row mb-3">
      <div className="col">
        <div className="card p-3 text-center">
          <h5>Completion</h5>
          <h2>{report.completion_percentage}%</h2>
        </div>
      </div>

      <div className="col">
        <div className="card p-3 text-center">
          <h5>Overdue</h5>
          <h2>{report.overdue_tasks}</h2>
        </div>
      </div>

      <div className="col">
        <div className="card p-3 text-center">
          <h5>Total Tasks</h5>
          <h2>{report.total_tasks}</h2>
        </div>
      </div>

      <div className="col">
        <div className="card p-3 text-center">
          <h5>Risks</h5>
          <h2>{report.risk_count}</h2>
        </div>
      </div>
    </div>
  );
}