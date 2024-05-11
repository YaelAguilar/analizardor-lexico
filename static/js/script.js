document.querySelector("form").onsubmit = async function (e) {
  e.preventDefault();
  
  const formData = new FormData(this);
  const fileInput = document.getElementById('fileInput');
  const codeArea = document.getElementById('code');

  if (fileInput.files.length > 0) {
    const file = fileInput.files[0];
    const reader = new FileReader();
    reader.onload = async function (event) {
      codeArea.value = event.target.result;
      await analyzeCode(formData);
    };
    reader.readAsText(file);
  } else {
    await analyzeCode(formData);
  }
};

async function analyzeCode(formData) {
  const code = formData.get("code");
  const response = await fetch("/analyze", {
    method: "POST",
    body: formData,
  });
  const result = await response.json();

  const inputCodeDiv = document.getElementById("inputCode");
  inputCodeDiv.innerHTML = "";
  result.forEach(token => {
    inputCodeDiv.innerHTML += `${token.value}<br>`;
  });

  const resultBody = document.getElementById("resultBody");
  resultBody.innerHTML = "";
  result.forEach((token, index) => {
    const row = document.createElement("tr");
    const cellLine = document.createElement("td");
    const cellToken = document.createElement("td");
    cellLine.innerText = `LÍNEA ${index + 1}`;
    cellToken.innerText = `<${token.type}> ${token.value}`;
    row.appendChild(cellLine);
    row.appendChild(cellToken);
    resultBody.appendChild(row);
  });
}
