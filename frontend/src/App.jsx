import React from 'react';
import {BrowserRouter} from 'react-router-dom'
import {Route, Routes} from "react-router";
import DailyMain from "./pages/DailyMain";
const App = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path='/main' element={<DailyMain/>} />


            </Routes>
        </BrowserRouter>
    );
};

export default App;