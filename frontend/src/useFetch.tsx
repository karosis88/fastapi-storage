import {useEffect, useState} from "react";
import {errorMessage, userInfo} from "./types"


const useFetch = (relativeUrl: RequestInfo | URL, params: RequestInit) => {
    let url: RequestInfo | URL = "http://127.0.0.1:8000" + relativeUrl;
    const [data, setData]       = useState<null | any>(null)
    const [error, setError]     = useState<null | string>(null)
    const [pending, setPending] = useState(false)

    useEffect(() => {
        fetch(url, params)
            .then(resp => {
                return resp.json()
            })
            .then(data => {

                if (data.detail) {
                    if (data.detail === "Invalid username or password") {
                        localStorage.removeItem('auth')
                    }
                    setError(data.detail)
                    return
                }
                setData(data)
                setError(null)
             
            })
            .catch(e => {
                setError("Connection error")

            })
            .finally(() => setPending(false))

    }, [])

    return {data, error, pending, setData, setError, setPending}
}

export default useFetch;