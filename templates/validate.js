user = null;
function Getallrooms(){
    var http = new XMLHttpRequest()
    http.open("http://127.0.0.1:5000/api/rooms", true)
    http.onreadystatechange = function(){
        if(this.status === 200){
            rooms = JSON.parse(this.responseText);
            Getallrooms()

        }
        
    }   
    http.send();
}

function Setuprooms()

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
    var http = new XMLHttpRequest()
    http.open("http://localhost:5000/baset/api/user?name="+username, true)
    http.onreadystatechange = function(){
        if(this.status === 200){
            user = JSON.parse(this.responseText);
            Getallrooms()

        }
        
    }   
    http.send();


    
}