$(document).ready(function() {
        $('.multi-select').select2({
            placeholder: 'Search for categories'
        });

    new WOW().init();

    //unmasking the password
    $('.pw-toggle').on('click', function() {
    	$('.pw-masking').toggleClass('masked');
    });

    //toggling tooltips for passwords
    var inputMask = $('.input-pw');
    inputMask.on('focus',function() {
    	$('.tool-tip').addClass('show-tooltip');
    	console.log('in')

    });
        
    inputMask.on('focusout',function() {
    	$('.tool-tip').removeClass('show-tooltip');
    	console.log('out')
    });

   
    $(window).on('scroll', function() {
        var dTop = $('.footer-cta').offset().top - $(this).height(),
            scTop = $(this).scrollTop();
            
        if(scTop > dTop){
            $('.buy-cta').addClass('fade-down');
        }
        else{
             $('.buy-cta').removeClass('fade-down');
        }
    })

    // $('#loginbtn').submit(function(event){
    //     $('.model-open').removeClass('model-open');
    //     console.log('clicked');
    // });
    



});