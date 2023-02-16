import React from "react";
import "./App.css";
import { Route, Routes } from "react-router-dom";
import Home from "./components/HomePage/Home";
import Search from "./components/SearchPage/Search";
import Contact from "./components/ContactPage/Contact";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/home" element={<Home />} />
      <Route path="/search" element={<Search />} />
      <Route path="/contact" element={<Contact />} />
    </Routes>
  );
}

export default App;
