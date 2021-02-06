import React from "react";
import VideoWrapper from "../VideoWrapper/VideoWrapper"
import "./MainWrapper.scss";


function MainWrapper() {
	return (
		<div className="wrapper">
  <div className="video__wrapper"><VideoWrapper/></div>
  <div className="caption__wrapper">Item #2</div>
  <div className="keyboard__wrapper">Item #3</div>
  <div className="statistics__wrapper">Item #4</div>
</div>

	);
}

export default MainWrapper;