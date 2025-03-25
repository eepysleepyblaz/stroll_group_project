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

    
    $('#delete_walk_btn').click(function() {
        var walkIdVar;
        walkIdVar = $(this).attr('data-walkid');

        $.get('/stroll/delete_walk/',
            {'walk_id': walkIdVar},
            function(data) {
                $('.walk_screen').html("This walk has been deleted.");
            }
        )
    });

    $('#delete_question_btn').click(function() {
        var questionIdVar;
        questionIdVar = $(this).attr('data-questionid');

        $.get('/stroll/delete_question/',
            {'question_id': questionIdVar},
            function(data) {
                $('.question_screen').html("This question has been deleted.");
                $('#comments_section').hide();
            }
        )
    });

    $('.delete_question_comment_btn').click(function() {
        var questionCommentClassVar;
        questionCommentClassVar = $(this).attr('data-questioncommentclass');

        $.get('/stroll/delete_question_comment/',
            {'question_comment_class': questionCommentClassVar},
            function(data) {
                $(`#${questionCommentClassVar}`).html("<strong>This comment has been deleted</strong>");
            }
        )
    });

    $('.delete_walk_comment_btn').click(function() {
        var walkCommentClassVar;
        walkCommentClassVar = $(this).attr('data-walkcommentclass');

        $.get('/stroll/delete_walk_comment/',
            {'walk_comment_class': walkCommentClassVar},
            function(data) {
                $(`#${walkCommentClassVar}`).html("<strong>This comment has been deleted</strong>");
            }
        )
    });
});
