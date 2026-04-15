export default function IssuesList({ audit }) {
  return (
    <div className="card p-3 mb-3">
      <h4>🚨 Issues Detected ({audit.issue_count})</h4>

      {audit.issues.length === 0 ? (
        <p>No issues 🎉</p>
      ) : (
        <ul className="list-unstyled">
          {audit.issues.map((issue, index) => (
            <li key={index} style={{ color: "red" }}>
              {issue}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}