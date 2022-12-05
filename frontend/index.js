
// Reset the form after submit
function resetForm(){
    $("#myForm")[0].reset();
}

// Get data from the form and send using AJAX
function getdataAndSend(){
    // getting the data
    let data = $("#myForm").serializeArray() ;

    // Transforming the data to a single object
    let formatData = data.map(({name, value}) =>  ({
        [name]: value
        
    })).reduce((accumulator, currentValue)=>({
        ...accumulator,
        ...currentValue

    }), {});
    // Transforming the data to json format
    let jsonData = JSON.stringify(formatData)
    // console.log(jsonData);
    $.ajax({
        url: 'http://localhost:8888',
        type: "POST", 
        dataType: "json",
        crossDomain: true,
        data: jsonData,
        success: function (result) {
            console.log(result);
            resetForm()
            location.reload()
        },
        error: function () {
            console.log("error");
        }
    });
}
// Check the empty field
function emptyField(){
    let lasName = $("input[name=lastName").val();
    let firstName = $("input[name=firstName").val();
    let phone = $("input[name=telephone").val();
    let message = $("textarea#textarea").val();
    if(lasName == "" || firstName == "" || phone=="" || message==""){
        return false
    } else{
        return true
    }
}
// Submit the form
function submitForm(){
    $( "#submitBtn" ).on("click", function( event ) {
        event.preventDefault();

        if(emptyField()){
            getdataAndSend()
        }
});
}

$(document).ready( function(){
            submitForm()

});