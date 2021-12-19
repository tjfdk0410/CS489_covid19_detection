// let debugMessage = document.getElementById("debug");

window.addEventListener("load", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://localhost:8123/detect/');
  xhr.onload = () => {

    let response = JSON.parse(xhr.response);

    if (response.out == true){
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
      button1.onclick = () => {
        chrome.scripting.executeScript({
          target: { tabId: tab.id },
          function: applyEffect,
          args: [response, "highlight"]
        });
      };

      let button2 = document.createElement("button");
      button2.innerText = "Blur";
      button2.style.cssText = buttonStyle;
      button2.onclick = () => {
        chrome.scripting.executeScript({
          target: { tabId: tab.id },
          function: applyEffect,
          args: [response, "blur"]
        });
      };

      buttonBox.append(button1);
      buttonBox.append(button2);

      explainBox.append(explain1);
      explainBox.append(explain2);
      explainBox.append(buttonBox);
    }
  };
  xhr.send(tab.url);
});

function applyEffect(response, effect) {
  let tabDebug = document.createElement("p");
  let pTags = document.getElementsByTagName("p");

  for (var i = 0; i < pTags.length; i++){
    var jArray = [];

    // check if fake sentences exist in the paragraph
    for (var j =0; j < response.attention.length; j++){
      if (pTags[i].textContent.includes(response.attention[j][0])) {
        jArray.push(j);
      }
    }

    if (jArray.length > 0) {
      if (effect == "blur"){
        pTags[i].style.filter = "blur(5px)";
      }
      else {
        var remain = pTags[i].textContent;
        pTags[i].innerHTML = "";

        for (var k =0; k < jArray.length; k++){
          if (remain.includes(response.attention[jArray[k]][0])) {
            let splitted = remain.split(response.attention[jArray[k]][0]);

            pTags[i].append(splitted[0]);

            let hightlight = document.createElement("span");
            hightlight.innerText = response.attention[jArray[k]][0];

            if (response.attention[jArray[k]][1] > 0.5 && response.attention[jArray[k]][1] <= 0.6){
              hightlight.style.background = 'rgb(255, 200, 200)';
            }
            else if (response.attention[jArray[k]][1] > 0.6 && response.attention[jArray[k]][1] <= 0.7){
              hightlight.style.background = 'rgb(255, 160, 160)';
            }
            else if (response.attention[jArray[k]][1] > 0.7 && response.attention[jArray[k]][1] <= 0.8){
              hightlight.style.background = 'rgb(255, 120, 120)';
            }
            else if (response.attention[jArray[k]][1] > 0.8 && response.attention[jArray[k]][1] <= 0.9){
              hightlight.style.background = 'rgb(255, 80, 80)';
            }
            else if (response.attention[jArray[k]][1] > 0.9 && response.attention[jArray[k]][1] <= 1){
              hightlight.style.background = 'rgb(255, 40, 40)';
            }

            pTags[i].append(hightlight);
            remain = splitted[1];
          }
        }
        pTags[i].append(remain);
      }
    }
  }

  // tabDebug.innerText = response.attention.length;

  document.body.appendChild(tabDebug);
}


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
