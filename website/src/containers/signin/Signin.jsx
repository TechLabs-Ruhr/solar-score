import React from 'react';
import './signin.css';
import { Signup, Login, Logout, Dashboard} from '../index';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Link } from 'react-router-dom';

const Signin = () => {
  return (<div className="solarscore__signin section__margin" id="signin">
    <Signup />
  </div>);
};

export default Signin;
