"use strict";

(function(){

    console.log('loaded');

    // Force lowercase to each input element that has class "transform-lowercase".
    Array.from(document.querySelectorAll('input.transform-lowercase')).forEach(function(item){
        item.addEventListener('input', function(e) {
            let target = e.target;
            let p = target.selectionStart;
            target.value = target.value.toLowerCase();
            target.setSelectionRange(p, p);
        });
    })

})();