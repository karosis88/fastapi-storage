import React, { useEffect } from 'react'
import useFetch from '../useFetch'
import HeaderBar from './header'
import FileRow from "./filerow"

export default function Files() {

    let credentials: string = localStorage.getItem('auth') as string
    let headers

    if (credentials)
        headers = {
            "Authorization" : "Bearer " + JSON.parse(credentials).access_token 
        }
    else
        headers = {}

    const {data, error, pending, setData} = useFetch("/storage/files", {headers: headers})
    return (
        <div>
            <HeaderBar/>
            {pending && <div>Loading files...</div>}
            {error &&  <div>{error}</div>}
            {data && <div className="filewrapper">
                <div className="filestitle">Files</div>
                {data.map((value: any) => {
                    return <FileRow name={value.name} size={value.size} data={data} setData={setData}/>
                })}
            </div> }

        </div>
    )
}
