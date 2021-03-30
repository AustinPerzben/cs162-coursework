$('#makeTask').on('show.bs.modal', function (e) {
    var title = $(e.relatedTarget).data('title');
    var content = $(e.relatedTarget).data('content');
    // var panel = $(e.relatedTarget).data('panel');
    $(e.currentTarget).find('input[name="taskTitle"]').val(title);
    $(e.currentTarget).find('input[name="taskContent"]').val(content);
    // $(e.currentTarget).find('input[name="panel"]').val(panel);
});
