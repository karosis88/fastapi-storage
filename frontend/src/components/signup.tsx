import React, {useEffect, useState} from 'react';
import useFetch from "../useFetch";
import HeaderBar from './header';

const Signup = () => {
    const [error, setError] = useState(null)
    const [created, setCreated] = useState(false)

    const submitHandler = async (e: React.MouseEvent<HTMLButtonElement>) => {
        let usernameValue: String = (document.getElementById("username") as HTMLInputElement).value
        let passwordValue: String = (document.getElementById("password") as HTMLInputElement).value


        try {
            let response: Response = await fetch("http://127.0.0.1:8000/auth/signup", {
                "method" : "POST",
                "headers" : {
                    "Content-Type" : "Application/json"
                },
                "body" : JSON.stringify({
                    "username" : usernameValue,
                    "password" : passwordValue
                })
            })
            let content = await response.json()
            if (!response.ok) {
                setError(content["detail"])
                return
            }
            setError(null)
            setCreated(true)

        }
        catch (error: any) {
            setError(error)
        }
    }

    
    return (
        <div>
            <HeaderBar/>
            <h2> Sign Up </h2>
            <form className="signup-form">
                <div className="username-div">
                    <input id="username" type="text" placeholder="Username"/>
                </div>
                <div className="password-div">
                    <input id="password" type="password" placeholder="Password"/>
                </div>
                <div className="password-div">
                    <input id="re-password" type="password" placeholder="Re-Enter Password"/>
                </div>
                <button onClick={submitHandler} type="button" >Submit</button>

                {error && 
                (<p className="errorMsg">{error}</p>)}
                {created && <p className="successMsg">
                    Account was created</p>}
            </form>
        </div>
    );
};

export default Signup;