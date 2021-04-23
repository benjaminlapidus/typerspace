import React from "react";
import "./CaptionsWrapper.scss";
import { Splide, SplideSlide } from "@splidejs/react-splide";
import Caption from "../Caption/Caption";


//document.getElementById("nav-id__splide__arrow--prev").click()
//document.getElementById("nav-id__splide__arrow--next").click()

const primaryOptions = {
	type: "loop",
	perPage: 3,
	perMove: 1,
	gap: "1.20em",
	direction: "ttb",
	focus: "center",
	height: "16vh",
	pagination: false,
	arrows: true,
	autoWidth: true,
	lazyLoad: 'nearby'
};

const secondaryOptions = {
	focus: 'center',
}


const CaptionsWrapper = (props) => {
	const [captionIndex, setCaptionIndex] = React.useState(props.captionIndex);
	const [charIndex, setCharIndex] = React.useState(0);

	const checkChar = (char) => {
		let currCharIndex = charIndex;
		let currCaptionIndex = captionIndex;

		if (props.words[currCaptionIndex].text.split("")[currCharIndex] === String.fromCharCode(char)){
			currCharIndex++;
			setCharIndex(currCharIndex);

			if (currCharIndex >= props.words[currCaptionIndex].text.split("").length){
				setCharIndex(0);
				currCaptionIndex++;
				setCaptionIndex(currCaptionIndex);
			}
		}
	}

	document.addEventListener("keydown", (e) => {
		if (e.keyCode != 16) {
			// If the pressed key is anything other than SHIFT
			if (e.keyCode >= 65 && e.keyCode <= 90) {
				// If the key is a letter
				if (e.shiftKey) {
					// If the SHIFT key is down, return the ASCII code for the capital letter
					checkChar(e.keyCode);
				} else {
					// If the SHIFT key is not down, convert to the ASCII code for the lowecase letter
					checkChar(e.keyCode + 32);
				}
			} else {
				checkChar(e.keyCode);
			}
		}


	});

	return (
		<div className="wrapper">
			<div id="infoi"></div>
			<Splide className="slider" options={primaryOptions}>
				{props.words.map((phrase, captionInd) => {
					return (
						<SplideSlide>
							<div className="caption__line">
								{phrase.text.split("").map((letter, letterInd) => {
									return (
										<Caption
											captionInd = {captionInd}
											captionIndex = {captionIndex}
											charIndex = {charIndex}
											letterInd = {letterInd}
											letter={letter}
										/>
									);
								})}
							</div>
						</SplideSlide>
					);
				})}
			</Splide>
		</div>
	);
};

export default CaptionsWrapper;
