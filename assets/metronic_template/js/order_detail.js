

function convert_to_en(number ,type) {
    String.prototype.getBaseConversionNumber = function(label){
        const faDigits = ['۱','۲','۳','۴','۵','۶','۷','۸','۹','۰'];
        const enDigits = ['1','2','3','4','5','6','7','8','9','0'];
        const arDigits = ['٠','٩','٨','٧','٦','٥','٤','٣','٢','١']
         
        var whichDigit = {};
         
        switch(label){
          case 'fa':
            whichDigit[label] = faDigits;
          break;
          case 'en':
            whichDigit[label] = enDigits;
          break; 
          case 'ar':
            whichDigit[label] = arDigits;
          break;
          case 'all':
            whichDigit = {"fa" : faDigits, "en" : enDigits, "ar" : arDigits};
          break;
          default:
            whichDigit = [];
        }
         
        return whichDigit;
      }
       
       
      String.prototype.CvnFromTo = function(fromDigits,toDigits,str){
        var str = str == undefined ? this : str;
        for(var i=0;i<toDigits.length;i++){
          const currentFromDigit = fromDigits[i];
          const currentToDigit = toDigits[i];
          const regex = new RegExp(currentFromDigit,'g');
          str = str.replace(regex, currentToDigit);
        }
        return str;
      }
       
      String.prototype.convertDigits = function(to){
        let str = this;
        const toCvn = (this.getBaseConversionNumber(to))[to];
        const allDigits = this.getBaseConversionNumber("all");
         
        delete allDigits[to];
         
        const Objkeys = Object.keys(allDigits);
        for(var i=0;i<Objkeys.length;i++){
          const currentKey = Objkeys[i];
          const fromCvn = allDigits[currentKey];
          str = this.CvnFromTo(fromCvn,toCvn,str)
        }
        return str;
      }
       
      const myNumber = number
      const intFa = myNumber.toString().convertDigits("fa");
      const intAr = myNumber.toString().convertDigits("ar");
      const intUs = intFa.convertDigits("en");
       
    //   console.log(intFa); // ۹۸۷۶۵۴۳۲۱
    //   console.log(intAr); // ٩٨٧٦٥٤٣٢١
    //   console.log(intUs); // 987654321
      if(type == true){

          return intUs;
      }else{
        return intFa;
      }
  }

function Call_Status(select) {
  var requesturl = $('#change_call_status_order').val();
  $.ajax({
    url:requesturl,
    method:"GET",
    data:{
      call_status:$(select).val(),

    },
    success:function(response){
      Swal.fire({
        text: "با موفقیت انجام شد",
        icon: "success",
        buttonsStyling: true,
        confirmButtonText: "باشه",
        customClass: {
            confirmButton: "btn btn-primary"
        }
    })
    }
  })
  
}



function Create_Addres_Order(){
  const form = $('#create_addres_order_form');
  var submitButton= document.getElementById('create_addres_order');
  submitButton.setAttribute('data-kt-indicator','on');
  submitButton.disabled = true;
  var requesturl = $('#create_addres_order').val();
  $.ajax({
    url : requesturl,
    method : 'POST',
    data:form.serialize(),
    success: function(response) {
      submitButton.removeAttribute('data-kt-indicator');
      // Disable button to avoid multiple click 
      submitButton.disabled = false;
      $('#kt_modal_new_address').modal('hide');
      Swal.fire({
        text: "با موفقیت انجام شد",
        icon: "success",
        buttonsStyling: true,
        confirmButtonText: "باشه",
        customClass: {
            confirmButton: "btn btn-primary"
        }}).then(function (result) {
          location.reload();
        })
        setTimeout(function(){
          location.reload();
          
      }, 4000);
    }

  })
}



// $('status_call_order').on('change', function(){
//     console.log($(this).val(),"!@%$!@%");
// })

$(document).ready(function() {
  // 



      $('#status_order').on('change', function(){

          var requesturl = $('#change_status_order').val();
          $.ajax({
            url:requesturl,
            method:"GET",
            data:{
              status_order:$(this).val(),

            },
            success:function(response){
              Swal.fire({
                text: "با موفقیت انجام شد",
                icon: "success",
                buttonsStyling: true,
                confirmButtonText: "باشه",
                customClass: {
                    confirmButton: "btn btn-primary"
                }
            })
              
            }
          })
      })

 
      $('#craete_product_submit').click(function(event){
        
        event.preventDefault();
        const form = $('#kt_modal_new_product_form')

        var submitButton = document.getElementById("craete_product_submit")
        var create_product_modal =  $('#kt_modal_new_product')
        const inputs = form.find("input, textarea");
        submitButton.setAttribute('data-kt-indicator','on');
        submitButton.disabled = true;
        var rurlcreate_product = $('#rurlcreate_product').val();
        requesturl = $('#rurl_pro_to_order').val();

        main_data = form.serialize();
        main_data['count'] = $('.count').val()
    
        $.ajax({
          url:requesturl,
          method:'POST',
          data:main_data,
          success: function(response){
              isvalid = true 
              
     
        
            //  });
          Swal.fire({
              text: "با موفقیت انجام شد",
              icon: "success",
              buttonsStyling: true,
              confirmButtonText: "باشه",
              customClass: {
                  confirmButton: "btn btn-primary"
              }}).then(function (result) {
                location.reload();
              })
          setTimeout(function(){
              location.reload();
              
          }, 4000);
        
          },

        });
      });


      $.ajax({
        url: $('#rurl_getorder_price').val(),
        method : 'GET',
       
        datatype : 'json',
        success: function(response) {
          price = convert_to_en(number=response['order_price'],type=false)

          var all_price1 = document.getElementById('all_price1')
          var all_price2 = document.getElementById('all_price2')
          all_price1.innerText =price
          all_price2.innerText =price

        }
      });
  

});


function convert_to_en2(number ,type) {
  String.prototype.getBaseConversionNumber = function(label){
      const faDigits = ['۱','۲','۳','۴','۵','۶','۷','۸','۹','۰'];
      const enDigits = ['1','2','3','4','5','6','7','8','9','0'];
      const arDigits = ['٠','٩','٨','٧','٦','٥','٤','٣','٢','١']
       
      var whichDigit = {};
       
      switch(label){
        case 'fa':
          whichDigit[label] = faDigits;
        break;
        case 'en':
          whichDigit[label] = enDigits;
        break; 
        case 'ar':
          whichDigit[label] = arDigits;
        break;
        case 'all':
          whichDigit = {"fa" : faDigits, "en" : enDigits, "ar" : arDigits};
        break;
        default:
          whichDigit = [];
      }
       
      return whichDigit;
    }
     
     
    String.prototype.CvnFromTo = function(fromDigits,toDigits,str){
      var str = str == undefined ? this : str;
      for(var i=0;i<toDigits.length;i++){
        const currentFromDigit = fromDigits[i];
        const currentToDigit = toDigits[i];
        const regex = new RegExp(currentFromDigit,'g');
        str = str.replace(regex, currentToDigit);
      }
      return str;
    }
     
    String.prototype.convertDigits = function(to){
      let str = this;
      const toCvn = (this.getBaseConversionNumber(to))[to];
      const allDigits = this.getBaseConversionNumber("all");
       
      delete allDigits[to];
       
      const Objkeys = Object.keys(allDigits);
      for(var i=0;i<Objkeys.length;i++){
        const currentKey = Objkeys[i];
        const fromCvn = allDigits[currentKey];
        str = this.CvnFromTo(fromCvn,toCvn,str)
      }
      return str;
    }
     
    const myNumber = number
    const intFa = myNumber.toString().convertDigits("fa");
    const intAr = myNumber.toString().convertDigits("ar");
    const intUs = intFa.convertDigits("en");
     
  //   console.log(intFa); // ۹۸۷۶۵۴۳۲۱
  //   console.log(intAr); // ٩٨٧٦٥٤٣٢١
  //   console.log(intUs); // 987654321
    if(type == true){

        return intUs;
    }else{
      return intFa;
    }
}
  function change_number(btn,row_id){
      var row_value = btn.name
      var price_vahed = document.getElementById(`price_vahed_${row_id}`)
      var kol_price = document.getElementById(`all_price_${row_id}`)
      var kol_price_en = convert_to_en2(kol_price.innerText,type=true)
      var price_vahed_en = convert_to_en2(price_vahed.innerText,type=true)
      var order_id = $('#order_id').val();
      kol_price.innerText =convert_to_en2(number=price_vahed_en * Number($(btn).val()),type=false) 
      $.ajax({
          url:"/admindashboard/update_order_product/" + order_id,
          method :"GET",
          data : {
              "number":convert_to_en2(number=$(btn).val()),
              "product_id":row_id,
          },
          success: function(response){
              var all_price = response['all_price']
              var all_price1 = document.getElementById('all_price1')
              var all_price2 = document.getElementById('all_price2')
   

              var one = convert_to_en2(number= all_price,type=false)
              var tow = convert_to_en2(number= all_price,type=false)

              all_price1.innerText =one
              all_price2.innerText =tow
          }

      

      })

      
  }

