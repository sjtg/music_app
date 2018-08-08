// (function($){
//   $(function(){
//
//     $('.sidenav').sidenav();
//     $('.parallax').parallax();
//     $('select').material_select();
//      $('.dropdown-trigger').dropdown();
//
//   }); // end of document ready
// })(jQuery); // end of jQuery name space
(function($){
  $(function(){
    $('.dropdown-trigger').dropdown();
    $('.fixed-action-btn').floatingActionButton();
    $('.select').formSelect();
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.modal').modal();
    $('.slider').slider();
    $('.materialboxed').materialbox();
    $('.tooltipped').tooltip();
    $('html, body').animate({
      scrollTop: $(".intro").offset().top
    }, 2000);


// $('.select').material_select();
  }); // end of document ready
})(jQuery); // end of jQuery name space

var header = $('header');
var range = 200;

$(window).on('scroll', function () {

  var scrollTop = $(this).scrollTop(),
      height = header.outerHeight(),
      offset = height / 1.1,
      calc = 1 - (scrollTop - offset + range) / range;

  header.css({ 'opacity': calc });

  if (calc > '1') {
    header.css({ 'opacity': 1 });
  } else if ( calc < '0' ) {
    header.css({ 'opacity': 0 });
  }

});

$(window).on("load",function() {
  $(window).scroll(function() {
    var windowBottom = $(this).scrollTop() + $(this).innerHeight();
    $(".fade").each(function() {
      /* Check the location of each desired element */
      var objectBottom = $(this).offset().top + $(this).outerHeight();

      /* If the element is completely within bounds of the window, fade it in */
      if (objectBottom < windowBottom) { //object comes into view (scrolling down)
        if ($(this).css("opacity")==0) {$(this).fadeTo(500,1);}
      } else { //object goes out of view (scrolling up)
        if ($(this).css("opacity")==1) {$(this).fadeTo(500,0);}
      }
    });
  }).scroll(); //invoke scroll-handler on page-load
});


// music player


var audio = document.getElementById("audio-player");

$(document).ready(function() {
  $("#play-button").click(function() {
    if ($(this).hasClass("unchecked")) {
      $(this)
        .addClass("play-active")
        .removeClass("play-inactive")
        .removeClass("unchecked");
      $(".info-two")
        .addClass("info-active");
      $("#pause-button")
        .addClass("scale-animation-active");
      $(".waves-animation-one, #pause-button, .seek-field, .volume-icon, .volume-field, .info-two").show();
      $(".waves-animation-two").hide();
      $("#pause-button")
        .children('.icon')
        .addClass("icon-pause")
        .removeClass("icon-play");
      setTimeout(function() {
        $(".info-one").hide();
      }, 400);
      audio.play();
      audio.currentTime = 0;
    } else {
      $(this)
        .removeClass("play-active")
        .addClass("play-inactive")
        .addClass("unchecked");
      $("#pause-button")
        .children(".icon")
        .addClass("icon-pause")
        .removeClass("icon-play");
      $(".info-two")
        .removeClass("info-active");
      $(".waves-animation-one, #pause-button, .seek-field, .volume-icon, .volume-field, .info-two").hide();
      $(".waves-animation-two").show();
      setTimeout(function() {
        $(".info-one").show();
      }, 150);
      audio.pause();
      audio.currentTime = 0;
    }
  });
  $("#pause-button").click(function() {
    $(this).children(".icon")
      .toggleClass("icon-pause")
      .toggleClass("icon-play");

    if (audio.paused) {
      audio.play();
    } else {
      audio.pause();
    }
  });
  $("#play-button").click(function() {
    setTimeout(function() {
      $("#play-button").children(".icon")
        .toggleClass("icon-play")
        .toggleClass("icon-cancel");
    }, 350);
  });
  $(".like").click(function() {
    $(".icon-heart").toggleClass("like-active");
  });
});

function CreateSeekBar() {
  var seekbar = document.getElementById("audioSeekBar");
  seekbar.min = 0;
  seekbar.max = audio.duration;
  seekbar.value = 0;
}

function EndofAudio() {
  document.getElementById("audioSeekBar").value = 0;
}

function audioSeekBar() {
  var seekbar = document.getElementById("audioSeekBar");
  audio.currentTime = seekbar.value;
}

function SeekBar() {
  var seekbar = document.getElementById("audioSeekBar");
  seekbar.value = audio.currentTime;
}

audio.addEventListener("timeupdate", function() {
  var duration = document.getElementById("duration");
  var s = parseInt(audio.currentTime % 60);
  var m = parseInt((audio.currentTime / 60) % 60);
  duration.innerHTML = m + ':' + s;
}, false);

Waves.init();
Waves.attach("#play-button", ["waves-button", "waves-float"]);
Waves.attach("#pause-button", ["waves-button", "waves-float"]);
