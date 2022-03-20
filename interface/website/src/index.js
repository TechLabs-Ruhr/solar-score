

import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './index.css';
import LogoutPage from './pages/logout/LogoutPage';
import SignupPage from './pages/signup/SignupPage';
import LoginPage from './pages/login/LoginPage';
import DashboardPage from './pages/dashboard/DashboardPage';
import App from './App';


const rootElement = document.getElementById("root");
ReactDOM.render(
  <BrowserRouter>
  <Routes>
    <Route path="" element={<App />} />
    <Route path="login" element={<LoginPage />} />
    <Route path="signup" element={<SignupPage />} />
    <Route path="dashboard" element={<DashboardPage />} />
    <Route path="logout" element={<LogoutPage />} />
  </Routes>
  </BrowserRouter>,
  rootElement
);
