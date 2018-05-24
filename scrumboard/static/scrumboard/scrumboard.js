(function(){
    'use strict';

    angular.module('scrumboard.demo', [])
        .controller('ScrumboardController', [ '$scope', ScrumboardController]);

    function ScrumboardController($scope) {
        $scope.add = function (list, title) {
            var card = {
                title: title
            };
            list.cards.push(card);
        };
        
        
    }
}());
