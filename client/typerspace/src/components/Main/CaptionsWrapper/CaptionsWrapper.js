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
};

const CaptionsWrapper = (props) => {
	const [currentKey, setCurrentKey] = React.useState(0);
	const [captionIndex, setCaptionIndex] = React.useState(0);
	const [charIndex, setCharIndex] = React.useState(0);

	const checkChar = (char) => {
		let currCharIndex = charIndex;
		let currCaptionIndex = captionIndex;

		console.log("Here: " + props.words[captionIndex].split("")[charIndex]);
		console.log("char: " + String.fromCharCode(char))
		if (props.words[captionIndex].split("")[charIndex] === String.fromCharCode(char)){
			currCharIndex++;
			setCharIndex(currCharIndex);

			if (currCharIndex >= props.words[captionIndex].split("").length){
				currCaptionIndex++;
				setCaptionIndex(currCaptionIndex);
				setCharIndex(0);
				document.getElementById("nav-id__splide__arrow--next").click()
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
					setCurrentKey(e.keyCode);
					checkChar(e.keyCode);
				} else {
					// If the SHIFT key is not down, convert to the ASCII code for the lowecase letter
					setCurrentKey(e.keyCode + 32);
					checkChar(e.keyCode + 32);
				}
			} else {
				setCurrentKey(e.keyCode);
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
						<SplideSlide key={captionInd}>
							<div className="caption__line">
								{phrase.split("").map((letter, letterInd) => {

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