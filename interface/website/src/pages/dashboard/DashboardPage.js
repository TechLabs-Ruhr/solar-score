import React from 'react';
import Dashboard from '../../views/dashboard/Dashboard';
import { Navbar, Footer } from '../../components';
import './dashboardpage.css';
import PowerTable from '../../components/core/Table';
import PowerChart from '../../components/core/Chart';

const DashboardPage = () => {
  return (
    <div className="Dashboard">
      <Navbar />
      <div className="section__margin">
        <Dashboard />
        <PowerChart />
        <PowerTable />
      </div>
      <Footer />
    </div>
  )
};

export default DashboardPage;
