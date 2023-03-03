import React, { useEffect } from 'react'
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

    let credentials: string = localStorage.getItem('auth') as string
    let headers: any;

    if (credentials)
        headers = {"Authorization": 'Bearer ' + JSON.parse(credentials).access_token}
    else
        headers = {}

    const handleRemove = async () => {

    

        try {
            setPending(true)
            let response: Response = await fetch(`http://127.0.0.1:8000/storage/remove?file_name=${props.name}`,
                {"method" : "POST",
                 "headers": headers})
            if (!response.ok) {
                return
            }

            let data = props.data.filter((element: any) => 
                element.name != props.name) 
            props.setData(data)
            setError(null)
        }

        catch (error) {
            setError("Connection error")
        }

        finally {
            setPending(false)
        }
    }

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/storage/file/${props.name}`, {headers: headers})
            .then(resp => resp.blob())
            .then(blobby => {
                let objectUrl = window.URL.createObjectURL(blobby)
                let link: any;
                let links = document.querySelectorAll('.filename')

                links.forEach(ln => {
                    if (ln.innerHTML === "Name: " +props.name) {
                        link = ln.nextSibling?.nextSibling?.firstChild;
                        return
                    }
                })
                if (link) {
                    link.href = objectUrl
                    link.download = props.name
            }
            } )
    }, [])

    return (
    <div>
        {!pending && 
        <div className="file">
            <div className="filename">Name: {props.name}</div>
            <div className="fsize">Size: {props.size}kb</div>
            
            <div className="buttons-wrapper" >
                <a type="button">Download</a> 
                <button type="button" onClick={async () => await handleRemove()}>Remove</button>
            </div>
            
        </div>
        }
        {pending && <div>Removing...</div>}
    </div>
    )
}


