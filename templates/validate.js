function validate()
{
    var username=document.getElementById("username").value;
    if(username=="admin"){
        alert("login succes");
        return false;

    }
    else
    {
        alert("login failed")
    }
    
}