// callback executed when canvas was found
function handleRecs(recs) { 
	var index = 0, length = recs.length;
	for ( ; index < length; index++) {
	    recs[index].style.backgroundColor = "#FFFFFF";
	    recs[index].style.filter = "blur(10px)";
	} 
}

// set up the mutation observer
var observer = new MutationObserver(function (mutations, me) {
  // `mutations` is an array of mutations that occurred
  // `me` is the MutationObserver instance
  var recs = document.querySelectorAll("ytd-compact-video-renderer");
  if (recs.length > 18) { // if this is greater than 18, all of our recommendations are loaded in
    handleRecs(recs);
    me.disconnect(); // stop observing
    return;
  }
});

// start observing
observer.observe(document, {
  attributes: true,
  childList: true,
  characterData: true,
  subtree: true
});