import React from 'react'
import {errorMessage, userInfo} from "../types"
import useFetch from '../useFetch'
import HeaderBar from './header'

function Main() {
    let credentials: string | null = localStorage.getItem("auth")
    let headers: any = credentials ? {"Authorization": "Bearer " + JSON.parse(credentials).access_token} : {}
    const {data, error, pending} = useFetch("/auth/me", {
        headers: headers
    })


    return (
        <div>
                <HeaderBar/>

                <h1 className='main-title'>Main Page</h1>
        </div>
    ) 
}

export default Main;
