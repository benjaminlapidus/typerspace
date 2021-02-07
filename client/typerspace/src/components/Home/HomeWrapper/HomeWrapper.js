import React from "react";
import "./HomeWrapper.scss";

function HomeWrapper() {
	const [link, setLink] = React.useState("");

	const ytParser = (url) => {
    var regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
    var match = url.match(regExp);

    setLink(match[7]);
   
}
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
				<div class="pluto"></div>
				<div class="asteroids-belt"></div>
			</div>

			<div className="search-wrapper">
			<form className="home__form" action={"/dashboard"}>
    			<label for="ytlink">Enter a YouTube link to begin your mission</label>
   				<input onChange={e => setLink(e.target.value)} type="text" id="ytlink" name="link" placeholder="https://youtu.be/Bed1z7f1EI4"/>
   				<div className="submitButtonWrapper">
   				<input id="submitButton" type="submit" value="Submit"/>
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