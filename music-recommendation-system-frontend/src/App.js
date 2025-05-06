import React from "react";
import { useSelector } from "react-redux";
import {Navigate, Route, Routes, BrowserRouter as Router} from "react-router-dom";
import Recommendations from "./pages/Recommmendations";
import Login from "./components/Login";
import "antd/dist/reset.css";

const App = () => {
    const userId = useSelector((state) => state.auth.userId);

    return (
        <Router>
            <div className="app-container">
                <Routes>
                    <Route path="/login" element={userId ? <Navigate to="/"/> : <Login/>}/>
                    <Route path="/" element={userId ? <Recommendations/> : <Navigate to="/login"/>}/>
                </Routes>
            </div>
        </Router>
    );
};

export default App;