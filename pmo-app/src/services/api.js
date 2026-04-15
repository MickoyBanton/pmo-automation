const BASE_URL = "http://127.0.0.1:5000";

export const getFullReport = async (projectId) => {
  const res = await fetch(`${BASE_URL}/full-report/${projectId}`);
  return res.json();
};