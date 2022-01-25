let responses = [
	"I don't know",
	"What? I wasn't listening.  Could you please ask again?",
	'I know it to be true',
	'Doubtful',
	'sure, i guess',
]

alert(responses.length) // python equivalent -> len(responses)

alert('welcome to the amazing 8 ball')

prompt('what is it you wish to know?  ')

alert('Looking into it...')

let response = responses[Math.floor(Math.random() * responses.length)]

// Math.random() returns a random float between 0 and 1
// responses.length is the length of the array (5)
// Math.random() * responses.length is a random float between 0 and 5
// Math.floor(Math.random() * responses.length)) is a random integer from 0 to 4
// responses[Math.floor(Math.random() * responses.length)] is a random element in the array

alert(response)