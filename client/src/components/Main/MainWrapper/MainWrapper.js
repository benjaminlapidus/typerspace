import React from "react";
import VideoWrapper from "../VideoWrapper/VideoWrapper";
import CaptionsWrapper from "../CaptionsWrapper/CaptionsWrapper";
import StatisticsWrapper from "../StatisticsWrapper/StatisticsWrapper";
import KeyboardWrapper from "../KeyboardWrapper/KeyboardWrapper";
import "./MainWrapper.scss";

function MainWrapper(props) {
var link = props.location.search.substring(props.location.search.length - 11);
const [isLoading, setLoading] = React.useState(true);
const [captionIndex, setCaptionIndex] = React.useState(true);
let [data, setData] = React.useState({});
const axios = require('axios').default;

function handleCaptionIndex(newValue) {
    setCaptionIndex(newValue);
  }

  React.useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/' + link).then(response => {
      setData(response.data);
      setLoading(false);
    });
  }, []);

  // React.useEffect(() => {
  //   axios.get("api/" + videoID).then(response => {
  //     console.log(response.data);
  //     setData(response.data);
  //     setLoading(false);
  //   });
  // }, []);

  if (isLoading) {
    return <div className="loader"></div>;
  }

  return (
		<div className="wrapper">
    <div class="solar-syst">
      <div class="sun"></div>
      <div class="mercury"></div>
      <div class="venus"></div>
      <div class="earth"></div>
      <div class="mars"></div>
      <div class="jupiter"></div>
      <div class="saturn"></div>
      <div class="uranus"></div>
      <div class="neptune"></div>
      <div class="asteroids-belt"></div>
    </div>
			<div className="video__wrapper">
				<VideoWrapper id={link} handleCaptionIndex={handleCaptionIndex} data={data.captions}/>
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
