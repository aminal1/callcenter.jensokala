// $(document).ready (function () {
//     $('.spinner-border').show();
//     var requesturl = $('#requesturl').val();
//     $.ajax({
//         url: requesturl, 
//         type: 'GET', // نوع HTTP request. مثلا GET یا POST
//         dataType: 'json', // نوع داده‌ی دریافتی
//         success: function(response) {
//             var tble= document.getElementById('kt_ecommerce_sales_table')
//             tble.className="table align-middle table-row-dashed fs-6 gy-5 dataTable no-footer"
//             $('.spinner-border').hide();
//             var tableBody = $('#tble');
//             response.forEach(function(item) {
//                 var row = $('<tr>');
//                 row.append($('<td>').text(item.id));
//                 row.append($('<td>').text(item.networker_name));
//                 row.append($('<td>').text(item.price));
//                 row.append($('<td>').text(item.price));
//                 row.append($('<td>').text(item.price));
//                 row.append($('<td>').text(item.price));
//                 row.append($('<td>').text(item.price));
//                 // row.append($('<td>').text(item.data.split('T')[0]));
//                 row.append($('<td>').text(item.status));
//                 var selectOption = $('<select>').addClass('form-control');
//                 item.call_status.forEach(function(status) {
//                     var option = $('<option>').attr('value', status.c_status_id).text(status.c_status_title);
//                     if (status.selected) {
//                         option.attr('selected', 'selected');
//                     }
//                     selectOption.append(option);
//                 });
//                 row.append($('<td>').append(selectOption));
//                 tableBody.append(row);
//             });
//         },
//         error: function(jqXHR, textStatus, errorThrown) {
//             alert('An error occurred while processing your request.');
//         },
//     });
// })

function ChangeCallStatus(select , row_id) {
    var order_id = row_id;
    var select_id = $(select ).val();
    var requesturl = $('#change_status_url').val(); 
    $.ajax({
        url:requesturl,
        method :"GET",
        data:{
            order_id:order_id,
            select_id:select_id
        },
       
    });
}



function DeleteOrder(order_id) {
         Swal.fire({
             text: "ایا از حذف کردن این سفارش مطمن هستید ؟  این کار غیر قابل بازگشت است",
             icon: "info",
             buttonsStyling: false,
             showCancelButton: true,
             confirmButtonText: "آره حذف کن",
             cancelButtonText: 'نه لغوش کن',
             customClass: {
                confirmButton: "btn btn-primary",
                cancelButton: 'btn btn-danger'
            }
         }).then(function (result) {
             if (result.isConfirmed) { 
                var csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
                
                var requesturl = $('#Delete_order').val();
                $.ajax({
                    url :requesturl,
                    method:'POST',
                    data:{
                        "csrfmiddlewaretoken":$('input[name="csrfmiddlewaretoken"]').val(),
                        "id":order_id,
                    },
                    success: function(response) {
                        var row = $(`#row_${order_id}`)
                        row.remove();
                        Swal.fire({
                            text: "سفارش شما با کد "  + order_id +"با موفقیت حذف شد",
                            icon: "success",
                            buttonsStyling: false,
                            confirmButtonText: "باشه",
                            customClass: {
                                confirmButton: "btn btn-primary"
                            }
                        });
                    },
                });
             }
         });
}

// $(document).ready(function() {
//     $("select[name='products']").click(function() {
//       var id = $(this).val();
      
//       if ($(this).find("option[value='" + id + "']").is(":selected")) {
//         var item = $('#hasan')
//         item.append("<input type='text' value='" + id + "' name='option-" + id + "'>");
//         console.log("FUCK")
//       } else {
//         $(this).parent().find("input[name='option-" + id + "']").remove();
//       }
//     });
//   });

// function CheckProduct(select){
//     console.log("FUCK")
//     var id = select.value
      
//     if ($(select).find("option[value='" + id + "']").is(":selected")) {
//         $(select).parent().append("<input type='text' value='" + id + "' id='option-" + id + "'>");
//         console.log(id)
//     } else {
//         console.log(id)
//         var inpot = document.getElementById(`option-${id}`)
//         console.log(inpot)
//         $(inpot).remove();
//     }
// }

// function OptionClick(option,id){
//     console.log(option)
//     if ($(option).is(":selected")) {

//         console.log("Fuck Yes")
//     }else{
        
//         console.log("Fuck No")
//     }

// }


function ChekBoxChek(cek) {
    
        if (cek.checked) {
            var value = $(cek).val()
            var inp = document.getElementById(value)
            var btn = document.getElementById(`btn_${value}`)
            inp.disabled = false;
            btn.disabled = false;

            
            
        }else {

            var value = $(cek).val()
            var inp = document.getElementById(value)
            var btn = document.getElementById(`btn_${value}`)
            inp.disabled = true;
            btn.disabled = true;
       

        }
      }
$("#create_order_submit").click(function (event){
    event.preventDefault();
    const form = $("#kt_modal_new_address_form");
    var submitButton = document.getElementById("create_order_submit")
    var create_user_modal =  $('#kt_modal_new_address')
    const inputs = form.find("input, textarea");
    submitButton.setAttribute('data-kt-indicator','on');

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
    var checked = 0
    $('input[name="products"]').each(function() {
        // Do whatever you want with each checkbox here
        if (this.checked) {
            checked += 1
           
        } else {
            console.log(' is not checked');
        }
     });
    if (checked === 0){
        isValid = false;
    }
    var requesturl  = $("#requesturl").val();
    if (isValid){
        $.ajax({
            url : requesturl,
            method: "POST",
            data : form.serialize(),
            success: function(response) {
                Swal.fire({
                    text: "سفارش جدید با موفقیت ثبت شد",
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
                    
                    $('#kt_modal_new_address').modal('hide')
                        
                 
                    
                    
                
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
                }).then(function (result) {
                                            
                 
                        
                    
                    submitButton.removeAttribute('data-kt-indicator');
        
                    
                    submitButton.disabled = false;
                 
                    
                    
                
            })
        }
            
        });


    }else{
        Swal.fire({
            text: "وارد کردن تمام فیلد ها اجباری میباشد و حداقل یک محصول را انتخاب کنید",
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

    };


});