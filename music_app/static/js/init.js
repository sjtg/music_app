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


// $('.select').material_select();
  }); // end of document ready
})(jQuery); // end of jQuery name space

// var header = $('header');
// var range = 200;
//
// $(window).on('scroll', function () {
//
//   var scrollTop = $(this).scrollTop(),
//       height = header.outerHeight(),
//       offset = height / 1.1,
//       calc = 1 - (scrollTop - offset + range) / range;
//
//   header.css({ 'opacity': calc });
//
//   if (calc > '1') {
//     header.css({ 'opacity': 1 });
//   } else if ( calc < '0' ) {
//     header.css({ 'opacity': 0 });
//   }
//
// });
//
// $(window).on("load",function() {
//   $(window).scroll(function() {
//     var windowBottom = $(this).scrollTop() + $(this).innerHeight();
//     $(".fade").each(function() {
//       /* Check the location of each desired element */
//       var objectBottom = $(this).offset().top + $(this).outerHeight();
//
//       /* If the element is completely within bounds of the window, fade it in */
//       if (objectBottom < windowBottom) { //object comes into view (scrolling down)
//         if ($(this).css("opacity")==0) {$(this).fadeTo(500,1);}
//       } else { //object goes out of view (scrolling up)
//         if ($(this).css("opacity")==1) {$(this).fadeTo(500,0);}
//       }
//     });
//   }).scroll(); //invoke scroll-handler on page-load
// });


// music player
$(function() {
    $('.jcarousel').jcarousel({
      wrap: 'circular'
    });
  
    $('.jcarousel-pagination').jcarouselPagination({
        item: function(page) {
            return '<li id="jcarousel-item' + page + '"><a href="#' + page + '">' + page + '</a></li>';
        }
    });
  
    $('#jcarousel-item1').addClass('active');
  
    $('.jcarousel-pagination')
    .on('jcarouselpagination:active', 'li', function() {
        $(this).addClass('active');
    })
    .on('jcarouselpagination:inactive', 'li', function() {
        $(this).removeClass('active');
    });
});

$('.jcarousel-prev').click(function() {
    $('.jcarousel').jcarousel('scroll', '-=1');
  
    $(".audio-avalanche")[0].pause();
    $(".audio-the-nights")[0].pause();
    $(".audio-dont-look-down")[0].pause();
    $(".play i").removeClass("fa-pause").addClass("fa-play");
    $(".play").removeClass("active")
  
    if ($('#jcarousel-item1').hasClass('active')) {
    $('.dont-look-down, .avalanche').removeClass('active');
    $('.the-nights').addClass('active');
    $(".song").html("The Nights");
    $(".artist").html("Avicii");
    $(".duration").html($(".audio-the-nights").duration);
  };
  
  if ($('#jcarousel-item2').hasClass('active')) {
    $('.the-nights, .avalanche').removeClass('active');
    $('.dont-look-down').addClass('active');
    $(".song").text("Don't Look Down");
    $(".artist").text("Martin Garrix");
  };
  
  if ($('#jcarousel-item3').hasClass('active')) {
    $('.the-nights, .dont-look-down').removeClass('active');
    $('.avalanche').addClass('active');
    $(".song").html("Avalanche");
    $(".artist").html("Bring Me The Horizon");
  };
});

$('.jcarousel-next').click(function() {
    $('.jcarousel').jcarousel('scroll', '+=1');
  
    $(".audio-avalanche")[0].pause();
    $(".audio-the-nights")[0].pause();
    $(".audio-dont-look-down")[0].pause();
    $(".play i").removeClass("fa-pause").addClass("fa-play");
    $(".play").removeClass("active")
  
        if ($('#jcarousel-item1').hasClass('active')) {
    $('.dont-look-down, .avalanche').removeClass('active');
    $('.the-nights').addClass('active');
    $(".song").html("The Nights");
    $(".artist").html("Avicii");
  };
  
  if ($('#jcarousel-item2').hasClass('active')) {
    $('.the-nights, .avalanche').removeClass('active');
    $('.dont-look-down').addClass('active');
    $(".song").html("Don't Look Down");
    $(".artist").html("Martin Garrix");
  };
  
  if ($('#jcarousel-item3').hasClass('active')) {
    $('.the-nights, .dont-look-down').removeClass('active');
    $('.avalanche').addClass('active');
    $(".song").html("Avalanche");
    $(".artist").html("Bring Me The Horizon");
  };
});

$(".options a").click(function() {
  $(this).toggleClass("active");
});

$(".favorite").click(function() {
  if($(".options .favorite i").hasClass("fa-heart")) {
    $(".options .favorite i").removeClass("fa-heart").addClass("fa-heart-o");
  }
  else {
    $(".options .favorite i").removeClass("fa-heart-o").addClass("fa-heart");
  }
});

$(".play").click(function() {
  $(".play").toggleClass("active");
  if($(".play i").hasClass("fa-play")) {
    $(".play i").removeClass("fa-play").addClass("fa-pause");
  }
  else {
    $(".play i").removeClass("fa-pause").addClass("fa-play");
  }
  
  if($(".play").hasClass("active") && $("#jcarousel-item3").hasClass("active")) {
    var audio = $(".audio-avalanche")[0];
    audio.play();
  } else {
    var audio = $(".audio-avalanche")[0];
    audio.pause();
    }
  
  if($(".play").hasClass("active") && $("#jcarousel-item2").hasClass("active")) {
    var audio = $(".audio-dont-look-down")[0];
    audio.play();
  } else {
    var audio = $(".audio-dont-look-down")[0];
    audio.pause();
    }
  
  if($(".play").hasClass("active") && $("#jcarousel-item1").hasClass("active")) {
    var audio = $(".audio-the-nights")[0];
    audio.play();
  } else {
    var audio = $(".audio-the-nights")[0];
    audio.pause();
    }
});

$(".volume").click(function(){
    $(".volume").removeClass("active");
    $(".volume-slider").animate({marginTop: '-150px'}, 500);
});

$(".volume-slider .close").click(function(){
    $(".volume-slider").animate({marginTop: '0px'}, 500);
})

$(".side-menu-trigger").click(function(){
    $(".side-menu").animate({marginLeft: '0px'});
    $(".volume-slider").animate({marginTop: '0px'}, 500);
}); 

$(".side-menu li a, .side-menu .close").click(function(){
    $(".side-menu").animate({marginLeft: '-310px'});
}); 

$('.volume-slider input[type="range"]').on('input', function () {
            var percent = Math.ceil(((this.value - this.min) / (this.max - this.min)) * 100);
            console.log(this.min);
            $(this).css('background', '-webkit-linear-gradient(left, #e74c3c 0%, #e74c3c ' + percent + '%, #999 ' + percent + '%)');
        });

$(".volume-slider").slider({
    min: 0,
    max: 100,
    value: 0,
    range: "min",
    animate: true,
    slide: function(event, ui) {
      setVolume((ui.value) / 100);
    }
});

function setVolume(myVolume) {
    var myMedia = document.getElementByClass('audio-avalanche');
    myMedia.volume = myVolume;
}