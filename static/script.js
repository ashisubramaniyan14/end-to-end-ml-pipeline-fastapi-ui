async function getPrediction() {
    const res = await fetch('/predict');
    const data = await res.json();

    document.getElementById("output").innerHTML = `
        <p>Symbol: ${data.symbol}</p>
        <p>Prediction: ${data.prediction}</p>
        <p>Label: ${data.prediction_label}</p>
    `;
}