$(()=>{
  $(".currency").each(function(){
    x = $(this).text()
    console.log($(this).text());
    $(this).html("$"+x)
  });

})
