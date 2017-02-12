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
