import React from "react";
import './firebase.config';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Link } from 'react-router-dom';
import DrawerAppBar from './components/HomePage';

export const App = () => {
  return(
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<DrawerAppBar />} />
      </Routes>
    </BrowserRouter>
  );
}
