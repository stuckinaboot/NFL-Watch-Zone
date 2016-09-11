$(function () {
    var obtainPlayerData = function (callback) {
        var file = './players_from_updates.txt'
        // var file = './nfl-players2.txt';

        playerMap = {};
        $.getJSON(file, function (json) {
            var allPlayersJSON = json;

            $.each(allPlayersJSON, function (index, player) {
                playerMap[player['player']] = 
                {
                    pos: player['pos'],
                    team: player['team'],
                };
            });

            callback (playerMap);
        }).fail(function (a, b, err) {
            alertify.error('Failed loading players - ' + err); 
        });

        // playerMap = {};
        // $.ajax({
        //     url: file,
        //     type: 'GET',
        //     dataType: 'jsonp',
        //     jsonpCallback: 'callback',
        //     async: true,
        //     success: function (data) { 
        //         var allPlayersJSON = data;

        //         $.each(allPlayersJSON['list'], function (index, player) {
        //             playerMap[player['player']] = 
        //             {
        //                 pos: player['pos'],
        //                 team: player['team'],
        //             };
        //         });

        //         callback (playerMap);
        //     },
        //     error: function (data, err) { 
        //         alertify.error('Failed loading players - ' + err); 
        //     },
        // });
    };
    window.PlayerHandler = obtainPlayerData;
});