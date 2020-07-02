# Tkinter-CryptothonApp
Cryptothon is an Encryption and Decryption app made with Python and Tkinter.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [py to exe](#py-to-exe)
* [License](#license)

## General info
This project is a simple Crytptograpy app made with Python and Tkinter and some modules which are mentioned below. The Encrypted message and key is generated after encryption. During Decryption, the encrypted message and encrypted key filenames are entered to display the original message.

![Cryptothon](https://user-images.githubusercontent.com/67178624/86348444-4dc65980-bc7d-11ea-99a3-f8712c81ae2f.png)
	
## Technologies
Project is created with:
* Python version: 3.8.3
* Tkinter version: 8.5
* Cryptography Api version: 2.9.2
	
## Setup
### To run this project,
#### Install Tkinter
```
pip install tkinter
```
#### Install Cryptography Api
```
pip install cryptography
```
#### Run using cmd
```
python Cryptothon.py
```

## .py to .exe
### Convert .py file to .exe file
#### Install the pyinstaller module
* ```pip install pyinstaller```
#### Instructions
* Open your cmd and change your directory to the .py file.
* Choose an Icon. Icon must be in .ico format.
* Type ```pyinstaller -w -F -i (Your icon directory with file name) (filename.py)``` and hit enter.
* Open the directory and go to Dist folder where you can find the App.

## License
* MIT licensed. See the [License](LICENSE) file for full details. 

