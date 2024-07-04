# password_manager
*A Fernet password manager*

Sometimes you don't want to pay for a password manager on the internet with a company that doesn't take it's security so seriously.
Ok let's be honest, this program is not fool proof and it's just used to learn about security, so don't use it for real!

How does it work?

A hashed key is generated as a seperate file which will be saved as "secret.key".
This key is used to encrypt the password that is being asked for.
To save the encrypted password it is saved in the file passwords.json.

The main loop asks you 3 options:

- add
- retrieve
- exit

To Do:
* More functionality
* Better security
