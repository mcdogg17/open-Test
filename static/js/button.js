let socket = io();
$("#button_for_test").click(function () {
    socket.emit("run_test", $("#text").val());
});
socket.on('send_result', function(res) {
        $("#res_positive").text(res[0] + ' %');
        $("#res_neutral").text(res[1] + ' %');
        $("#res_negative").text(res[2] + ' %');
});