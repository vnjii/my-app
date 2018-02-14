<canvas> </canvas>


<script>
     var canvas =
     document.querySelector('canvas'),
              ctx = canvas.getContext( '2d');
          ctx.fillRect(10,10,10,10);
</script>


var canvas =
document.querySelector('canvas'),
    ctx = canvas.getContext('2d');

var resize = function ()  {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
};

window.addEventListener('resize', resize);

window.addEventListener('load', function() {

  resize();

  var pos, vel;
  pos ={
    x:10
    y:10
  };
  var loop = function () {
    ctx.clearRect (0,0, canvas.width, canvas.height);
    pos.x += vel.x;
    pos.y += vel.y;
    if (pos.x < 5 || pos.y > canvas.width)
    vel.x *= -1;
    }
    if (pos.y < 5 || pos.y > canvas.height - 5) {
      vel.y *= -1;
    }
    ctx.fillRect(pos.x - 5, pos.y - 5, 10, 10);
  };

  setInterval(loop, 1000 / 60);
});
