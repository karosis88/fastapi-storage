import {Link} from "react-router-dom"
import React from 'react'
import useFetch from "../useFetch"


export default function HeaderBar() {

  let credentials: string = localStorage.getItem("auth") as string
  let headers: any = credentials ? {"Authorization": "Bearer " + JSON.parse(credentials).access_token} : {}
  const {data, error, pending} = useFetch("/auth/me", {
      headers: headers
  })

  return (
    <div className="header">
        <div className="title-wrapper">
            <Link to="/" className="title">Storagik</Link>
        </div>
        <div className="links">
            {!credentials &&
            <Link to="/login" className="login-link">Login</Link>}
            {!credentials &&
            <Link to="/signup" className="signup-link">Sign up</Link>}
            {credentials &&
            <Link to="/upload" className="upload-link">Upload</Link>}
            {credentials &&
            <Link to="/files" className="upload-link">Files</Link>}
            {data && !pending && !error &&
            <Link to="/create-storage" className="upload-link">Storage</Link>}
            {data && !pending && !error &&
            <Link to="/files" className="upload-link">{data.username}</Link>}
        </div>
    </div>
  )
}
