# MacBook Pro / Air Keyboard Test Utility
This is a small utility to test the keyboard of a MacBook Pro or MacBook Air.
It provides keyboard layout GUI that looks like the actual MacBook keyboard.

## How to create standalone app for Macs 

Make sure you have pyistaller installed on your Mac.

Download the code from this repository.

On your Mac, open teminal and cd to the downloaded folder.

Now type the following line for each of the py files in this folder to create standalone app for your Mac.


## For MacBook Keyboard.
pyinstaller --onefile --windowed --name "MacBook Keyboard Tester" Mac_KB_Test.py

## For Full Mac Keyboard.
pyinstaller --onefile --windowed --name "Full Keyboard Tester" full_kb_mac.py




### Keyboard image on initialization
![MacBook Keyboard](https://github.com/fnmalik2002/MacBook-Pro-Air-Keyboard-Test/blob/main/Resources/image1.png)


### Keyboard image after successful test

As a key is pressed, the color of the key changes
![MacBook Keyboard](https://github.com/fnmalik2002/MacBook-Pro-Air-Keyboard-Test/blob/main/Resources/image2.png)

### Full Keyboard image on initialization
![MacBook Keyboard](https://github.com/fnmalik2002/MacBook-Pro-Air-Keyboard-Test/blob/main/Resources/image3.png)


### Full Keyboard image after successful test

As a key is pressed, the color of the key changes
![MacBook Keyboard](https://github.com/fnmalik2002/MacBook-Pro-Air-Keyboard-Test/blob/main/Resources/image4.png)


