import React, {useState} from 'react';
import logo from '../../assets/logo.svg';
import './navbar.css';
import {RiMenu3Line, RiCloseLine} from 'react-icons/ri';

const Menu = () => (
  <>
  <p><a href="#home">Home</a></p>
   <p><a href="#about">About the Project</a></p>
   </>
)

const Navbar = () => {
  const [toggleMenu, setToggleMenu] = useState(false);
  return (
  <div className="solarscore__navbar">
  <div className="solarscore__navbar-links">
      <div className="solarscore__navbar-links-logo">
      <img src ={logo} alt = "logo" />
      </div>
        <div className="solarscore__navbar-links_container">
      <Menu/>
        </div>
  </div>
  <div className="solarscore__navbar-sign">
    <p>Sign in</p>
    <button type="button"> Sign Up</button>
  </div>
  <div className="solarscore__navbar-menu">
    {toggleMenu
      ? <RiCloseLine color="fff" size={27} onClick={()=> setToggleMenu(false)}/>
      : <RiMenu3Line color="fff" size={27} onClick={()=> setToggleMenu(true)}/>
    }
    {toggleMenu &&(
      <div className="solarscore__navbar-menu_container scale-up-center">
        <div className="solarscore__navbar-menu_container-links">
        <Menu/>
        </div>
        <div className="solarscore__navbar-menu_container-links-sign">
        <p>Sign in</p>
         <button type="button"> Sign Up</button>
         </div>
        </div>
       )}
    </div>
  </div>
  ); 
};

export default Navbar;
