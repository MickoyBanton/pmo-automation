import { useEffect, useState } from "react";
import { getFullReport } from "../services/api";
import Header from "../components/Header";
import MetricsCards from "../components/MetricsCards";
import IssuesList from "../components/IssuesList";
import TasksTable from "../components/TasksTable";

export default function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    getFullReport(1).then(setData);
  }, []);

  if (!data) return <p>Loading...</p>;

  return (
    <div className="container mt-4">
      <Header data={data} />
      <MetricsCards report={data.report} />
      <IssuesList audit={data.audit} />
      <TasksTable />
    </div>
  );
}