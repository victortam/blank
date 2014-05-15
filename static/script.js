$(document).ready(function() {


        //name manipulation
        $("#nameform").submit(function() {

            //send data to back end
            $.post('/back_end_function', {name: $("#name").val()}, function(data) {

                //recieve data from backend
                sentence = data['sentence'];

                //append to html body
                $("body").append("<p>" + sentence + "</p>");

            });
            return false ;
        });




        //query dw
        $("#trialform").submit(function() {

            //send data to back end
            $.post('/query_data_warehouse', {date: $("#date").val()}, function(data) {

                //recieve data from backend
                trial_count = data['trial_count'];

                //append to html body
                $("body").append("<p>trial count for " + $("#date").val() + ": " + trial_count + "</p>");

            });
            return false ;
        });



 
});  