import React from "react";
import "./StatisticsWrapper.scss";

function StatisticsWrapper() {
	return (
		<div className="wrapper">
 			<h1 onClick={e=>document.getElementById("nav-id__splide__arrow--next").click()}>Next</h1>
 			<h1 onClick={e=>document.getElementById("nav-id__splide__arrow--prev").click()}>Prev</h1>

</div>

	);
}

export default StatisticsWrapper;