$(function() {
  $(".owl-carousel").owlCarousel({
    items: 1,
    // merge: true,
    loop: true,
    margin: 10,
    lazyLoad: true,
    // center: true,
    responsive: {
      320: {
        items: 1
      },
      560: {
        items: 2
      },
      992: {
        items: 3
      }
    }
  });
});

