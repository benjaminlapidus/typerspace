import React from "react";
import "./Caption.scss";

//document.getElementById("nav-id__splide__arrow--prev").click()
//document.getElementById("nav-id__splide__arrow--next").click()

const Caption = (props) => {
	const [currentKey, setCurrentKey] = React.useState(0);
	

	

	return (
		<span
			id={props.letter === " " ? "space" : ""}

				className={
					props.captionInd === props.captionIndex ?
					props.letterInd === props.charIndex
						? "temp blinking-cursor"
						: "temp"
					: "temp"
												
					}

				style={{
					color:
					props.captionInd === props.captionIndex ?
					props.letterInd < props.charIndex
						? "#bababa"
						: "white"
					: "darkGray"
				}}>
			{props.letter}
		</span>
	);
};

export default Caption;