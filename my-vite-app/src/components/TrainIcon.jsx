import React from "react";

export default function TrainIcon({ position }) {
  const xStart = 100;
  const xEnd = 500;
  const y = 150;

  // Linear interpolation: 0 → start, 1 → end
  const x = xStart + (xEnd - xStart) * position;

  return <circle cx={x} cy={y} r="10" fill="red" />;
}
