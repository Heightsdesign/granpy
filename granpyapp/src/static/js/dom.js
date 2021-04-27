
function submit_entry(){

    var question = document.querySelector('input[type="text"]');

    fetch(`${window.origin}/question/`, {
        method: "POST",
        credentials: "include",
        body : JSON.stringify(question.value),
        cache : "no-cache",
        headers : new Headers({
            "content-type" : "application/json"
        })
    })

    .then( function (response){
        if(response.status !== 200){
            console.log(response.warningMessage)
        }

        response.json().then(function (data){

            console.log(data)
        })
    })


    console.log(question.value);
};
