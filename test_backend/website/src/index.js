

import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from "./App";
import './index.css';
import { Login, Logout } from './views/auth';
import SignupPage from './pages/signup/SignupPage';
import LoginPage from './pages/login/LoginPage';
import SignupPageOne from './pages/signup/SignupPageOne';


const rootElement = document.getElementById("root");
ReactDOM.render(
  <BrowserRouter>
  <Routes>
    <Route path="/" element={<App />} />
    <Route path="login" element={<LoginPage />} />
    <Route path="signup" element={<SignupPage />} />
    <Route path="signup1" element={<SignupPageOne />} />
    <Route path="logout" element={<Logout />} />
  </Routes>
  </BrowserRouter>,
  rootElement
);
