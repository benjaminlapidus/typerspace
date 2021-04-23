import React from "react";
import VideoWrapper from "../VideoWrapper/VideoWrapper";
import CaptionsWrapper from "../CaptionsWrapper/CaptionsWrapper";
import StatisticsWrapper from "../StatisticsWrapper/StatisticsWrapper";
import KeyboardWrapper from "../KeyboardWrapper/KeyboardWrapper";
import "./MainWrapper.scss";

function MainWrapper(props) {
var link = props.location.search.substring(props.location.search.length - 11);
// var idFound = props.location.search.indexOf("?v=");
// var timeFound = props.location.search.indexOf("?t=")
// var time = 0;
// if(timeFound != -1){
//   time = 0;
// }
// if(idFound == -1){
//   link = props.location.search.substring(props.location.search.length - 11);
// } else {
//   var link = props.location.search.toLowerCase().substring(idFound + 3, idFound + 15);
// }
const [isLoading, setLoading] = React.useState(true);
const [captionIndex, setCaptionIndex] = React.useState(0);
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
    <div className="solar-syst">
      <div className="sun"></div>
      <div className="mercury"></div>
      <div className="venus"></div>
      <div className="earth"></div>
      <div className="mars"></div>
      <div className="jupiter"></div>
      <div className="saturn"></div>
      <div className="uranus"></div>
      <div className="neptune"></div>
      <div className="asteroids-belt"></div>
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
