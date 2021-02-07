import React from "react";
import VideoWrapper from "../VideoWrapper/VideoWrapper";
import CaptionsWrapper from "../CaptionsWrapper/CaptionsWrapper";
import StatisticsWrapper from "../StatisticsWrapper/StatisticsWrapper";
import KeyboardWrapper from "../KeyboardWrapper/KeyboardWrapper";
import "./MainWrapper.scss";

let words = ["dbv", "Second sentence is cool", "Third is even better!", ""];

function MainWrapper() {
	
const [isLoading, setLoading] = React.useState(true);
const [captionIndex, setCaptionIndex] = React.useState(true);
let [data, setData] = React.useState({});
let videoID = "F12PJgyVKyA";
const axios = require('axios').default;

function handleCaptionIndex(newValue) {
    setCaptionIndex(newValue);
  }

  React.useEffect(() => {
    axios.get("http://typer.space/api/" + videoID).then(response => {
      setData(response.data);
      setLoading(false);
    });
  }, []);

  if (isLoading) {
    return <div style={{color: "white"}}>Loading...</div>;
  }

  return (
		<div className="wrapper">
			<div className="video__wrapper">
				<VideoWrapper handleCaptionIndex={handleCaptionIndex} data={data.captions}/>
			</div>
			<div className="caption__wrapper">
				<CaptionsWrapper captionIndex={captionIndex} words={data.captions} />
			</div>
			<div className="keyboard__wrapper">
				<KeyboardWrapper />
			</div>
			<div className="statistics__wrapper">
				<StatisticsWrapper />
			</div>
		</div>
	);
}

export default MainWrapper;