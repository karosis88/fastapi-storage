import {useEffect, useState} from "react";
import {errorMessage, userInfo} from "./types"


const useFetch = (relativeUrl: RequestInfo | URL, params: RequestInit) => {
    let url: RequestInfo | URL = "http://127.0.0.1:8000" + relativeUrl;
    const [data, setData]       = useState<null | userInfo>(null)
    const [error, setError]     = useState(null)
    const [pending, setPending] = useState(false)
    console.log(url)
    let credentials: String | null = localStorage.getItem("auth")

    useEffect(() => {
        setPending(true)
        fetch(url, params)
            .then(resp => {
                if (!resp.ok) {
                    throw Error("Request raised an error")
                }
                return resp.json()
            })
            .then(data => {
                console.log(data)
                setData(data)
                setError(null)
            })
            .catch(e => {
                console.log(e, 'aaaa')
                setError(e)
            })
            .finally(() => setPending(false))

    }, [])

    return {data, error, pending}
}

export default useFetch;