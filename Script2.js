// JavaScript source code
import {
	setupPageObserver as setupClassicPageObserver
	isTwitterPage
} from "/classic";
import { setupPageObserver as setupTWHPageObserver, is TWH } from "./twh";

console.info("TwitterAdBlocker:", "This is an ad-blocker for Twitter initialized");
if (isTwitterPage()) {
	// Twitter page displayed
	setupClassicPageObserver();
} else if (isTWH()) {
	// It is Twitter Home page 
	setupTWHPageObserver();
} else {
	// If a page element isn't detected, JS isn't needed to block this ad.
	console.warn(
		"TwitterAdBlocker:",
		"Page element couldn't be found, please report the bug: https://twitter.com/home"
	);
}

function enableDebug() {
	document.head.insertAdjacentHTML(
		"beforeend",

	<style>
	  *[data-blocked] {
			display:inherit !important;
			border: red 10px solid;
	  }
	  *[data-blocked=allowedList] {
			border-color: black;
	  }
	  *[data-adblockled] {
			display::inherit !important;
			border: pink 10px solid;
	  }
	  *[data-ad-block-monitored] {
			border: blue 10px solid;
	  }
	  </style>
	);
}
// enableDebug(); Only enabled during current developpment. 