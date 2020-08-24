




var navbar = document.getElementById("navbar");
var navpos = navbar.offsetTop;
var savebtn = document.getElementById("svform");
savebtn.addEventListener("submit",saveMsg);
function saveMsg(e){
    e.preventDefault();
    var req = new XMLHttpRequest();
    var url = 'sv_msg';
    req.open("POST",url,true);
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var mobile = document.getElementById("mobile").value;
    var subject = document.getElementById("subject").value;
    var msg = document.getElementById("msg").value;
    var csrfmiddlewaretoken=$('[name=csrfmiddlewaretoken]').val()
    req.setRequestHeader("Content-type", "application/json");
    req.setRequestHeader("X-CSRFTOKEN",csrfmiddlewaretoken)
    
    req.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            alert("Thank you for contacting us. We'll get back to you soon");
        }
    };
    
    var data = JSON.stringify({"name":name,"email":email,"mobile":mobile,"subject":subject,"message":msg});
    
    console.log(data);
    req.send(data);
}
var ham = document.getElementById("ham");
var ham1 = document.getElementById("ham1");
var ham2 = document.getElementById("ham2");
var ham3 = document.getElementById("ham3");
var clicked=1;
ham.addEventListener("click",()=>{
    if(clicked){
        navbar.style.right="0";
        ham1.style.transform="rotate(45deg) translate(7px,7px)";

        ham3.style.transform="rotate(-45deg) translate(7px,-7px)";

        ham2.style.display="none";
        clicked=0;
    }
    else{
        navbar.style.right="-100%";
        ham1.style.transform="rotate(0)";
        ham3.style.transform="rotate(0)";
        ham2.style.display="block";
        clicked=1;
    }
    
});
window.onscroll = ()=>{
    if(window.pageYOffset > navpos){
        navbar.classList.add("stickynav");
        navbar.classList.remove("navbar");
    }else{
        navbar.classList.remove("stickynav");
        navbar.classList.add("navbar");
    }
};
var pages = document.getElementsByClassName("page");
for(let i=0; i<pages.length; i++){
    pages[i].style.height = navbar.offsetHeight;
}

function initAll(){
    
    var slide = document.getElementById("slide");
    var slilink = document.getElementById("slilink");
}
var device = window.matchMedia("(min-width:900px)");
var slide_list,title_list,link_list,dest_list;
title_list=[];
link_list=[];
dest_list=[];
calling();
function calling(){
    fetch('show_slide')
    .then((resp)=>resp.json())
    .then(function(data){
        slide_list=data;
        for(var i in slide_list){
            title_list[i]=slide_list[i].title;
            link_list[i]=slide_list[i].slide;
            dest_list[i]=slide_list[i].slide_link;
        }
    })
}


var slideIndex = 1;
slideShow(slideIndex);

function plusSlides(n){
    slideShow(slideIndex += n);
}

function currentSlide(n){
    slideShow(slideIndex=n);
}
function slideShow(n){
    if(n>link_list.length){slideIndex=1;}
    if(n<1){slideIndex=link_list.length;}
    slide.src=link_list[slideIndex-1];
    slilink.href = dest_list[slideIndex-1];
}
setInterval(()=>{plusSlides(1);},5000);
const parallax = document.getElementById("parallex1");
window.addEventListener("scroll",function(){
    if(device.matches){
        var offset = window.pageYOffset;
        parallax.style.backgroundPositionY = offset*0.6 + "px";
    }
   
})



