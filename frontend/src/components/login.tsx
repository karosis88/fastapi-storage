import React, {useEffect, useState} from 'react';
import HeaderBar from './header';


export default function Login() {


    const [error, setError] = useState(String || null)
    
    const submitHandler = async (e: React.MouseEvent<HTMLButtonElement>) => {
        let usernameValue: String = (document.getElementById("username") as HTMLInputElement).value
        let passwordValue: String = (document.getElementById("password") as HTMLInputElement).value
        console.log(usernameValue, passwordValue)
        
        try {
            let response: Response = await fetch(`http://127.0.0.1:8000/auth/login`, {
                    "method" : "POST",
                    "headers" : {
                        "Content-Type" : 'application/x-www-form-urlencoded'
                    },
                    "body" : `username=${usernameValue}&password=${passwordValue}`
                })
            let content = await response.json()
            if (!response.ok) {
                if (Boolean(response.status === 422))
                    setError("Invalid data sent")
                else
                    setError(content["detail"])
                    

                return
            }
            setError("")
            localStorage.setItem("auth", JSON.stringify(content))
            window.location.href = "/"
            }
        catch (error) {
            setError("er")
        }
    }

    return (
        <div>
            <HeaderBar/>
            <h2>Sign In</h2>
            <form className="signin-form">
                    <div className="username-div">
                        <input id="username" type="text" placeholder="Username"/>
                    </div>
                    <div className="password-div">
                        <input id="password" type="password" placeholder="Password"/>
                    </div>
                    <button onClick={submitHandler} type="button" >Submit</button>

                    {error && 
                    (<p className="errorMsg">{error}</p>)}
                </form>
        </div>
    )
}
