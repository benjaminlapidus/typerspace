import React from "react";
import "./VideoWrapper.scss";
import ReactPlayer from 'react-player/youtube'



function VideoWrapper() {
	return (

// Only loads the YouTube player
<ReactPlayer url='https://www.youtube.com/watch?v=ysz5S6PUM-U'
width='100%'
height='100%'
volume=".2"/>
	);
}

export default VideoWrapper;