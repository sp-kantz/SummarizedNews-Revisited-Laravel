//used by start() on button click
var webServiceUrl_start = '../exec';

//on button click
//start the process
function start()
{
	//disable the button
	var button = document.getElementById("startButton");
	button.disabled = true;
    
	//send request to start the main process	
	try
	{			
		var asyncRequest = new XMLHttpRequest(); 
		asyncRequest.onreadystatechange = function() 
		{		
			if (asyncRequest.readyState == 4 && asyncRequest.status == 200) 
			{			
				button.disabled = false;
				location.reload(true);
			}
		};
		asyncRequest.open('GET', webServiceUrl_start, false);	
		asyncRequest.send(); 
	} 
	catch ( exception )
	{
		alert ( 'Request Failed' );
	} 	
}