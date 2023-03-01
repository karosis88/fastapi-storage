import { userInfo } from "os"

type errorMessage = {
    preview: String,
    type: String, 
}

type userInfo = {
    id: Number,
    username: String,
    email: String,
    first_name: String,
    last_name: String
}

export type {errorMessage,
        userInfo}