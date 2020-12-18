function validateform(){  
  var name=document.form.name.value;  
  var msg=document.form.msg.value;  
    
  if (name==null || name==""){  
    alert("Name can't be blank!");  
    return false;  
  }else if(msg==null|| msg==""){  
    alert("Messgage can't be blank!");  
    return false;  
    }  
  }

  $(document).ready(function() {
    $(".btn-outline-danger").click(function() {
      var id = $(this).attr("id");
      var check = confirm("Are you sure you want to delete ?" );
      if(check==true){
        window.location.href = id;
      }else{
        return false;
      }
    });
  });
  
 