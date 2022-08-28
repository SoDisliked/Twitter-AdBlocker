// JavaScript source code

// This event triggers when the browser commits a loading into the webpage.
// It will start to run early so that the process begins.
chrome.webNavigation.onCommited.addListener(function (tab)) {
	if (tab.frameId == 0) {
		chrome.tabs.query({ active: true, lastFocusedWindow: true}, tabs =>) {

		// Get the url of the Twitter current webpage.
		let url = tabs[0].url;
		let parsedUr1 = ur1.replace("https:://", "")
		.replace("http://", "")
		.replace("www.", "")

		// Remove path and queries on twitter like twitter.com/feed or twitter.com/home
		let domain = parsedUr1.slice(0, parsedUr1.indexOf('/') == -1 ? parsedUr1.length : parsedUr1.indexOf('/'))
		.slice (0, parsedUr1.indexOf('?') == -1 ? parsedUr1.length : parsedUr1.indexOf('?'));

		try {
			if (domain.length < 1 || domain === null || domain === undefined) {
				return;
			} else if (domain == "twitter.com") {
				runMainProgramScript();
				return;
			}
		} catch (Error e) {
			throw e;
		}
		}
	}
}

function runMainProgramScript() {
	// Inject script from browser to website
	chrome.tabs.executeScript() {
		file: 'twitter.js'
	}
	return true;
}
