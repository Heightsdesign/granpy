
(function() {
    var Message;
    Message = function (arg) {
        this.text = arg.text, this.message_side = arg.message_side;
        this.draw = function (_this) {
            return function () {
                var $message;
                $message = $($('.message_template').clone().html());
                $message.addClass(_this.message_side).find('.text').html(_this.text);
                $('.messages').append($message);
                return setTimeout(function () {
                    return $message.addClass('appeared');
                }, 0);
            };
        }(this);
        return this;
    };

    $(function () {
        var getMessageText, message_side, sendMessage
        message_side = 'right';
        getMessageText = function () {
            var $message_input;
            $message_input = $('.message_input');
            return $message_input.val();
        };

        sendMessage = function (text, side) {
            var $messages, message;
            $('.message_input').val('');
            $messages = $('.messages');
            message_side = side;
            message = new Message({
                text: text,
                message_side: message_side,
            });

            message.draw();
            return $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
        };

        $('.send_message').click(function (e) {

                var user_input = $('.message_input').val();

                sendMessage(getMessageText(), 'right');

                fetch(`${window.origin}/question/`, {
                    method: "POST",
                    credentials: "include",
                    body : JSON.stringify(user_input),
                    cache : "no-cache",
                    headers : new Headers({
                        "content-type" : "application/json"
                    })
                })

                .then( function (response){
                    var granResponse = response.json();
                    
                    granResponse.then(function (data){

                        console.log(data);

                        if (data['status'] === 'OK'){

                            var granpy_res = data['granpyMessage'] + data['wikiresult'];

                            sendMessage(granpy_res, 'left');

                            var url_str = 'Pour en savoir plus : ' + JSON.stringify(data['wikiurl']);

                            var newdiv = document.createElement('div');   
                            var message_template = document.getElementsByClassName('message_template')[0];

                            newdiv.setAttribute("id", "map");   

                            //message_template.insertBefore(newdiv,message_template.lastChild) //OR insert it

                            initMap = function(latitude, longitude) {

                                document.getElementById("map").style.height = '300px';
                                document.getElementById("map").style.width = '100%';

                                latitude = data['lat'];
                                longitude = data['long'];
                                var options = {
                                    center: { lat: latitude, lng:longitude },
                                    zoom: 17
                                };
                                var map = new google.maps.Map(document.getElementById("map"), options);
                                var marker = new google.maps.Marker({position:{lat: latitude, lng: longitude}, map:map});
                            };

                            message_template.appendChild(newdiv);

                            sendMessage(url_str, 'left');
                            initMap();
                            
                        } else {
                            var warningMessage = data['warningMessage'];
                            sendMessage(warningMessage, 'left');
                        }
                    newdiv.remove()
                    });
                
                });
        });

        sendMessage("Comme nous disions jadis, bien l'bonjour !", 'left');
        });

}.call(this)); 
