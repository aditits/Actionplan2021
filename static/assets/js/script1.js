jQuery(function ($) { "use strict";
	
	/* ========================================================================= */
	/*	Page Preloader
	/* ========================================================================= */
	
	
	window.onload = function () {
		document.getElementById('preloader').style.display = 'none';
         $("#loader").fadeOut("slow", function() {
                // will fade out the whole DIV that covers the website.
                $("#preloader").delay(300).fadeOut("slow");
            }); 
      
	}


	/* ========================================================================= */
	/*	Post image slider
	/* ========================================================================= */
	
	$("#post-thumb, #gallery-post").slick({
		infinite: true,
		arrows:false,
		autoplay: true,
  		autoplaySpeed: 4000
		
	});
	
	$("#features").slick({
		infinite: true,
		arrows:false,
		autoplay: true,
  		autoplaySpeed: 4000
	});


	/* ========================================================================= */
	/*	Menu item highlighting
	/* ========================================================================= */


	$("#navigation").sticky({
		topSpacing : 0
	});
	
 
	/* ========================================================================= */
	/*	Magnific popup
	/* =========================================================================  */
	$('.image-popup').magnificPopup({
    type: 'image',
    removalDelay: 160, //delay removal by X to allow out-animation
    callbacks: {
        beforeOpen: function () {
            // just a hack that adds mfp-anim class to markup
            this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
            this.st.mainClass = this.st.el.attr('data-effect');
        }
    },
    closeOnContentClick: true,
    midClick: true,
    fixedContentPos: false,
    fixedBgPos: true
});
	/* ========================================================================= */
	/*	Portfolio Filtering Hook
	/* =========================================================================  */

  	var mixer = mixitup('.portfolio-items-wrapper');
	
	/* ========================================================================= */
	/*	Testimonial Carousel
	/* =========================================================================  */
 
	//Init the carousel
	$("#testimonials").slick({
		infinite: true,
		arrows:false,
		autoplay: true,
  		autoplaySpeed: 4000
	});





	/* ========================================================================= */
	/*   Contact Form Validating
	/* ========================================================================= */


	$('#contact-submit').click(function (e) {

		//stop the form from being submitted
		e.preventDefault();

		/* declare the variables, var error is the variable that we use on the end
		to determine if there was an error or not */
		var error = false;
		var name = $('#name').val();
		var email = $('#email').val();
		var subject = $('#subject').val();
		var message = $('#message').val();

		/* in the next section we do the checking by using VARIABLE.length
		where VARIABLE is the variable we are checking (like name, email),
		length is a JavaScript function to get the number of characters.
		And as you can see if the num of characters is 0 we set the error
		variable to true and show the name_error div with the fadeIn effect. 
		if it's not 0 then we fadeOut the div( that's if the div is shown and
		the error is fixed it fadesOut. 
		
		The only difference from these checks is the email checking, we have
		email.indexOf('@') which checks if there is @ in the email input field.
		This JavaScript function will return -1 if no occurrence have been found.*/
		if (name.length == 0) {
			var error = true;
			$('#name').css("border-color", "#D8000C");
		} else {
			$('#name').css("border-color", "#666");
		}
		if (email.length == 0 || email.indexOf('@') == '-1') {
			var error = true;
			$('#email').css("border-color", "#D8000C");
		} else {
			$('#email').css("border-color", "#666");
		}
		if (subject.length == 0) {
			var error = true;
			$('#subject').css("border-color", "#D8000C");
		} else {
			$('#subject').css("border-color", "#666");
		}
		if (message.length == 0) {
			var error = true;
			$('#message').css("border-color", "#D8000C");
		} else {
			$('#message').css("border-color", "#666");
		}

		//now when the validation is done we check if the error variable is false (no errors)
		if (error == false) {
			//disable the submit button to avoid spamming
			//and change the button text to Sending...
			$('#contact-submit').attr({
				'disabled': 'false',
				'value': 'Sending...'
			});

			/* using the jquery's post(ajax) function and a lifesaver
			function serialize() which gets all the data from the form
			we submit it to send_email.php */
			$.post("sendmail.php", $("#contact-form").serialize(), function (result) {
				//and after the ajax request ends we check the text returned
				if (result == 'sent') {
					//if the mail is sent remove the submit paragraph
					$('#cf-submit').remove();
					//and show the mail success div with fadeIn
					$('#mail-success').fadeIn(500);
				} else {
					//show the mail failed div
					$('#mail-fail').fadeIn(500);
					//re enable the submit button by removing attribute disabled and change the text back to Send The Message
					$('#contact-submit').removeAttr('disabled').attr('value', 'Send The Message');
				}
			});
		}
	});

});
// End Jquery Function


	/* ========================================================================= */
	/*	Animated section
	/* ========================================================================= */

	var wow = new WOW(
		{
		  offset:       100,          // distance to the element when triggering the animation (default is 0)
		  mobile:       false      // trigger animations on mobile devices (default is true)
		}
	 );
	 wow.init();


	/* ========================================================================= */
	/*	Smooth Scroll
	/* ========================================================================= */
	var scroll = new SmoothScroll('a[href*="#"]');



	/* ========================================================================= */
	/*	Google Map Customization
	/* =========================================================================  */

	function initialize() {

		var myLatLng = new google.maps.LatLng(22.333851, 91.812256);

		var roadAtlasStyles = [{
			"featureType": "landscape",
			"elementType": "geometry.fill",
			"stylers": [{
				"color": "#2F3238"
			}]
		}, {
			"elementType": "labels.text.fill",
			"stylers": [{
				"color": "#FFFFFF"
			}]
		}, {
			"elementType": "labels.text.stroke",
			"stylers": [{
				"visibility": "off"
			}]
		}, {
			"featureType": "road",
			"elementType": "geometry.fill",
			"stylers": [{
				"color": "#50525f"
			}]
		}, {
			"featureType": "road",
			"elementType": "geometry.stroke",
			"stylers": [{
				"visibility": "on"
			}, {
				"color": "#808080"
			}]
		}, {
			"featureType": "poi",
			"elementType": "labels",
			"stylers": [{
				"visibility": "off"
			}]
		}, {
			"featureType": "transit",
			"elementType": "labels.icon",
			"stylers": [{
				"visibility": "off"
			}]
		}, {
			"featureType": "poi",
			"elementType": "geometry",
			"stylers": [{
				"color": "#808080"
			}]
		}, {
			"featureType": "water",
			"elementType": "geometry.fill",
			"stylers": [{
				"color": "#3071a7"
			}, {
				"saturation": -65
			}]
		}, {
			"featureType": "road",
			"elementType": "labels.icon",
			"stylers": [{
				"visibility": "off"
			}]
		}, {
			"featureType": "landscape",
			"elementType": "geometry.stroke",
			"stylers": [{
				"color": "#bbbbbb"
			}]
		}];

		var mapOptions = {
			zoom: 14,
			center: myLatLng,
			disableDefaultUI: true,
			scrollwheel: false,
			navigationControl: false,
			mapTypeControl: false,
			scaleControl: false,
			draggable: false,
			mapTypeControlOptions: {
				mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'roadatlas']
			}
		};

		var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);


		var marker = new google.maps.Marker({
			position: myLatLng,
			map: map,
			title: '',
		});


		google.maps.event.addListener(marker, 'click', function () {
			infowindow.open(map, marker);
		});

		var styledMapOptions = {
			name: 'US Road Atlas'
		};

		var usRoadMapType = new google.maps.StyledMapType(
			roadAtlasStyles, styledMapOptions);

		map.mapTypes.set('roadatlas', usRoadMapType);
		map.setMapTypeId('roadatlas');
	}

	google.maps.event.addDomListener(window, "load", initialize);




	// js for counter//

jQuery(function ($) {
	// custom formatting example
	$('.count-number').data('countToOptions', {
	  formatter: function (value, options) {
		return value.toFixed(options.decimals).replace(/\B(?=(?:\d{3})+(?!\d))/g, ',');
	  }
	});
	
	// start all the timers
	$('.timer').each(count);  
	
	function count(options) {
	  var $this = $(this);
	  options = $.extend({}, options || {}, $this.data('countToOptions') || {});
	  $this.countTo(options);
	}
  });
  
  (function($){
	  $(window).on("load",function(){
		  $(document).scrollzipInit();
		  $(document).rollerInit();
	  });
	  $(window).on("load scroll resize", function(){
		  $('.numscroller').scrollzip({
			  showFunction    :   function() {
									  numberRoller($(this).attr('data-slno'));
								  },
			  wholeVisible    :     false,
		  });
	  });
	  $.fn.scrollzipInit=function(){
		  $('body').prepend("<div style='position:fixed;top:0px;left:0px;width:0;height:0;' id='scrollzipPoint'></div>" );
	  };
	  $.fn.rollerInit=function(){
		  var i=0;
		  $('.numscroller').each(function() {
			  i++;
			 $(this).attr('data-slno',i); 
			 $(this).addClass("roller-title-number-"+i);
		  });        
	  };
	  $.fn.scrollzip = function(options){
		  var settings = $.extend({
			  showFunction    : null,
			  hideFunction    : null,
			  showShift       : 0,
			  wholeVisible    : false,
			  hideShift       : 0,
		  }, options);
		  return this.each(function(i,obj){
			  $(this).addClass('scrollzip');
			  if ( $.isFunction( settings.showFunction ) ){
				  if(
					  !$(this).hasClass('isShown')&&
					  ($(window).outerHeight()+$('#scrollzipPoint').offset().top-settings.showShift)>($(this).offset().top+((settings.wholeVisible)?$(this).outerHeight():0))&&
					  ($('#scrollzipPoint').offset().top+((settings.wholeVisible)?$(this).outerHeight():0))<($(this).outerHeight()+$(this).offset().top-settings.showShift)
				  ){
					  $(this).addClass('isShown');
					  settings.showFunction.call( this );
				  }
			  }
			  if ( $.isFunction( settings.hideFunction ) ){
				  if(
					  $(this).hasClass('isShown')&&
					  (($(window).outerHeight()+$('#scrollzipPoint').offset().top-settings.hideShift)<($(this).offset().top+((settings.wholeVisible)?$(this).outerHeight():0))||
					  ($('#scrollzipPoint').offset().top+((settings.wholeVisible)?$(this).outerHeight():0))>($(this).outerHeight()+$(this).offset().top-settings.hideShift))
				  ){
					  $(this).removeClass('isShown');
					  settings.hideFunction.call( this );
				  }
			  }
			  return this;
		  });
	  };
	  function numberRoller(slno){
			  var min=$('.roller-title-number-'+slno).attr('data-min');
			  var max=$('.roller-title-number-'+slno).attr('data-max');
			  var timediff=$('.roller-title-number-'+slno).attr('data-delay');
			  var increment=$('.roller-title-number-'+slno).attr('data-increment');
			  var numdiff=max-min;
			  var timeout=(timediff*1000)/numdiff;
			  //if(numinc<10){
				  //increment=Math.floor((timediff*1000)/10);
			  //}//alert(increment);
			  numberRoll(slno,min,max,increment,timeout);
			  
	  }
	  function numberRoll(slno,min,max,increment,timeout){//alert(slno+"="+min+"="+max+"="+increment+"="+timeout);
		  if(min<=max){
			  $('.roller-title-number-'+slno).html(min);
			  min=parseInt(min)+parseInt(increment);
			  setTimeout(function(){numberRoll(eval(slno),eval(min),eval(max),eval(increment),eval(timeout))},timeout);
		  }else{
			  $('.roller-title-number-'+slno).html(max);
		  }
	  }
  })(jQuery);


//js for faq//

var acc = document.getElementsByClassName("faq1");
				var i;

				for (i = 0; i < acc.length; i++) {
					acc[i].addEventListener("click", function () {
						this.classList.toggle("active");
						var panel1 = this.nextElementSibling;
						if (panel1.style.maxHeight) {
							panel1.style.maxHeight = null;
						} else {
							panel1.style.maxHeight = panel1.scrollHeight + "px";
						}
					});
				}


    