import React from "react";
import "./StatisticsWrapper.scss";
//<h1 onClick={e=>document.getElementById("nav-id__splide__arrow--next").click()}>Next</h1>
//<h1 onClick={e=>document.getElementById("nav-id__splide__arrow--prev").click()}>Prev</h1>
function StatisticsWrapper(props) {

//going to get this data from props later, because the statistics will be updated in another component
let [wpm, setWpm] = React.useState(76);
let [pKeystrokes, setPKeystrokes] = React.useState(153); //correct keystrokes
let [nKeystrokes, setNKeystrokes] = React.useState(12); //wrong keystrokes
let [accuracy, setAccuracy] = React.useState(98);
let [correctWords, setCorrectWords] = React.useState(87);
let [wrongWords, setWrongWords] = React.useState(5);

	return (
		<div className="column_div">
			<div className="stat">
				<span> WPM: {wpm}</span>
			</div>
			<div className="stat">
				Accuracy:
				<span style={{color: "gold"}}>{' '+accuracy}{'%'}</span>
			</div>
			<div className="stat">
			  Keystrokes:
				(
				<span style={{color: "green"}}>
				  {' '}{pKeystrokes}{' '}
				</span>
				 |
				 <span style={{color: "red"}}>
 				  {' '}{nKeystrokes}{' '}
 				</span>
				)
			</div>
			<div className="stat">
			  Correct words:
				<span style={{color: "green"}}>{' '}{correctWords}</span>
			</div>
			<div className="stat">
			  Wrong words:
				<span style={{color: "red"}}>{' '}{wrongWords}</span>
			</div>
			</div>
	);
}

export default StatisticsWrapper;
