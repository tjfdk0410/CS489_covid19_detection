window.addEventListener("load", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://localhost:8123/detect/');
  xhr.onload = () => {
    if (xhr.responseText === 'fake'){
      document.body.style.height = '320px';

      let detectMessage = document.getElementById("detectMessage");
      detectMessage.innerHTML = "Fake News Warning!";
      detectMessage.style.color = 'red';

      let image = document.getElementById("image");
      image.remove();

      let explainBox = document.getElementById("explainBox");

      let explainStyle = "padding-left: 10px; padding-right: 10px; font-size: 15px;";

      let explain1 = document.createElement("p");
      explain1.innerText = "This website contains fake news related to covid-19 with a high probability.";
      explain1.style.cssText = explainStyle;

      let explain2 = document.createElement("p");
      explain2.innerText = "If you want to know specifically which sentences are fake, click this button.";
      explain2.style.cssText = explainStyle;

      let buttonBox = document.createElement("div");
      buttonBox.style.cssText = "width: 290px; height: 50px; margin: auto; padding-bottom: 15px; display: flex; flex-direction: row; justify-content: center;";

      let buttonStyle = "width: 100px; height: 50px; border-radius: 10px; margin: auto";

      let button1 = document.createElement("button");
      button1.innerText = "Highlight";
      button1.style.cssText = buttonStyle;

      let button2 = document.createElement("button");
      button2.innerText = "Blur";
      button2.style.cssText = buttonStyle;

      buttonBox.append(button1);
      buttonBox.append(button2);

      explainBox.append(explain1);
      explainBox.append(explain2);
      explainBox.append(buttonBox);


      // chrome.scripting.executeScript({
      //   target: { tabId: tab.id },
      //   function: popupWarning,
      // });
    }
  };
  xhr.send(tab.url);
});

// Not Used
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
