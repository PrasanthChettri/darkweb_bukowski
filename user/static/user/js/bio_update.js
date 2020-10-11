function update(bio , profile_url){
	console.log(profile_url) ;
	 document.getElementById("bio").innerHTML =  ` <form action = ` +  profile_url  +` method = 'GET'>
	            <label for="new_bio">Write : </label><br>
				<textarea id="new_bio" name="new_bio" rows="4" cols="50">`
				+ bio + 
				`</textarea>
				    <button class="btn btn-outline-light" type="submit" value="Submit">Submit</button>
				</form>
			` ;
}