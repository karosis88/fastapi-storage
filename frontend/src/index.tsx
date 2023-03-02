import ReactDOM from 'react-dom/client';
import './index.css';
// import Signup from "./components/signup";
import {BrowserRouter, Route, Routes} from "react-router-dom"
import Signup from './components/signup';
import Login from './components/login';
import Main from './components/main';
import Upload from "./components/upload";
import Files from './components/files';
import CreateStorage from './components/create-storage';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/signup" element={<Signup/>}/>
      <Route path="/login" element={<Login/>}/>
      <Route path="/upload" element={<Upload/>}/>
      <Route path="/files" element={<Files/>}/>
      <Route path="/create-storage" element={<CreateStorage/>}/>
      <Route path="/" element={<Main/>}/>
    </Routes>
  </BrowserRouter>
);



// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
