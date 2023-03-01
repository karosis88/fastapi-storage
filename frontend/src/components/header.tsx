import {Link} from "react-router-dom"
import React from 'react'


export default function HeaderBar() {
  return (
    <div className="header">
        <div className="title-wrapper">
            <Link to="/" className="title">Storage</Link>
        </div>
        <div className="links">
            <Link to="/login" className="login-link">Login</Link>
            <Link to="/signup" className="signup-link">Sign up</Link>
        </div>
    </div>
  )
}
