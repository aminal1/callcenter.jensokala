$("#submit-modal-form").click(function(event) {
    // ابتدا فرم مودال را پیدا کنید
    event.preventDefault();
    console.log(this.value)
    const form = $("#modal-form");
    // فیلدهای مورد نظر فرم را بیابیم
    var submitButton = document.getElementById("submit-modal-form")
    var create_user_modal =  $('#create_user_modal')
    const inputs = form.find("input, textarea");
    submitButton.setAttribute('data-kt-indicator','on');

    // Disable button to avoid multiple click 
    submitButton.disabled = true;
    // یک جس تیمپ
    let isValid = true;

    // فیلدها را چک کنید
    inputs.each(function() {
        if ($(this).val().trim() === "") {
            $(this).addClass("is-invalid");
            isValid = false;
        } else {
            $(this).removeClass("is-invalid");
        }
    });

    // اگر فیلدها معتبر هستند، برای ارسال فرم به سمت سرور از ajax استفاده کنید
    if (isValid) {
        form_at = document.getElementById("modal-form")
        var requesturl=form_at.getAttribute('action');
    
        $.ajax({
            type: "POST",
            url: requesturl,
            data: form.serialize(),
            success: function(response) {
                console.log(response)
          
                
                Swal.fire({
                    text: "کاربر مورد نظر با موفقیت ثبت شد",
                    icon: "success",
                    buttonsStyling: true,
                    confirmButtonText: "باشه",
                    customClass: {
                        confirmButton: "btn btn-primary"
                    }
                }).then(function (result) {
                                    
                    //form.submit(); // submit form
                    submitButton.removeAttribute('data-kt-indicator');
        
                    // Disable button to avoid multiple click 
                    submitButton.disabled = false;
                    location.reload();
                    $('#kt_modal_add_user').modal('hide')
                        
                 
                    
                    
                
            })
            },
            error: function(xhr, status, error) {
                var responseJson = JSON.parse(xhr.responseText);
                Swal.fire({
                    text: responseJson['message'],
                    icon: "error",
                    buttonsStyling: false,
                    confirmButtonText: "Ok, got it!",
                    customClass: {
                        confirmButton: "btn btn-primary"
                    }
                }).then(function (result) {
                                            
                 
                        
                    //form.submit(); // submit form
                    submitButton.removeAttribute('data-kt-indicator');
        
                    // Disable button to avoid multiple click 
                    submitButton.disabled = false;
                 
                    
                    
                
            })
            }
        });
    } else {
        Swal.fire({
            text: "وارد کردن تمام فیلد ها اجباری میباشد",
            icon: "error",
            buttonsStyling: false,
            confirmButtonText: "Ok, got it!",
            customClass: {
                confirmButton: "btn btn-primary"
            }
        }).then(function (result) {
                                    
         
                                          
            //form.submit(); // submit form
            submitButton.removeAttribute('data-kt-indicator');

            // Disable button to avoid multiple click 
            submitButton.disabled = false;
         
            
            
        
    })
    }
});

function CloseModal(){
    // var create_user_modal =  $('#)
    // console.log(create_user_modal)
    // create_user_modal;
   
    $('#kt_modal_add_user').modal('hide')
    
    
}


function CloseEditModal (pk){
    $(`#kt_modal_edit_user${pk}`).modal('hide')

}
$("#submit_edit_user").click(function(event) {
   
});


function EditUser (pk){
    console.log(pk)
    // var pk =this.value
    
    var submitButton = document.getElementById(`submit_edit_user${pk}`)
    const form = $(`#edit-modal-form${pk}`);
    const inputs = form.find("input, textarea");
    submitButton.setAttribute('data-kt-indicator','on');

    // Disable button to avoid multiple click 
    submitButton.disabled = true;
    let isValid = true;

    // فیلدها را چک کنید
    inputs.each(function() {
        if ($(this).val().trim() === "") {
            $(this).addClass("is-invalid");
            isValid = false;
        } else {
            $(this).removeClass("is-invalid");
        }
    });
    if (isValid) {
        form_at = document.getElementById(`edit-modal-form${submitButton.value}`)
        var requesturl=form_at.getAttribute('action');
    
        $.ajax({
            type: "GET",
            url: requesturl,
            data: form.serialize(),
            success: function(response) {
           
               
            
                
                Swal.fire({
                    text: "کاربر مورد نظر با ادیت شد",
                    icon: "success",
                    buttonsStyling: true,
                    confirmButtonText: "Ok, got it!",
                    customClass: {
                        confirmButton: "btn btn-primary"
                    }
                }).then(function (result) {
                     
                    location.reload();               
                    //form.submit(); // submit form
                    submitButton.removeAttribute('data-kt-indicator');
        
                    // Disable button to avoid multiple click 
                    submitButton.disabled = false;
                    $('#kt_modal_add_user').modal('hide')
                        
                 
                    
                    
                
            })
            },
            error: function(xhr, status, error) {
                var responseJson = JSON.parse(xhr.responseText);
                Swal.fire({
                    text: responseJson['message'],
                    icon: "error",
                    buttonsStyling: false,
                    confirmButtonText: "Ok, got it!",
                    customClass: {
                        confirmButton: "btn btn-primary"
                    }
                }).then(function (result) {
                                            
                 
                        
                    //form.submit(); // submit form
                    submitButton.removeAttribute('data-kt-indicator');
        
                    // Disable button to avoid multiple click 
                    submitButton.disabled = false;
                 
                    
                    
                
            })
            }
        });
    } 

}



function DeleteUser(pk){
    var requesturl = $(`#deletedurl${pk}`).val();
    var row_id = $(`#row${pk}`)
    Swal.fire({
        text: "آیا از حذف این کاربر مطمن هستید؟ ",
        icon: "warning",
        showCancelButton: true,
        buttonsStyling: false,
        confirmButtonText: "بله , حذف کن",
        cancelButtonText: "نه , لغو",
        customClass: {
            confirmButton: "btn fw-bold btn-danger",
            cancelButton: "btn fw-bold btn-active-light-primary"
        }
    }).then(function (result) {
        if (result.value) {
            $.ajax({
                type: "GET",
                url: requesturl,
                
                success: function(response) {
                    
                    row_id.remove()
                
                    
                    Swal.fire({
                        text: "کاربر مورد نظر با موفقیت حذف شد",
                        icon: "success",
                        buttonsStyling: true,
                        confirmButtonText: "تایید",
                        customClass: {
                            confirmButton: "btn btn-primary"
                        }
                    })
                },
                error: function(xhr, status, error) {
                    var responseJson = JSON.parse(xhr.responseText);
                    Swal.fire({
                        text: responseJson['message'],
                        icon: "error",
                        buttonsStyling: false,
                        confirmButtonText: "باشه",
                        customClass: {
                            confirmButton: "btn btn-primary"
                        }
                    })
                }
            });   
        }                        

                        

     
        
        
    
})



}