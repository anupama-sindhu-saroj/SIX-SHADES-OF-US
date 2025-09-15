import React, { useEffect, useState } from "react";
import TrainIcon from "./TrainIcon";

export default function MapView() {
  const [trains, setTrains] = useState([]);

  // Mock data until backend is ready
  useEffect(() => {
    const interval = setInterval(() => {
      setTrains([
        { id: "Train1", position: Math.random() }, // random position between 0-1
        { id: "Train2", position: Math.random() }
      ]);
    }, 1000); // update every 1 sec

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ marginTop: "20px" }}>
      <svg width="600" height="300" style={{ border: "1px solid black" }}>
        {/* Stations */}
        <circle cx="100" cy="150" r="15" fill="blue" />
        <text x="80" y="140" fill="black">Station A</text>

        <circle cx="500" cy="150" r="15" fill="green" />
        <text x="480" y="140" fill="black">Station B</text>

        {/* Track */}
        <line x1="100" y1="150" x2="500" y2="150" stroke="black" strokeWidth="3" />

        {/* Trains */}
        {trains.map((train) => (
          <TrainIcon key={train.id} position={train.position} />
        ))}
      </svg>
    </div>
  );
}

