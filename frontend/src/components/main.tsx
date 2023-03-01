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
                {pending && <div>Loading...</div>}
                {!pending && data &&<div>Loged in as {data.username}</div>}
                {error && <div>Loged in as Anonymous</div>}
        </div>
    ) 
}

export default Main;
