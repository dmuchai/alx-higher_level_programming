$(document).ready(function () {
    function fetchTranslation() {
        const langCode = $("#language_code").val().trim();
        if (langCode !== "") {
            const apiUrl = "https://www.fourtonfish.com/hellosalut/?lang=" + langCode;
            $.get(apiUrl, function (data) {
                $("#hello").text(data.hello);
            }).fail(function () {
                $("#hello").text("Error: Unable to fetch translation.");
            });
        }
    }

    // Trigger when the button is clicked
    $("#btn_translate").click(fetchTranslation);

    // Trigger when ENTER is pressed in the input field
    $("#language_code").keypress(function (event) {
        if (event.which === 13) { // 13 is the ENTER key code
            fetchTranslation();
        }
    });
});
