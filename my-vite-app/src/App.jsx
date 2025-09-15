import React from "react";
import MapView from "./components/MapView";

export default function App() {
  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>🚆 Train Traffic Dashboard</h1>
      <MapView />
    </div>
  );
}
