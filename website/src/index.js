import React from 'react';
import { render } from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from "./App";
import './index.css';
import { Login, Logout } from './views/auth';
import SignupPage from './pages/signup/SignupPage';
import LoginPage from './pages/login/LoginPage';

const rootElement = document.getElementById("root");
render(
  <BrowserRouter>
  <Routes>
    <Route path="/" element={<App />} />
    <Route path="login" element={<LoginPage />} />
    <Route path="signup" element={<SignupPage />} />
    <Route path="logout" element={<Logout />} />
  
  </Routes>
  </BrowserRouter>,
  rootElement
);