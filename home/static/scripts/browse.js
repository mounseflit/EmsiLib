
var nblock = 2;
var add_remove = 36;

$(".referenceblock:gt(" + nblock + ")").hide();

function showmore() {

  if ((nblock+1) < $('.referenceblock').length)
    nblock = nblock + add_remove;

  $(".referenceblock").fadeIn();
  $(".referenceblock:gt(" + nblock + ")").hide();

};

function showless() {

  if (nblock > add_remove) {
    nblock = nblock - add_remove;
  }

  $(".referenceblock:gt(" + nblock + ")").fadeOut();

};


var startStatus = "less";

  function toggler() {
  
    
      if (startStatus == "less") {
        showless();
        document.getElementById("bt").innerText = "Show More";
        startStatus = "more";
      } else if (startStatus == "more") {
        showmore();
        document.getElementById("bt").innerText = "Show Less";
        startStatus = "less";
      }
    }
  
window.onload = function(){
        toggler();
      };