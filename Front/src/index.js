import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import {Provider} from 'react-redux';
import store from './components/redux/store';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Corentin from "./components/Corentin";
import BarChart from "./components/Turnover/BarChart";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <Provider store={store}>
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<App/>}/>
                <Route path="/co" element={<Corentin/>}/>
                <Route path="/bar" element={<BarChart/>}/>
                <Route path="*" element={<App/>}/>
            </Routes>
        </BrowserRouter>
    </Provider>
);

