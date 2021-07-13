window.addEventListener('load', () => {
    canvas.addEventListener('mousedown', startPainting);
    canvas.addEventListener('mouseup', stopPainting);
    canvas.addEventListener('mousemove', paint);
});

const clearButton = document.getElementById('clearButton');

clearButton.addEventListener('click', () => {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const predictionCanvas = document.getElementById('predictionCanvas');
    const predictionCtx = predictionCanvas.getContext('2d');
    predictionCtx.clearRect(0, 0, predictionCanvas.width, predictionCanvas.height);

});

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

let brushCoordinates = {x:0, y:0};
let isPainting = false;

function getPosition(event){
    let rect = canvas.getBoundingClientRect();
    brushCoordinates.x = event.clientX - rect.left;
    brushCoordinates.y = event.clientY - rect.top;
}

function startPainting(event){
    isPainting = true;
    getPosition(event);
}

function stopPainting(){
    isPainting = false;
}

function paint(event){
    if (!isPainting){
        return;
    }

    ctx.beginPath();

    ctx.lineWidth = 10;
    ctx.lineCap = 'round';
    ctx.strokeStyle = 'black';

    ctx.moveTo(brushCoordinates.x, brushCoordinates.y);
    getPosition(event);
    ctx.lineTo(brushCoordinates.x , brushCoordinates.y);
    ctx.stroke();
}

