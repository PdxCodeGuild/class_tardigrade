var message, message2, rot13, user_input, user_input2
const alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'

let encryptionButton = document.getElementById("rot13")
let user_encrypt = document.querySelector("#encrypt")
let encrypt_output = document.getElementById("output")

let decryptionButton = document.getElementById("decryption")
let user_decrypt = document.querySelector("#decrypt")
let decrypt_output = document.getElementById("output2")

encryptionButton.onclick = function () {
  message = user_encrypt.value
  function rot13(message) {
    return message.replace(/[a-z]/gi, letter => alpha[alpha.indexOf(letter) + 13]);
  }
  encrypt_output.innerText = `"${message}" encrypted is "${rot13(message)}"`
}

decryptionButton.onclick = function () {
  message2 = user_decrypt.value
  function reverse13(message2) {
    return message2.replace(/[a-z]/gi, letter1 => alpha[alpha.indexOf(letter1) + 13]);
  }
  decrypt_output.innerText = `"${message2}" decrypted is "${reverse13(message2)}"`
}