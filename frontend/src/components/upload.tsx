import React, { useState } from 'react';
import HeaderBar from './header';

const Upload = () => {
    const [error, setError] = useState<null | String>(null)
    const [pending, setPending] = useState<Boolean>(false)
    const [success, setSuccess] = useState<null | String>(null)
    
    const submitHandler = async (e: React.MouseEvent<HTMLButtonElement>) => {
        let fileElement: HTMLInputElement = document.getElementById("file") as HTMLInputElement
        let file: File
        let credentials: string = localStorage.getItem("auth") as string
        let headers;
      

        if (credentials) {
            headers = {
                "Authorization" : "Bearer " + JSON.parse(credentials).access_token
            }
        }
        else {
            headers = {}
        }
        if (fileElement.files) {
            setPending(true)
            file = fileElement.files[0]
            let formData: FormData = new FormData()
            formData.append("file", file)
            setPending(true)
            try {
                let response: Response = await fetch("http://127.0.0.1:8000/storage/upload", {
                    "body" : formData,
                    "method" : "POST",
                    "headers" : headers
                })

                let content = await response.json()

                if (!response.ok) {
                    setError(content.detail)
                    setSuccess(null)
                    return
                }
                setSuccess("File was uploaded!")
                setError(null)
                
            }
            catch (error) {
                setError("HTTP request failed")
                setSuccess(null)
            }
            finally {
                setPending(false)
            }

        }
        else {
            return
        }
    }

    return (
        <div>
            <HeaderBar/>
            
            <div className="uploadwrapper">
                {!pending &&
                <form action="">
                    <input id="file" type="file"/>
                    <button onClick={submitHandler} type="button">Send</button>
                </form>}
                {pending && <div>Loading...</div>}
                {error && <div>{error}</div>}
                {success && <div>{success}</div>}
            </div>
            
        </div>
    );
};

export default Upload;