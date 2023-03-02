import React from 'react'
import { useState } from 'react'

type file = {
    name: string,
    size: number,
    data: any,
    setData: any
}


export default function FileRow (props: file) {

    const [pending, setPending] = useState<boolean>()
    const [erro, setError] = useState<string | null>()


    const handleRemove = async () => {
        let credentials: string = localStorage.getItem('auth') as string
        let headers

        if (credentials)
            headers = {"Authorization": 'Bearer ' + JSON.parse(credentials).access_token}
        else
            headers = {}
    

        try {
            setPending(true)
            let response: Response = await fetch(`http://127.0.0.1:8000/storage/remove?file_name=${props.name}`,
                {"method" : "POST",
                 "headers": headers})
            console.log(await response.text())
            if (!response.ok) {
                return
            }

            let data = props.data.filter((element: any) => 
                element.name != props.name) 
            props.setData(data)
            setError(null)
        }

        catch (error) {
            console.log(error)
            setError("Connection error")
        }

        finally {
            setPending(false)
        }
    }

    return (
    <div>
        {!pending && 
        <div className="file">
            <div className="filename">Name: {props.name}</div>
            <div className="fsize">Size: {props.size}kb</div>
            
            <div className="buttons-wrapper">
                <button type="button">Download</button>
                <button type="button" onClick={async () => await handleRemove()}>Remove</button>
            </div>
            
        </div>
        }
        {pending && <div>Removing...</div>}
    </div>
    )
}


