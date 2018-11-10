// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

'use strict';

let toggle = document.getElementById('toggle');
let test = document.getElementById('test');
let math = document.getElementById('math');
let cs = document.getElementById('cs');
let chem = document.getElementById('chem');
let drawing = document.getElementById('drawing');
let econ = document.getElementById('econ');
let cb = document.getElementById('cb');
// chrome.storage.sync.get('color', function(data) {
//   changeColor.style.backgroundColor = data.color;
//   changeColor.setAttribute('value', data.color);
// });

const getAllEvents = async () => {        // call this to fetch all events in the database
	const response = await fetch("http://127.0.0.1:5000/todo/api/v1.0/tasks", {
	method: "get"
	});
	const data = await response.json();
	chrome.extension.getBackgroundPage().console.log(data);
};

const postEvent = async (payload) => {  // call this to create an event in the database
  const response = await fetch("http://127.0.0.1:5000/clickbait", {
    method: "post",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });
  const data = await response.json();
  chrome.extension.getBackgroundPage().console.log(data);
  return data;
}

toggle.onclick = function(element) {
    // let color = element.target.value;
    // chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    //   chrome.tabs.executeScript(
    //       tabs[0].id,
    //       {code: 'document.body.style.backgroundColor = "' + color + '";'});
    // });
	// getAllEvents();
    postEvent({ test : 0, test1 : 1 });
};

test.onclick = function(element) {
    // Read it using the storage API
    chrome.storage.sync.get(['math', 'cs', 'chem', 'drawing', 'econ', 'cb'], function(items) {
      chrome.extension.getBackgroundPage().console.log(JSON.stringify(items));
    });
};

math.onclick = function(element) {
    // Read it using the storage API
    save_options();
};
cs.onclick = function(element) {
    // Read it using the storage API
    save_options();
};
chem.onclick = function(element) {
    // Read it using the storage API
    save_options();
};
drawing.onclick = function(element) {
    // Read it using the storage API
    save_options();
};
econ.onclick = function(element) {
    // Read it using the storage API
    save_options();
};
cb.onclick = function(element) {
    // Read it using the storage API
    save_options();
};

// Saves options to chrome.storage
function save_options() {
    chrome.extension.getBackgroundPage().console.log("called saveoptions");
  var mathCheck = document.getElementById('math').checked;
  var csCheck = document.getElementById('cs').checked;
  var chemCheck = document.getElementById('chem').checked;
  var drawingCheck = document.getElementById('drawing').checked;
  var econCheck = document.getElementById('econ').checked;
  var cbCheck = document.getElementById('cb').checked;

  chrome.storage.sync.set({
    math: mathCheck,
    cs: csCheck,
    chem: chemCheck,
    drawing: drawingCheck,
    econ: econCheck,
    cb: cbCheck
  }, function() {
    // don't do anything here
  });
}

// Restores select box and checkbox state using the preferences
// stored in chrome.storage.
function restore_options() { // on new page load
  // Use default value color = 'red' and likesColor = true.
  chrome.storage.sync.get({
    math: true,
    cs: true,
    chem: true,
    drawing: true,
    econ: true,
    cb: true
  }, function(items) {
    document.getElementById('math').checked = items.math;
    document.getElementById('cs').checked = items.cs;
    document.getElementById('chem').checked = items.chem;
    document.getElementById('drawing').checked = items.drawing;
    document.getElementById('econ').checked = items.econ;
    document.getElementById('cb').checked = items.cb;
  });
}

document.addEventListener('DOMContentLoaded', restore_options);