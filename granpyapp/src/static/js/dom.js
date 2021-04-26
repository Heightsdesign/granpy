//var input = document.querySelector('input[type="text"]');
//var submitbtn = document.querySelector('input[type="submit"]');

//submitbtn.addEventListener('click', function(){

    //console.log(input.value);
    
//});

function submit_entry(){

    var question = document.querySelector('input[type="text"]');

    //var entry = {
        //input: question.value
    //};

    fetch(`${window.origin}/question/`, {
        method: "POST",
        credentials: "include",
        body : JSON.stringify(question.value),
        cache : "no-cache",
        headers : new Headers({
            "content-type" : "application/json"
        })
    })

    console.log(question.value);
};
