import React, { useState, useEffect } from 'react';

const RunsList = () => {
  const [runs, setRuns] = useState([]);

  useEffect(() => {
    // Function to fetch runs
    const fetchRuns = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/run/');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setRuns(data); // Set the runs in state
      } catch (error) {
        console.error("Could not fetch runs:", error);
      }
    };

    fetchRuns(); // Call the function to fetch runs
  }, []); // Empty dependency array means this effect runs once on mount

  return (
    <div>
      <h2>Runs</h2>
      <ul>
        {runs.map(run => (
          <li key={run.id}>
            {run.date}, {run.distance_km} km, avg heart rate: {run.average_heart_rate} with id: {run.id}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RunsList;
