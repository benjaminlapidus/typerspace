import React from "react";
import "./HomeWrapper.scss";

function HomeWrapper(props) {
	const [link, setLink] = React.useState("");

	const ytParser = (url) => {
    var regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
    var match = url.match(regExp);
    setLink((match&&match[7].length==11)? match[7] : false);
}

	return (
		<div>
			<h1 className="header">Typerspace</h1>
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

			<div className="search-wrapper">
			<h2 className="bottom_header">Begin your mission</h2>
			<form className="home__form" action={"/dashboard"}>
   				<input onChange={e => ytParser(e.target.value)} type="text" id="ytlink" name="link" />
   				<div className="submitButtonWrapper">
   				<input id="submitButton" type="submit" value="takeoff"/>
   				</div>
  			</form>
  			</div>

			<div className="attribution">
				Background created by <a href="https://github.com/KOWLOR">Malik Dellidj</a>
			</div>
		</div>
	);
}

export default HomeWrapper;
