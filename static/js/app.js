// Handle on click of the button
function onSubmitClicked() {

    var text_val = $("#inptextbox1").val();

    if (text_val != undefined && text_val != null && text_val != "") {
        json_body = {
            "text_input": text_val
        }

        console.log("Submit button clicked");

        // var url = "http://127.0.0.1:5000/predict_delivery_date"; // local url
        var url = "/get_grpc_response"; //hosted server url

        var server_resp_div = document.getElementById("server_resp_div");

        $.ajax({
            type: "POST",
            url: url,
            data: JSON.stringify(json_body),
            contentType: "application/json",
            success: function (data) {
                console.log(data);
                server_resp_div.innerHTML = "<span>Server Response: " + data['server_response'] + "</span>";
                $('#server_resp_div').show();
            },
            error: function(err) {
                console.log("Server returned error")
            }
        });
    } else {
        alert("No data entered");
    }
}

function onPageLoad() {
    console.log("document loaded");
}

window.onload = onPageLoad;