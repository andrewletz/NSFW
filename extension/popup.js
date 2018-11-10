// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

'use strict';

let get = document.getElementById('get');
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
}

const postTest = async () => {        // call this to fetch all events in the database
    const response = await fetch("http://127.0.0.1:5000/todo/api/v1.0/tasks", {
    method: "get"
    });
    const data = await response.json();
    chrome.extension.getBackgroundPage().console.log(data);
}

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

get.onclick = function(element) {
    // let color = element.target.value;
    // chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    //   chrome.tabs.executeScript(
    //       tabs[0].id,
    //       {code: 'document.body.style.backgroundColor = "' + color + '";'});
    // });
	// getAllEvents();
    postEvent({ test : 0, test1 : 1 });
};