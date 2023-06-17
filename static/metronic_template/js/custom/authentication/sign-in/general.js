"use strict";

// Class definition
var KTSigninGeneral = function() {
    // Elements
    var form;
    var submitButton;
    var validator;

    // Handle form
    var handleValidation = function(e) {
        // Init form validation rules. For more info check the FormValidation plugin's official documentation:https://formvalidation.io/
        validator = FormValidation.formValidation(
			form,
			{
				fields: {					
					'email': {
                        validators: {
                          
							notEmpty: {
								message: 'نام کاربری اجباری میباشد'
							}
						}
					},
                    'password': {
                        validators: {
                            notEmpty: {
                                message: 'رمز عبور اجباری میباشد'
                            }
                        }
                    } 
				},
				plugins: {
					trigger: new FormValidation.plugins.Trigger(),
					bootstrap: new FormValidation.plugins.Bootstrap5({
                        rowSelector: '.fv-row',
                        eleInvalidClass: '',  // comment to enable invalid state icons
                        eleValidClass: '' // comment to enable valid state icons
                    })
				}
			}
		);	
    }

    var handleSubmitDemo = function(e) {
        // Handle form submit
        submitButton.addEventListener('click', function (e) {
            // Prevent button default action
            e.preventDefault();

            // Validate form
            validator.validate().then(function (status) {
                if (status == 'Valid') {
                    // Show loading indication
                    submitButton.setAttribute('data-kt-indicator','on');

                    // Disable button to avoid multiple click 
                    submitButton.disabled = true;
                    

                    // Simulate ajax request
                    setTimeout(function() {
                        // Hide loading indication


                        
                        var email = $("input[name='email']").val();
                        var password = $("input[name='password']").val();
                        var csrf = $("input[name='csrfmiddlewaretoken']").val();
                        $.ajax({
                            url: "/api_login",
                            method: "POST",
                            data: { 
                            "email": email, 
                            "password": password,
                            "csrfmiddlewaretoken":csrf
                        } 
                        }).done(function( response ) {
                                Swal.fire({
                                    text: response['message'],
                                    icon: "success",
                                    buttonsStyling: false,
                                    confirmButtonText: "باشه",
                                    customClass: {
                                        confirmButton: "btn btn-primary"
                                    }
                                }).then(function (result) {
                                    
                                        email= "";
                                        password= "";  
                                                                      
                                        //form.submit(); // submit form
                                        submitButton.removeAttribute('data-kt-indicator');

                                        // Disable button to avoid multiple click 
                                        submitButton.disabled = false;
                                     
                                        location.href  =  response['redirect_url']
                                        
                                    
                                })
                                
                        }).fail(function(xhr, status, errorThrown) {
                            var responseJson = JSON.parse(xhr.responseText);
                            Swal.fire({
                                
                                text: responseJson['message'],
                                icon: "error",
                                buttonsStyling: false,
                                confirmButtonText: "باشه ",
                                customClass: {
                                    confirmButton: "btn btn-primary"
                                }
                            }).then(function (result) {
                                if (result.isConfirmed) { 
                                    email= "";
                                    password= "";  
                                                                  
                                    submitButton.removeAttribute('data-kt-indicator');

                                    // Disable button to avoid multiple click 
                                    submitButton.disabled = false;
                                }
                            })

                        });
                        // Show message popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/
                        // Swal.fire({
                        //     text: "You have successfully logged in!",
                        //     icon: "success",
                        //     buttonsStyling: false,
                        //     confirmButtonText: "Ok, got it!",
                        //     customClass: {
                        //         confirmButton: "btn btn-primary"
                        //     }
                        // }).then(function (result) {
                        //     if (result.isConfirmed) { 
                        //         form.querySelector('[name="email"]').value= "";
                        //         form.querySelector('[name="password"]').value= "";  
                                                              
                        //         //form.submit(); // submit form
                        //         var redirectUrl = form.getAttribute('data-kt-redirect-url');
                        //         if (redirectUrl) {
                        //             location.href = redirectUrl;
                        //         }
                        //     }
                        // });
                    }, 2000);   						
                } else {
                    // Show error popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/
                    Swal.fire({
                        text: "متاسفم شما باید نام کاربری و رمز عبور خود را وارد کنید",
                        icon: "error",
                        buttonsStyling: false,
                        confirmButtonText: "باشه ",
                        customClass: {
                            confirmButton: "btn btn-primary"
                        }
                    });
                }
            });
		});
    }

    var handleSubmitAjax = function(e) {
        // Handle form submit
        submitButton.addEventListener('click', function (e) {
            // Prevent button default action
            e.preventDefault();

            // Validate form
            validator.validate().then(function (status) {
                if (status == 'Valid') {
                    // Hide loading indication
                    submitButton.removeAttribute('data-kt-indicator');

                    // Enable button
                    submitButton.disabled = false;
                                        
                    // Check axios library docs: https://axios-http.com/docs/intro 
                    
                    $.ajax( {
                        url : '/api_login',
                        method : "POST",
                        email: form.querySelector('[name="email"]').value, 
                        password: form.querySelector('[name="password"]').value 
                    }).then(function (response) {
                        if (response) {
                            form.querySelector('[name="email"]').value= "";
                            form.querySelector('[name="password"]').value= "";  
                            console.log(response.data);
                            const redirectUrl = form.getAttribute('data-kt-redirect-url');
                            
                            if (redirectUrl) {
                                location.href = redirectUrl;
                            }
                        } else {
                            // Show error popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/
                            Swal.fire({
                                text: "Sorry, the email or password is incorrect, please try again.",
                                icon: "error",
                                buttonsStyling: false,
                                confirmButtonText: "Ok, got it!",
                                customClass: {
                                    confirmButton: "btn btn-primary"
                                }
                            });
                        }
                    }).catch(function (error) {
                        Swal.fire({
                            text: "Sorry, looks like there are some errors detected, please try again.",
                            icon: "error",
                            buttonsStyling: false,
                            confirmButtonText: "Ok, got it!",
                            customClass: {
                                confirmButton: "btn btn-primary"
                            }
                        });
                    });
                } else {
                    // Show error popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/
                    Swal.fire({
                        text: "وارد کردن رمز عبور اجباری میباشد",
                        icon: "error",
                        buttonsStyling: false,
                        confirmButtonText: "Ok, got it!",
                        customClass: {
                            confirmButton: "btn btn-primary"
                        }
                    });
                }
            });
		});
    }

    // Public functions
    return {
        // Initialization
        init: function() {
            form = document.querySelector('#kt_sign_in_form');
            submitButton = document.querySelector('#kt_sign_in_submit');
            
            handleValidation();
            handleSubmitDemo(); // used for demo purposes only, if you use the below ajax version you can uncomment this one
            //handleSubmitAjax(); // use for ajax submit
        }
    };
}();

// On document ready
KTUtil.onDOMContentLoaded(function() {
    KTSigninGeneral.init();
});
