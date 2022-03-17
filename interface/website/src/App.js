import React from 'react';
import {Footer, Header, Signin} from './containers';
import {Navbar, Test, Test2} from './components';
import './App.css';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './views/auth/login/Login';
import Signup from './views/auth/signup/Signup';
import Logout from './views/auth/logout/Logout';
import Dashboard from './views/dashboard/Dashboard';

const App = () => {
  return (
    <div className="App">
     <div className="gradient__bg">
     <Navbar />
     </div>
      <div className="solarscore__flexheader gradient__bg section__margin">
      <Header />
      <Signin />
      </div>
      <Test />
      <Test2 />
      <Footer />
      <Router>
        <Navbar />
        <Routes>
          <Route path='/login' component={Login} exact />
          <Route path='/signup' component={Signup} exact />
          <Route path='/logout' component={Logout} exact />
          <Route path='/dashboard' component={Dashboard} exact />
        </Routes>
      </Router>

  </div>
  )
}; 
export default App;


