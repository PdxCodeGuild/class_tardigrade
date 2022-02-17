</form>
	<div id="container">
		<div class="color" style="background-color: darksalmon;"></div>
		<!-- <div class="color" style="background-color: darksalmon;"></div>
		<div class="color" style="background-color: darkseagreen;"></div>
		<div class="color" style="background-color: paleturquoise;"></div>
		<div class="color" style="background-color: paleturquoise;"></div> -->
	</div>
	<script>
		const form = document.querySelector('form') // alternatively document.getElementByTagName('form')
@@ -42,14 +43,19 @@ <h1>Color Divs</h1>
			event.preventDefault() // stops the page from refreshing when the form is submitted
			// console.log(event)
			// console.log(input.value) // input.value is the text typed into the input element

			const color = input.value
			const colorDiv = document.createElement('div') // creates a new div
			colorDiv.classList.add('color') // gives that div class="color"
			colorDiv.style.backgroundColor = input.value //
			colorDiv.style.backgroundColor = color //
			container.appendChild(colorDiv) // makes colorDiv a child of container
			// console.log(colorDiv)
			// console.log(colorDiv.style)

			colorDiv.addEventListener('click', function() {
				document.body.style.backgroundColor = color
			})

			input.value = '' // set the input back to an empty string
			console.log(colorDiv.style)
		})
	</script>
</body>
