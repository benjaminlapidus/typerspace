import React from "react";
import VideoWrapper from "../VideoWrapper/VideoWrapper"
import CaptionsWrapper from "../CaptionsWrapper/CaptionsWrapper"
import StatisticsWrapper from "../StatisticsWrapper/StatisticsWrapper"
import KeyboardWrapper from "../KeyboardWrapper/KeyboardWrapper"
import "./MainWrapper.scss";

let words = ["dbv","Second sentence is cool","Third is even better!",""];

function MainWrapper() {
	return (
	<div className="wrapper">
  <div className="video__wrapper"><VideoWrapper/></div>
  <div className="caption__wrapper"><CaptionsWrapper words={words} /></div>
  <div className="keyboard__wrapper"><KeyboardWrapper/></div>
  <div className="statistics__wrapper"><StatisticsWrapper/></div>
</div>

	);
}

export default MainWrapper;