import React, { useState, useEffect, Fragment } from 'react';
import './logout.css'

const Logout = () => {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (localStorage.getItem('token') == null) {
      window.location.replace('http://localhost:3000/login');
    } else {
      setLoading(false);
    }
  }, []);

  const handleLogout = e => {
    e.preventDefault();

    fetch('http://127.0.0.1:8000/api/v1/users/auth/logout/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${localStorage.getItem('token')}`
      }
    })
      .then(res => res.json())
      .then(data => {
        console.log(data);
        localStorage.clear();
        window.location.replace('http://localhost:3000/login');
      });
  };

  return (
    <div>
      {loading === false && (
        <Fragment>
          <div className="solarscore__logout">
          <div className="solarscore__logout-content">
            <h1>Are you sure you want to logout?</h1>
            <input className="solarscore__logout-button" type='button' value='Logout' onClick={handleLogout} />
          </div>
          </div>
        </Fragment>
      )}
    </div>
  );
};

export default Logout;
