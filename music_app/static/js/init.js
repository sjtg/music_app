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



// music player
