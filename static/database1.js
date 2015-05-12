var socket;

$(document).ready(function(){
    socket= io.connect('http://localhost:5000/');

    
    $('#signup').click(function(e){
	var name= $('#userInput').val();
	var pw = $('#passwordInput').val();
	console.log(name+" "+pw);
	socket.emit('login',{user:name,password:pw});
	
	
    }
		      )});
		     
		      

   
        
