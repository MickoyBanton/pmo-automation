export default function TasksTable({ tasks }) {
  return (
    <div className="card p-3">
      <h4 className="text-center mb-3">Tasks</h4>

      <table className="table table-bordered">
        <thead>
          <tr>
            <th className="text-center">Name</th>
            <th className="text-center">Status</th>
            <th className="text-center">Deadline</th>
          </tr>
        </thead>

        <tbody>
          {tasks.map((t, i) => (
            <tr key={i}>
              <td className="text-center">{t.name}</td>
              <td className="text-center">{t.status}</td>
              <td className="text-center">{t.deadline}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}