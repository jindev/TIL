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
});

var forEx = new Vue({
  el: '#forEx',
  data: {
    todos: [
      {text: '튜토리얼'},
      {text: '실전'},
      {text: '마무리'},
    ]
  }
});
