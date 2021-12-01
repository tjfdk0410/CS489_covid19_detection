let detect = document.getElementById("detect");

detect.addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.runtime.sendMessage({
    url: tab.url
  }, (response) => {
    if (response.message === 'fake'){
      chrome.scripting.executeScript({
        target: { tabId: tab.id },
        function: popupWarning,
      });
    }
  });
});

// The body of this function will be execuetd as a content script inside the current page
function popupWarning() {
  let modal = document.createElement("div");
  modal.style.cssText = "position: fixed; z-index: 100; padding-top: 100px; left: 0; top: 0; width: 100%; height: 100%; overflow: auto; background-color: rgb(0,0,0); background-color: rgba(0,0,0,0.4);";
  modal.style.display = 'block';

  let modal_content = document.createElement("div");
  modal_content.style.cssText = "background-color: #fefefe; margin: auto; padding: 20px; border: 1px solid #888; width: 30%; height: 20%;";

  let close = document.createElement("span");
  close.style.cssText = "color: #aaaaaa; float: right; font-size: 28px; font-weight: bold;";
  close.innerText = 'X';

  let title = document.createElement("h2");
  title.style.cssText = "color: #E1300D; text-align: center; font-size: 28px; font-weight: bold; padding-top: 20px; padding-bottom: 30px;";
  title.innerText = "FAKE NEWS WARNING";

  let content = document.createElement("p");
  content.style.cssText = "width: 80%; margin: auto;";
  content.innerText = "This website may contain fake news related to covid-19.";

  modal_content.append(close);
  modal_content.append(title);
  modal_content.append(content);
  modal.append(modal_content);

  document.body.appendChild(modal);

  window.onclick = function(event) {
    if (event.target == modal || event.target == close) {
      modal.style.display = "none";
    }
  }

}
