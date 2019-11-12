function hideModal() {
    let $modal = $(".modal");
    let $body = $('body');
    $modal.removeClass("in");
    $(".modal-backdrop").remove();
    $body.removeClass('modal-open');
    $body.css('padding-right', '');
    $modal.hide();
}
