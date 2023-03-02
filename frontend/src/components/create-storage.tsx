import React, { useEffect } from 'react'
import useFetch from '../useFetch'
import HeaderBar from './header'

export default function CreateStorage() {

    let credentials: string = localStorage.getItem('auth') as string
    let headers

    if (credentials)
        headers = {"Authorization": 'Bearer ' + JSON.parse(credentials).access_token}
    else
        headers = {}
    const {pending, error, data} = useFetch("/storage/info", {
        "headers" : headers
    })

    return (
        <div>
            <HeaderBar/>
            {pending && <div>Loading...</div>}
            {!pending && !error && <div>Storage was created</div>}
            {!error && <div>{error}</div>}
            
        </div>
    )
}
