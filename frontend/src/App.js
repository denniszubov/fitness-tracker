import React from 'react';
import RunsList from './Runs';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Routes>
      <Route path="run/" element={<RunsList />} />
    </Routes>
  );
}

export default App;
