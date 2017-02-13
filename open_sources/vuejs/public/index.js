var app = new Vue({
  el: '#app',
  data: {
    name: 'Vue'
  }
});

var directiveEx = new Vue({
  el: '#directiveEx',
  data: {
    name: 'directive text',
    htmlEx: '<i>hi html</i>',
    visible: true,
    ifValue: 0
  }
});

var bindEx = new Vue({
  el: '#bindEx',
  data: {
    name: 'Vue',
    smile: false,

    feelsGood: 'https://imgh.us/feelsgood_1.jpg',
    feelsBad: 'http://imgh.us/feelsbad.jpg'
  }
})
