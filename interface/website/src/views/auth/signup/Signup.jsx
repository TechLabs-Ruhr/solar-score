
import React, { useState, useEffect } from 'react';
import './signup.css';

const Signup = () => {
  const [name, setName] = useState('');
  const [address, setAddress] = useState('');
  const [pv, setPv] = useState('');
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password1, setPassword1] = useState('');
  const [password2, setPassword2] = useState('');
  const [errors, setErrors] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (localStorage.getItem('token') !== null) {
      window.location.replace('http://localhost:3000/dashboard');
    } else {
      setLoading(false);
    }
  }, []);

  const onSubmit = e => {
    e.preventDefault();

    const user = {
      name: name, 
      address: address,
      pv: pv,
      username: username,
      email: email,
      password1: password1,
      password2: password2
    };

    fetch('http://127.0.0.1:8000/api/v1/users/auth/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(user)
    })
      .then(res => res.json())
      .then(data => {
        if (data.key) {
          localStorage.clear();
          localStorage.setItem('token', data.key);
          window.location.replace('http://localhost:3000/dashboard');
        } else {
          setName('');
          setAddress('');
          setPv('');
          setUsername('');
          setEmail('');
          setPassword1('');
          setPassword2('');
          localStorage.clear();
          setErrors(true);
        }
      });
  };

  return (
    <div className="solarscore__signup solarscore__signup-content">
      {loading === false && <h1 className="gradient__text">Sign Up here</h1>}
      {errors === true && <h2>Make sure you use a valid e-mail address and a password with more than 8 characters and contains a combination of digits text and special signs.</h2>}
      <form onSubmit={onSubmit}>
        <label className="solarscore__label" htmlFor='name'>Name:</label><br />
        <input className="solarscore__signup-messagebox"
          name='name'
          type='text'
          value={name}
          onChange={e => setName(e.target.value)}
          required
        />{' '}
        <br />
        <label className="solarscore__label" htmlFor='address'>Address:</label><br />
        <input className="solarscore__signup-messagebox"
          name ='address'
          type='text'
          value={address}
          onChange={e => setAddress(e.target.value)}
          required
        />{' '}
        <br />
        <label className="solarscore__label" htmlFor='pv'>PV max kW/h:</label><br />
        <input className="solarscore__signup-messagebox"
          name='pv'
          type='text'
          value={pv}
          onChange={e => setPv(e.target.value)}
          required
        />{' '}
        <br />
        <label className="solarscore__label" htmlFor='email'>Email address:</label><br />
        <input className="solarscore__signup-messagebox"
          name='email'
          type='email'
          value={email}
          onChange={e => setEmail(e.target.value)}
          required
        />{' '}
        <br />
        <label className="solarscore__label" htmlFor='username'>Username:</label><br />
        <input className="solarscore__signup-messagebox"
          name='username'
          type='text'
          value={username}
          onChange={e => setUsername(e.target.value)}
          required
        />{' '}
        <br />
        <label className="solarscore__label" htmlFor='password1'>Password:</label> <br />
        <input className="solarscore__signup-messagebox"
          name='password1'
          type='password'
          value={password1}
          onChange={e => setPassword1(e.target.value)}
          required
        />{' '}
        <br />
        <label className="solarscore__label" htmlFor='password2'>Confirm password:</label> <br />
        <input  className="solarscore__signup-messagebox"
          name='password2'
          type='password'
          value={password2}
          onChange={e => setPassword2(e.target.value)}
          required
        />{' '}
        <br />
        <input className="solarscore__signup-button" type='submit' value='Signup' />
      </form>
    </div>
  );
};

export default Signup;



