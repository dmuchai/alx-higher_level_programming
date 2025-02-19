$(document).ready(function () {
    $("#btn_translate").click(function () {
        const langCode = $("#language_code").val().trim();
        if (langCode !== "") {
            const apiUrl = "https://www.fourtonfish.com/hellosalut/?lang=" + langCode;
            $.get(apiUrl, function (data) {
                $("#hello").text(data.hello);
            });
        }
    });
});
