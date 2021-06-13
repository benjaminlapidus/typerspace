import React from "react";
import "./Caption.scss";

//document.getElementById("nav-id__splide__arrow--prev").click()
//document.getElementById("nav-id__splide__arrow--next").click()

const Caption = (props) => {

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
						? "yellow"
						: "white"
					: "green"
				}}>
			{props.letter}
		</span>
	);
};

export default Caption;
