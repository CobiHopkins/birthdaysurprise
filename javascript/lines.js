//Function for drawing x amount of lines of random length.

export function drawLines(amount) {

  var canvas = document.getElementById('firework');
  var ctx = canvas.getContext('2d');

  ctx.beginPath()
  ctx.moveTo(getPath(), getPath());
  ctx.lineTo(getPath(), posY);
  ctx.strokeStyle = '#' + getColour();
  ctx.stroke();

}
