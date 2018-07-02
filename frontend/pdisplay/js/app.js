(function() {
    "use strict";

    var app = angular.module('portfolioApp', []);

    app.constant('env', {
       API_URL: "http://143.215.61.186:8000/stocks/"
    });

    app.controller('PortfolioController', [ '$scope', '$log', '$http', 'env', function($scope, $log, $http, env) {
        $scope.user = {}

        $scope.fetchDetails = function() {
            $http({
                method : 'GET',
                url    : env.API_URL + $scope.user.name + '/'
            }).then(function successCallback(response){
                $log.debug(response.data)
            }, function errorCallback(response){
                $log.debug(response.data)
            });
        }

    } ]);
})();