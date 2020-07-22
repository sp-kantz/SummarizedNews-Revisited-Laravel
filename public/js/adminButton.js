//used by start() on button click
var webServiceUrl_start = '../exec';

//on button click
//start the process
function start()
{
	//disable the button
	var button = document.getElementById("startButton");
	button.disabled = true;
	var status = document.getElementById("status");
		
	status.innerHTML="Process started";
    
	//send request to start the main process	
	try
	{			
		var asyncRequest = new XMLHttpRequest(); 
		asyncRequest.onreadystatechange = function() 
		{		
			result( asyncRequest );
		};
		asyncRequest.open('GET', webServiceUrl_start, true);	
		asyncRequest.send(); 
	} 
	catch ( exception )
	{
		alert ( 'Request Failed' );
	} 	
}

function result( asyncRequest )
{
	
	if ( asyncRequest.readyState == 4 )
	{
		var button = document.getElementById("startButton");
		button.disabled = false;

		var status = document.getElementById("status");
		
		status.innerHTML="Process Completed";
		
	} 
} 