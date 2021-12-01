// async chrome.runtime.onInstalled.addListener(() => {
//   let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
//   console.log(tab.url);
// });

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  console.log(request.url);
  // fetch('127.0.0.1:8000?url=' + request.url)
  // .then(function(response) {
  //   return response.json();
  // })
  // .then(function(jsonResponse) {
  //   // do something with jsonResponse
  //   sendResponse({ message: 'fake' });
  // })
  // .catch((error) => {
  //   console.error('Error:', error);
  // });
  sendResponse({ message: 'fake' });
  return true;
});
