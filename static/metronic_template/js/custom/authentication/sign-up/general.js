"use strict";

// Class definition
var KTSignupGeneral = function() {
    // Elements
    var form;
    var submitButton;
    var validator;
    var passwordMeter;

    // Handle form
    var handleForm  = function(e) {
        // Init form validation rules. For more info check the FormValidation plugin's official documentation:https://formvalidation.io/
        validator = FormValidation.formValidation(
			form,
			{
				fields: {
					'first-name': {
						validators: {
							notEmpty: {
								message: ' نام اجباری میباشد'
							}
						}
                    },
                    'last-name': {
						validators: {
							notEmpty: {
								message: 'نام خوانوادگی اجباری میباشد'
							}
						}
					},
                    'phone_number': {
						validators: {
                            regexp: {
                                regexp: "^(\\+98|0)?9\\d{9}$",
                                message: 'شماره تلفن به درستی وارد نشده',
                            },
							notEmpty: {
								message: 'شماره موبایل اجباری میباشد'
							}
						}
					},
					'email': {
                        validators: {
                            regexp: {
                                regexp: /^[A-Za-z][A-Za-z0-9_]{3,29}$/,
                                message: 'نام کاربری به درستی وارد نشده',
                            },
							notEmpty: {
								message: 'وارد کردن نام کاربری اجباری میباشد'
							},
                            
						}
					},
                    'password': {
                        validators: {
                            notEmpty: {
                                message: 'وارد کردن رمز عبور اجباری میباشد '
                            },
                            callback: {
                                message: 'لطفا رمز عبور بهتری انتخاب کنید',
                                callback: function(input) {
                                    if (input.value.length > 0) {
                                        return validatePassword();
                                    }
                                }
                            }
                        }
                    },
                    'confirm-password': {
                        validators: {
                            notEmpty: {
                                message: 'وارد کردن تاییدیه رمز عبور اجباری میباشد'
                            },
                            identical: {
                                compare: function() {
                                    return form.querySelector('[name="password"]').value;
                                },
                                message: 'رمز عبور و تاییدیه یکسان نیست'
                            }
                        }
                    },
                    'toc': {
                        validators: {
                            notEmpty: {
                                message: 'قبول کردن قوانین اجباری میباشد'
                            }
                        }
                    }
				},
				plugins: {
					trigger: new FormValidation.plugins.Trigger({
                        event: {
                            password: false
                        }  
                    }),
					bootstrap: new FormValidation.plugins.Bootstrap5({
                        rowSelector: '.fv-row',
                        eleInvalidClass: '',  // comment to enable invalid state icons
                        eleValidClass: '' // comment to enable valid state icons
                    })
				}
			}
		);

        // Handle form submit
        submitButton.addEventListener('click', function (e) {
            e.preventDefault();

            validator.revalidateField('password');

            validator.validate().then(function(status) {
		        if (status == 'Valid') {
                    // Show loading indication
                    submitButton.setAttribute('data-kt-indicator', 'on');

                    // Disable button to avoid multiple click 
                    submitButton.disabled = true;

                    // Simulate ajax request
                    setTimeout(function() {
                        // Hide loading indication
                        var error = true;
                        const form_data = $(form).serialize()
                        var requesturl = form.getAttribute('action');
                        $.ajax({
                            type: 'POST',
                            url: requesturl,
                            data: form_data,
                            success: function(response) {
                              console.log(response); // پاسخ دریافتی از سرور
                            }
                          }).done(function( response ) {
                            Swal.fire({
                                text: "ثبت نام با موفقیت انجام شد",
                                icon: "success",
                                buttonsStyling: false,
                                confirmButtonText: "باشه",
                                customClass: {
                                    confirmButton: "btn btn-primary"
                                }
                            }).then(function (result) {
                                
                                   
                                                                  
                                    //form.submit(); // submit form
                                    submitButton.removeAttribute('data-kt-indicator');

                                    // Disable button to avoid multiple click 
                                    submitButton.disabled = false;
                                 
                                    location.href  =  response['redirect_url']
                                    
                                
                            })
                            
                        }).fail(function(xhr, status, errorThrown) {
                               
                        Swal.fire({
                            
                            text:"نام کاربری انتخاب شده در حال حاضر وجود دارد",
                            icon: "error",
                            buttonsStyling: false,
                            confirmButtonText: "باشه ",
                            customClass: {
                                confirmButton: "btn btn-primary"
                            }
                        }).then(function (result) {
                            if (result.isConfirmed) { 
                                
                                                              
                                submitButton.removeAttribute('data-kt-indicator');

                                // Disable button to avoid multiple click 
                                submitButton.disabled = false;
                            }
                        })

                    });

                        // Show message popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/
                
                    }, 1500);   						
                } else {
                    // Show error popup. For more info check the plugin's official documentation: https://sweetalert2.github.io/
                    Swal.fire({
                        text: "Sorry, looks like there are some errors detected, please try again.",
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

        // Handle password input
        form.querySelector('input[name="password"]').addEventListener('input', function() {
            if (this.value.length > 0) {
                validator.updateFieldStatus('password', 'NotValidated');
            }
        });
    }

    // Password input validation
    var validatePassword = function() {
        return (passwordMeter.getScore() === 100);
    }

    // Public functions
    return {
        // Initialization
        init: function() {
            // Elements
            form = document.querySelector('#kt_sign_up_form');
            submitButton = document.querySelector('#kt_sign_up_submit');
            passwordMeter = KTPasswordMeter.getInstance(form.querySelector('[data-kt-password-meter="true"]'));

            handleForm ();
        }
    };
}();

// On document ready
KTUtil.onDOMContentLoaded(function() {
    KTSignupGeneral.init();
});
