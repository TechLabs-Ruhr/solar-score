import React from 'react';
import Dashboard from '../../views/dashboard/Dashboard';
import { Navbar, TestPrediction, Footer} from '../../components';
import './dashboardpage.css';

const DashboardPage = () => {
  return (
    <div className="Dashboard">
     <Navbar />
      <div className="section__margin">
      <Dashboard/>
      <TestPrediction />
      </div>
      <Footer />
  </div>
  )
};

export default DashboardPage;
