import React from "react";
import HeroSection from "../HeroSection";
import Navbar from "../Navbar";
import { homeObjOne } from "./Data";
// import Steps from "../Steps";

function Home() {
  return (
    <>
      <Navbar></Navbar>
      <HeroSection {...homeObjOne} />
    </>
  );
}

export default Home;
