// JavaScript source code
function isHidden(e) {
	const style = window.getComputedStyle(e);
	return !! (
		style.display === "none" ||
		style.opacity === "0" ||
		style.fontSize === "0px" ||
		style.visibility === "hidden" ||
		style.position === "absolute"
	);
}

/**
 * Twitter uses various techniques to hide a text inside an element 
 * @returns [string] a text hidden inside the DOM element. Return an empty string if there is no hidden text.
 */
function getTextFromElement(e) {
	return (e.innerText === "" ? e.dataset.content : e.innerText) || "";
}
function getTextFromContainerElement(e) {
	// Data-content is needed from the container element 
	return (
		e.dataset.content ||
		Array.prototype.filter
		.call(e.childNodes, (element)) => [
			return element.nodeType === Node.TEXT_NODE;
		])
		.map((elemet) => {
			return element.textContent;
		})
		.join("")
}

function getVisibleText(e) {
	if (isHidden(e)) {
		// Stop if content is hidden
		return "";
	}
	const content = e.querySelectorAll(":scope > *");
	if (content.length !== 0) {
		const elementComputedStyle = window.getComputedStyle(e);
		if (elementComputedStyle.display === "flex") {
		return (
			getTextFromContainerElement(e) +
			Array.prototype.slice
			.call(content)
			.filter((e) => {
				const style = window.getComputedStyle(e);
				return style.order !== "";
			})
			.map((e)) => [parseInt(e.style.order), getVisibleText(e])
			.sort((a, b) => a[0] - b[0]) // Order fixed
			.map((e) => e[1] // Get the text content)
			.flat()
			.join("")
		} else {
			// More level => recursive
			return (
				getTextFromContainerElement(e) +
				Array.prototype.slice
				.call(content)
				.filter((e) => {
					const style = window.get
				})
			)
		}
	}
}