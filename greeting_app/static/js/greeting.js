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