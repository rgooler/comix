$(document).on('swipeleft swiperight', function (event) {
 if(event.type == 'swiperight') {
  var prevpage = '#' + $.mobile.activePage.prev('div[data-role="page"]')[0].id;
  $.mobile.changePage(prevpage, {
   transition: 'slide',
   reverse: true
  });
 }

 if(event.type == 'swipeleft') {
  var nextpage = '#' + $.mobile.activePage.next('div[data-role="page"]')[0].id;
  $.mobile.changePage(nextpage, {
   transition: 'slide',
   reverse: false
  });
 }
});