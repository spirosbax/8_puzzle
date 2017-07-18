# 8 Puzzle Game with AI solver

### Implementation
I implemented: 
* Breadth First Search
* Depth First Search 
* A* search algorithm 

The solver uses A* search to find the shortest path to the goal in minimum time.
To assign a heuristic value to a Node I used the Manhattan distance of that Node from the goal plus the path cost from the starting state to that Node.

### Installation
The program requires python 3.5 and is currenctly compatible with Unix systems.
For simplicity the installation and download instructions will use the Debian (and derivatives like Ubuntu) package manager "aptitute" (apt-get) but feel free to replace it with your distribution's package manager.
The following lines should install python3.5 on your computer, but results may vary depending on your distribution, do some research before executing.
```sh
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python3.5
```

Next we will install the python3 package manager "pip3" and then the modules needed for the program to work
```sh
sudo apt-get install python3-pip
sudo pip3 install asciimatics pyfiglet resource 
```
### Downloading
There 2 ways to download the repository (at least as far as I know).
#### Using the git module (Recommended)
If you are unsure if you have the git module you can install it with
```sh
sudo apt-get install git
```
In order to download the repository you need to
```sh
git clone [link to this repository]
```
this will create a directory called "8_puzzle" containing the repository files, then do 
```sh
cd 8_puzzle
```
To change directory.
Then run the file "driver_3.py" with
```sh
python3 driver_3.py
```
#### Downloading the .zip file
Go to the top right of the repository and click the download.zip button, then extract the containing folder and "cd" into it,
lastly run the file with 
```sh
python3 driver_3.py
```

### Development
I am open to suggestions for improving the A* algorithm, feel free to contribute.
Want to contribute? Great! 
Fork the repository and start coding


### Todo

 - Add windows compatibility
