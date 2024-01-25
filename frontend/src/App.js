// App.js
import './App.css'
import Header from './components/Header/header';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import style from './components/Header/header.module.scss'

import Yash_alghoritm from './Pages/YASH-algorithm/yash_alghoritm';
import Sdes_alghoritm from './Pages/S-DES-algorithm/sdes_alghoritm';
import Saes_alghoritm from './Pages/S-AES-algorithm/saes_alghoritm';
import MainPage from './Pages/mainPage/mainPage';

function App() {
  return (
    <>
    <Header/>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<MainPage />} />
          <Route path='*' element={<MainPage />} />
          <Route path='/YASH' element={<Yash_alghoritm />} />
          <Route path='/S-DES' element={<Sdes_alghoritm />} />
          <Route path='/S-AES' element={<Saes_alghoritm />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
