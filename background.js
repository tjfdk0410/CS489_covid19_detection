// async chrome.runtime.onInstalled.addListener(() => {
//   let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
//   console.log(tab.url);
// });

// chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
//   console.log(request.url);
//   // fetch('127.0.0.1:8000?url=' + request.url)
//   // .then(function(response) {
//   //   return response.json();
//   // })
//   // .then(function(jsonResponse) {
//   //   // do something with jsonResponse
//   //   sendResponse({ message: 'fake' });
//   // })
//   // .catch((error) => {
//   //   console.error('Error:', error);
//   // });
//   sendResponse({ message: 'fake' });
//   return true;
// });

// chrome.webNavigation.onDOMContentLoaded.addListener(onCommitted, {
//   url: [
//     {hostEquals: 'www.example.org'},
//     {urlPrefix: 'https://example.org/'},
//     {urlMatches: '^https://(www\.)?example.org/.*$'},
//   ],
// });
//
// function onCommitted(info) {
//   const xhr = new XMLHttpRequest();
//   xhr.open('POST', 'http://localhost:8123/detect/');
//   xhr.send(info.url);
// }
