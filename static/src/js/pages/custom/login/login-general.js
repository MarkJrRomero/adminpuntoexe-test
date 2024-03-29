"use strict";

// Class Definition
var KTLogin = function() {
    var _login;

    var _showForm = function(form) {
        var cls = 'login-' + form + '-on';
        var form = 'kt_login_' + form + '_form';

        _login.removeClass('login-forgot-on');
        _login.removeClass('login-signin-on');
        _login.removeClass('login-signup-on');

        _login.addClass(cls);

        KTUtil.animateClass(KTUtil.getById(form), 'animate__animated animate__backInUp');
    }

    var _handleSignInForm = function() {
        var validation;

        // Init form validation rules. For more info check the FormValidation plugin's official documentation:https://formvalidation.io/
        validation = FormValidation.formValidation(
			KTUtil.getById('kt_login_signin_form'),
			{
				fields: {
					username: {
						validators: {
							notEmpty: {
								message: 'El Usuario es requerido'
							}
						}
					},
					password: {
						validators: {
							notEmpty: {
								message: 'La contraseña es Requerida'
							}
						}
					}
				},
				plugins: {
                    trigger: new FormValidation.plugins.Trigger(),
                    submitButton: new FormValidation.plugins.SubmitButton(),
                    //defaultSubmit: new FormValidation.plugins.DefaultSubmit(), // Uncomment this line to enable normal button submit after form validation
					bootstrap: new FormValidation.plugins.Bootstrap()
				}
			}
		);

        $('#kt_login_signin_submit').on('click', function () {

            validation.validate().then(function(status) {
		        if (status == 'Valid') {
                    swal.fire({
		                text: "¡Todo es genial! Ahora envía este formulario",
		                icon: "success",
		                buttonsStyling: false,
		                confirmButtonText: "Ok, Enviar!",
                        customClass: {
    						confirmButton: "btn font-weight-bold btn-light-primary"
    					}
		            }).then(function() {
						KTUtil.scrollTop();
						$('form').unbind('submit').submit();

					});
				} else {
					swal.fire({
		                text: "Lo sentimos, parece que se han detectado algunos errores, inténtalo de nuevo.",
		                icon: "error",
		                buttonsStyling: false,
		                confirmButtonText: "Ok, Entiendo!",
                        customClass: {
    						confirmButton: "btn font-weight-bold btn-light-primary"
    					}
		            }).then(function() {
						KTUtil.scrollTop();
					});
				}
		    });
        });
    }
return {
        // public functions
        init: function() {
            _login = $('#kt_login');
            _handleSignInForm();
        }
    };
}();

// Class Initialization
jQuery(document).ready(function() {
    KTLogin.init();
});
