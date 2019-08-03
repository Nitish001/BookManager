$("document").ready(function(){
    $("#search_but").click(function(){
        var message = $("#search").val();
        alert("hello");
        $.ajax({
            url: "/search/"+message,
            type: "GET",
            contentType: "application/json",
            data: JSON.stringify({"message": message})
        }).done(function(data) {
            console.log(message);
            //redirect
            window.location.href = "/search/"+message;
        });
    });
});
$("document").ready(function(){
    $("#insert_button").click(function(){
        var isbn = $("#isbn").val();
        var title =$('#title').val();
        var count = $('#count').val();
//        alert(isbn);
//        alert(title);
//        alert(count);
//        all.push([isbn,title,count]);
    $.ajax({
        url: '/insert',
        type: 'POST',
//        contentType: "application/json",
        data: { 'field1': isbn, 'field2' : title , 'field3' : count}
    }).done(function(data) {
//                console.log(data);
                //redirect
                window.location.href = "/";
            });
    });
});

