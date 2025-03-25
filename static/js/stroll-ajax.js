$(document).ready(function() {
    $('#like_walk_btn').click(function() {
        var walkIdVar;
        walkIdVar = $(this).attr('data-walkid');

        $.get('/stroll/like_walk/',
            {'walk_id': walkIdVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_walk_btn').hide();
            }
        )
    });

    $('#like_question_btn').click(function() {
        var questionIdVar;
        questionIdVar = $(this).attr('data-questionid');

        $.get('/stroll/like_question/',
            {'question_id': questionIdVar},
            function(data) {
                $('#like_count').html(data);
                $('#like_question_btn').hide();
            }
        )
    });
});
