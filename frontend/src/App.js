import React from 'react';
import RunsList from './Runs';
import Navigation from './Navigation';
import { Routes, Route } from 'react-router-dom';
import "bootstrap/dist/css/bootstrap.min.css";
import ActivityList from './ActivityList';
import Home from './Home';
import RunDetail from './RunDetail';

function App() {
  return (
    <>
      <Navigation />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="activity-list/" element={<ActivityList />} />
        <Route path="run/">
          <Route index element={<RunsList />} />
          <Route path=":run-id" element={<RunDetail />} />
        </Route>
      </Routes>
    </>
  );
}

export default App;
