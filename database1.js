var socket;

$(document).ready(function(){
    socket= io.connect('http://'+ document.domain+":"+location.port);

    
    $('#signup').click(function(e){
	var name= $('#emailInput').val();
	var pw = $('#passwordInput').val();
	socket.on('connect',function(){
	    socket.send('login',{email:name,password:pw});
	    console.log(name+' '+pw);
	})
    }
		      }
};
		     
		      

   
        
