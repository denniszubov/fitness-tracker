import React from 'react';
import RunsList from './Runs';
import Navigation from './Navigation';
import { Routes, Route } from 'react-router-dom';
import "bootstrap/dist/css/bootstrap.min.css";
import ActivityList from './ActivityList';
import Home from './Home';

function App() {
  return (
    <>
      <Navigation />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="activity-list/" element={<ActivityList />} />
        <Route path="run/" element={<RunsList />} />
      </Routes>
    </>
  );
}

export default App;
