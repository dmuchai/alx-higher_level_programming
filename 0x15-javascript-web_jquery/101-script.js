$(document).ready(function () {
    // Add item to the list
    $("#add_item").click(function () {
        $(".my_list").append("<li>Item</li>");
    });

    // Remove the last item from the list
    $("#remove_item").click(function () {
        $(".my_list li:last").remove();
    });

    // Clear all items from the list
    $("#clear_list").click(function () {
        $(".my_list").empty();
    });
});
