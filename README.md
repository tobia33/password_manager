# password manager

Password manager is a program that (can you guess?) manages passwords.
You can add passwords, delete passwords, see passwords... well that's about it,
so what makes this program worth your time?

For starters it's real simple to use and it's real simple to get information if you are lost!

But most importantly it's safe. 
every time you add a password you choose a decryption key which is used to encrypt your password,
the password will then encrypted using that key and will be stored in it's encrypted state!
it means no one can figure out your password without the decryption key.
So you are ok, as long as you do remember your decryption key,
if you don't the password can no longer be decrypted and can never be recovered.

The encryption is made using the Fernet encryption from the python cryptography library

Password manager is a python program, to use it you should download the password_manager_py directory and execute password_manager.py

Another version is currently being worked on, a phone application, using html, css, javascript and php.

