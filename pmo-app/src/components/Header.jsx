export default function Header({ data }) {
  const getStatusColor = () => {
    if (data.status === "Healthy") return "green";
    if (data.status === "At Risk") return "orange";
    return "red";
  };

  return (
    <div className="card p-3 mb-3">
      <h3>{data.project}</h3>
      <p>
        Status: <span style={{ color: getStatusColor() }}>{data.status}</span>
      </p>
      <p>Compliance Score: {data.audit.compliance_score}%</p>
    </div>
  );
}