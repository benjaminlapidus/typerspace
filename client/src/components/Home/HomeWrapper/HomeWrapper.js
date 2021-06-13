import React from "react";
import Typist from 'react-typist';
import "./HomeWrapper.scss";
import 'react-typist/dist/Typist.css'

function HomeWrapper(props) {
	const [link, setLink] = React.useState("");
	const ytParser = (url) => {
		var regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*/;
		var match = url.match(regExp);
		setLink(match && match[7].length == 11 ? match[7] : false);
	};

	return (
		<div className="Home">
			<h1 className="Home__header">Typerspace</h1>
			<h2 className="Home__sub_header">
				<Typist avgTypingDelay={80} cursor={{ hideWhenDone: false, blink: true}}>
				Begin Your Mission
			</Typist>
			</h2>
			<div className="Homesearch-wrapper">
				<form className="Home__form" action={"/dashboard"}>
					<input
						onChange={(e) => ytParser(e.target.value)}
						type="text"
						id="Home__ytlink"
						name="link"
					/>
					<div className="Home__submitButtonWrapper">
						<input
							id="Home__submitButton"
							type="submit"
							value="take off"
						/>
					</div>
				</form>
			</div>
		</div>
	);
}

export default HomeWrapper;