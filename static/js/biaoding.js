



	var points=new Array();
	var sign=0;
	var c;
	var cxt;
	var img;

	//	document.getElementById("myCanvas").onclick = function(){positionObj(event,"myCanvas")};
	function positionObj(event,id){
		var thisX = document.getElementById(id).offsetLeft;
		var thisY = document.getElementById(id).offsetTop;
		alert(event.clientX);
		alert(thisX);
		alert(event.clientY);
		alert(thisY);
		x = event.clientX - thisX;
		y = event.clientY - thisY;
		document.getElementById("signal_x").innerHTML=x;
		document.getElementById("signal_y").innerHTML=y;

		points[sign]=new Array();
		points[sign][0]=x;
		points[sign][1]=y;
		sign+=1;
		drawpoints();
//		var imageData = cxt.getImageData(0,0,640,480);
//		var i=y*640*4+x*4;
//		imageData.data[i]=255;
//		imageData.data[i+1]=0;
//		imageData.data[i+2]=0;
//		imageData.data[i+3]=255;
//		cxt.putImageData(imageData,0,0);
	}


		function drawpoints(){
		cxt.fillStyle="ffffff";
		cxt.fillRect(0,0,640,480);
		cxt.drawImage(img,0,0);
		for(var i=0;i<sign;i++){
			cxt.beginPath();
			cxt.fillStyle="#FF0000";
			cxt.arc(points[i][0],points[i][1],2,0,Math.PI*2,true);
			cxt.closePath();
			cxt.fill();
		}
	}

	window.onload = function(){
        points;
        sign=0;
        c=document.getElementById("myCanvas");
        cxt=c.getContext("2d");
        img=new Image()
        img.src=IImagePath;

        img.onload=function(){
            cxt.drawImage(img,0,0);
        }


    	document.oncontextmenu = function(event){
               event.preventDefault();
        };
		document.getElementById("myCanvas").onmousedown = function(event){
			if(event.button == 2)
			{
				if(sign!=0){
					sign-=1;
				}
				drawpoints();
			}else if(event.button == 0){
				positionObj(event,"myCanvas");
			}
			return true;
		}
	}


	function post(URL,data){
		var temp = document.createElement("form");
		temp.action = URL;
		temp.method = "post";
		temp.style.display = "none";
		alert(1);
		for(var x in data){
			var opt = document.createElement("input");
			opt.name = x;
			opt.value = data[x];
			temp.appendChild(opt);
		}
		document.body.appendChild(temp);
		temp.submSit();
		return temp;
	}

$(document).ready(function(e) {
	SidebarTabHandler.Init();
});
var SidebarTabHandler={
	Init:function(){
		$(".tabItemContainer>li").click(function(){
			$(".tabItemContainer>li>a").removeClass("tabItemCurrent");
			$(".tabBodyItem").removeClass("tabBodyCurrent");
			$(this).find("a").addClass("tabItemCurrent");
			$($(".tabBodyItem")[$(this).index()]).addClass("tabBodyCurrent");
		});
	}
}