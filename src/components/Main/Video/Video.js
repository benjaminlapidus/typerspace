import React from "react";
import "./VideoWrapper.css";
import ReactPlayer from "react-player/youtube";
//test video: https://www.youtube.com/watch?v=CHP0-NwiiXk
const VideoWrapper = (props) => {
  let videoLink = "https://www.youtube.com/watch?v=" + props.id;
  let [isPlaying, setIsPlaying] = React.useState(false);
  let [captionIndex, setCaptionIndex] = React.useState(0);
  console.log(props);
  const handleCaptionChange = (capIndex) => {
    setCaptionIndex(capIndex);
    props.handleCaptionIndex(capIndex);
  };

  const testData = (e) => {
    console.log(e);
    if (e.playedSeconds > props.data[captionIndex + 1].start) {
      console.log(e.playedSeconds);
      console.log(props.data[captionIndex + 1].start);
      document.getElementById("nav-id__splide__arrow--next").click();
      let tempIndex = captionIndex;
      handleCaptionChange(tempIndex + 1);
    }
  };

  return (
    // Only loads the YouTube player
    <ReactPlayer
      url={videoLink}
      width="100%"
      height="100%"
      onProgress={(e) => testData(e)}
    />
  );
};

export default VideoWrapper;
