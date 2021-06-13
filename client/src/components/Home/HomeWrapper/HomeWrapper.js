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
			<h1 className="Home__header">Typerspace</h1>
			<h2 className="Home__sub_header">Begin your mission</h2>

			<div className="search-wrapper">
			<form className="Home__form" action={"/dashboard"}>
   				<input onChange={e => ytParser(e.target.value)} type="text" id="Home__ytlink" name="link" />
   				<div className="Home__submitButtonWrapper">
   				<input id="Home__submitButton" type="submit" value="take off"/>
   				</div>
  			</form>
  			</div>
		</div>
	);
}

export default HomeWrapper;
