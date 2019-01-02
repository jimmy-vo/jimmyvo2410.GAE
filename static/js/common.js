
// Other event listeners can go here.
document.addEventListener("DOMContentLoaded", function(){  	
	$('#layout_top').load('header.html', function(responseTxt, statusTxt, xhr){
		if(statusTxt == "success"){
			$('#headerTemplate').html($('#headerContent').html());
			if ($('#headerNum').html() !== '-1')
			{
				$('#navigation li:eq(' + $('#headerNum').html() + ')').addClass("selected");
			}
		}
		if(statusTxt == "error")
		  	alert("Failed to load header: " + xhr.status + ": " + xhr.statusText);
	});
	$('#footer').load('footer.html');
});
