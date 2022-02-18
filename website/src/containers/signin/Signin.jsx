import React from 'react';
import './signin.css';
import { Signup, Login, Logout, Dashboard} from '../index';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Link } from 'react-router-dom';

const Signin = () => {
  return (<div className="solarscore__signin section__margin" id="signin">
    <div className="solarscore__signin-content">
        <h1 className="gradient__text">Sign Up here</h1>
    </div>
    <Router>
    <div className="solarscore__navbar-sign">
              <p><Link to='/login'>Login</Link></p>
            </div>
            <div className="solarscore__navbar-sign">
              <Link to='/signup'>
              <button type="button">Sign Up</button>
              </Link>
            </div>
    <Routes>
          <Route path='/login' element={<Login/>} />
          <Route path='/signup' element={<Signup/>}/>
          <Route path='/logout' element={<Logout/>} />
          <Route path='/dashboard' element={<Dashboard/>} />
        </Routes>
      </Router>
  </div>);
};

export default Signin;
