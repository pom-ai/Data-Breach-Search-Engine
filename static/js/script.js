$(document).ready(function() {
  $('#search-form').submit(function(event) {
    event.preventDefault();
    var query = $('#search-input').val();
    $.ajax({
      url: '/search',
      data: {'query': query},
      success: function(response) {
        $('#results').html(response);
      }
    });
  });
});