import React from "react";
import "./HomeWrapper.scss";


function HomeWrapper() {
	return (
		<div>
	<div class="description">
  <h1>Solar System</h1>
  <hr/>
  <p>
    I know this is not the first one on CodePen, but I'm a space and physics lover, and I wanted to create mine :)
  </p>
  <p>
    Here is a true time scaled solar-system, which means that every objects have a time relative to an Earth year.
    You can change the number in second of the
    <br/>
    <code>$year-in-second</code>
    variable to increase the speed of revolutions. Here 1 year = 30 seconds.
  </p>
  <p class="hide">
    Note the css tricks for the Saturn rings (box-shadow) and reverse animation to compensate the orbit.
  </p>
  <hr/>
  <p class="author">
    Made with
    <i class="fa fa-heart"></i>
    by Malik Dellidj
  </p>
  <p class="links">
    <a class="fa fa-codepen icon" href="https://codepen.io/kowlor/" target="_blank"></a>
    <a class="fa fa-github-alt icon" href="https://github.com/KOWLOR" target="_blank"></a>
    <a class="fa fa-twitter icon" href="https://twitter.com/Dathink" target="_blank"></a>
  </p>
</div>
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

</div>

	);
}

export default HomeWrapper;