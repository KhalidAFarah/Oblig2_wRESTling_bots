user = null;

function Getallrooms(){
    var http = new XMLHttpRequest()
    http.open("http://127.0.0.1:5000/api/rooms", true)
    http.onreadystatechange = function(){
        if(this.status === 200){
            rooms = JSON.parse(this.responseText);
            var rs = document.getElementsByClassName("rooms")
            for(var i = 0; i < rooms.length; i++){
                var btn = "<button class=\"btnrooms\" onclick=\"button_atrooms\">Join room</button>"
                var room_name = "<h1>Room  "+rooms[i].room_id+"</h1>"
                rs[0].innerHTML +=  "<div class=\"room\">"+ room_name + btn+"</div>" 
                function button_atrooms(){
                console.log("hei")
                
               }
 
            }
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
function validateUsername(str) {
    var error = "";
    var illegalChars = /\W/; // allow letters, numbers, and underscores

    if (str == "") {
        error = "&bull; Please enter Username<br>";
    } else if ((str.length < 5) || (str.length > 15)) {
        error = "&bull; Username must have 5-15 characters<br>";
    } else if (illegalChars.test(str)) {
  	error = "&bull; Please enter valid Username. Use only numbers and alphabets<br>";
    } else {
        var http = new XMLHttpRequest()
        console.log("1")
        http.open("http://localhost:5000/api/user?name="+username, true)
        http.onreadystatechange = function(){
            if(this.status === 200){
                user = JSON.parse(this.responseText);
                console.log(user)
                Getallrooms()

            }
            
        }   
        http.send();
        error = "";
    }
    return error;
}
}
    
