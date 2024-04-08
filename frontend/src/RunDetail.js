import React from 'react'
import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

export default function RunDetail() {
  const [runDetails, setRunDetails] = useState(null);
  const { "run-id": runId } = useParams();
  useEffect(() => {
    // Fetch run details
    const fetchRunDetails = async () => {
      try {
        const response = await fetch(`http://localhost:8000/api/run/${runId}/`);
        if (!response.ok) {
            throw new Error("Run details could not be fetched.");
          }
        const data = await response.json();
        setRunDetails(data);
      } catch (error) {
        console.error("Error fetching run details:", error);
        // Handle the error appropriately in your UI
      }
    };

    fetchRunDetails();
  }, [runId]);


  if (!runDetails) {
    return <div>Loading...</div>;
  }

  return (
    <>
    <h2>Run Details</h2>
    <p>Run ID: {runDetails.id}</p>
    <p>{runDetails.date}, {runDetails.distance_km} km, avg heart rate: {runDetails.average_heart_rate}</p>
    </>
  )
}
