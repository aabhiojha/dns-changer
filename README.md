                         ## About The Project

![Screenshot](https://github.com/aabhiojha/dns-changer/blob/main/Screenshot%20from%202024-06-12%2007-58-57.png)
 ### Built With

- [Python3](https://docs.python.org/3/)
 ## Getting Started

This script was tested on kali linux 2024.2 but it should work on majority of debian based distributions. 
 ### Prerequisites

Most of the debian based systems come with python preinstalled. So you can skip this section.
In case it is not present, Install it with: 
  ```sh
  sudo apt install python3 
  ```
 ## Usage

one line command:
  ```sh 
sudo python3 dns-change.py
  ```

This will backup your ```/etc/resolv.conf``` file and replace it with updated dns file.
