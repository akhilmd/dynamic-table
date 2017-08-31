# Dynamic Table: Advanced Algorithms Assignment 1
## Prerequisites
* [gcc 5](https://gcc.gnu.org/gcc-5/)
* [python3](https://www.python.org/download/releases/3.0/)
  * [matplotlib](https://matplotlib.org/)
* [SWIG](http://www.swig.org/)
## Run Locally
#### Clone Repository
```
$ git clone https://github.com/akhilmd/dynamic-table
```
#### `make` project
```
$ cd dynamic-table
$ make
$ make tests
```
These commands will create a few output folders and place generated files there. A python module will be placed in `./tests/`

#### Example run of project
Graphs can be saved to disc via matplotlib GUI.
```
$ ./tests/test.py 1000000
Testing all inserts before deletes for factor: 1.25
Testing all inserts before deletes for factor: 1.5
Testing all inserts before deletes for factor: 1.75
Testing all inserts before deletes for factor: 2
Testing all inserts before deletes for factor: 3


Populating operations with ratio: 1.5
Operating with factors:  (1.25, 1.25)
Operating with factors:  (1.25, 1.5)
Operating with factors:  (1.25, 1.75)
Operating with factors:  (1.25, 2)
Operating with factors:  (1.25, 3)
Operating with factors:  (1.5, 1.25)
Operating with factors:  (1.5, 1.5)
Operating with factors:  (1.5, 1.75)
Operating with factors:  (1.5, 2)
Operating with factors:  (1.5, 3)
Operating with factors:  (1.75, 1.25)
Operating with factors:  (1.75, 1.5)
Operating with factors:  (1.75, 1.75)
Operating with factors:  (1.75, 2)
Operating with factors:  (1.75, 3)
Operating with factors:  (2, 1.25)
Operating with factors:  (2, 1.5)
Operating with factors:  (2, 1.75)
Operating with factors:  (2, 2)
Operating with factors:  (2, 3)
Operating with factors:  (3, 1.25)
Operating with factors:  (3, 1.5)
Operating with factors:  (3, 1.75)
Operating with factors:  (3, 2)
Operating with factors:  (3, 3)

All times in milliseconds
statistic: mxi 	ratio: 1.5
0.112621 | 0.103787 | 0.099036 | 0.104850 | 0.132426 | 
0.121415 | 0.100438 | 0.105272 | 0.089441 | 0.116070 | 
0.084652 | 0.092784 | 0.114639 | 0.080199 | 0.080274 | 
0.102437 | 0.098387 | 0.101826 | 0.085959 | 0.104094 | 
0.040205 | 0.037238 | 0.043973 | 0.043288 | 0.109718 | 

statistic: mxd 	ratio: 1.5
0.035260 | 0.003071 | 0.009122 | 0.002931 | 0.002398 | 
0.040356 | 0.025995 | 0.006794 | 0.005629 | 0.002908 | 
0.018456 | 0.016185 | 0.013467 | 0.010660 | 0.004426 | 
0.020108 | 0.015740 | 0.010809 | 0.013967 | 0.006454 | 
0.008720 | 0.023211 | 0.005949 | 0.005235 | 0.004891 | 

statistic: avgop 	ratio: 1.5
0.000068 | 0.000061 | 0.000061 | 0.000060 | 0.000060 | 
0.000073 | 0.000065 | 0.000061 | 0.000062 | 0.000062 | 
0.000075 | 0.000070 | 0.000065 | 0.000062 | 0.000059 | 
0.000073 | 0.000068 | 0.000068 | 0.000065 | 0.000061 | 
0.000074 | 0.000069 | 0.000070 | 0.000068 | 0.000062 | 

statistic: avgi 	ratio: 1.5
0.000072 | 0.000064 | 0.000064 | 0.000061 | 0.000061 | 
0.000076 | 0.000068 | 0.000063 | 0.000065 | 0.000065 | 
0.000078 | 0.000073 | 0.000068 | 0.000065 | 0.000062 | 
0.000073 | 0.000068 | 0.000069 | 0.000066 | 0.000063 | 
0.000075 | 0.000069 | 0.000072 | 0.000071 | 0.000065 | 

statistic: avgd 	ratio: 1.5
0.000061 | 0.000057 | 0.000057 | 0.000059 | 0.000058 | 
0.000069 | 0.000061 | 0.000057 | 0.000056 | 0.000057 | 
0.000069 | 0.000065 | 0.000060 | 0.000057 | 0.000055 | 
0.000072 | 0.000067 | 0.000066 | 0.000062 | 0.000058 | 
0.000073 | 0.000069 | 0.000066 | 0.000064 | 0.000058 | 



Populating operations with ratio: 2.0
Operating with factors:  (1.25, 1.25)
Operating with factors:  (1.25, 1.5)
Operating with factors:  (1.25, 1.75)
Operating with factors:  (1.25, 2)
Operating with factors:  (1.25, 3)
Operating with factors:  (1.5, 1.25)
Operating with factors:  (1.5, 1.5)
Operating with factors:  (1.5, 1.75)
Operating with factors:  (1.5, 2)
Operating with factors:  (1.5, 3)
Operating with factors:  (1.75, 1.25)
Operating with factors:  (1.75, 1.5)
Operating with factors:  (1.75, 1.75)
Operating with factors:  (1.75, 2)
Operating with factors:  (1.75, 3)
Operating with factors:  (2, 1.25)
Operating with factors:  (2, 1.5)
Operating with factors:  (2, 1.75)
Operating with factors:  (2, 2)
Operating with factors:  (2, 3)
Operating with factors:  (3, 1.25)
Operating with factors:  (3, 1.5)
Operating with factors:  (3, 1.75)
Operating with factors:  (3, 2)
Operating with factors:  (3, 3)

All times in milliseconds
statistic: mxi 	ratio: 2.0
0.199890 | 0.173425 | 0.213756 | 0.211200 | 0.196565 | 
0.181839 | 0.205222 | 0.151676 | 0.206153 | 0.141515 | 
0.213248 | 0.217295 | 0.206483 | 0.166713 | 0.126344 | 
0.188870 | 0.182537 | 0.178986 | 0.207980 | 0.179824 | 
0.115474 | 0.112529 | 0.115034 | 0.116615 | 0.119147 | 

statistic: mxd 	ratio: 2.0
0.021546 | 0.003012 | 0.004378 | 0.006148 | 0.004855 | 
0.018449 | 0.013864 | 0.006564 | 0.005503 | 0.002364 | 
0.027262 | 0.005666 | 0.007167 | 0.006656 | 0.004452 | 
0.008096 | 0.006115 | 0.007332 | 0.008200 | 0.017657 | 
0.007887 | 0.006497 | 0.005960 | 0.005525 | 0.006992 | 

statistic: avgop 	ratio: 2.0
0.000064 | 0.000062 | 0.000061 | 0.000060 | 0.000060 | 
0.000066 | 0.000062 | 0.000061 | 0.000058 | 0.000057 | 
0.000066 | 0.000064 | 0.000062 | 0.000058 | 0.000058 | 
0.000063 | 0.000061 | 0.000064 | 0.000061 | 0.000060 | 
0.000062 | 0.000062 | 0.000061 | 0.000063 | 0.000061 | 

statistic: avgi 	ratio: 2.0
0.000069 | 0.000064 | 0.000065 | 0.000059 | 0.000060 | 
0.000069 | 0.000065 | 0.000063 | 0.000057 | 0.000056 | 
0.000070 | 0.000067 | 0.000064 | 0.000056 | 0.000057 | 
0.000062 | 0.000061 | 0.000066 | 0.000063 | 0.000062 | 
0.000062 | 0.000062 | 0.000062 | 0.000065 | 0.000063 | 

statistic: avgd 	ratio: 2.0
0.000053 | 0.000058 | 0.000054 | 0.000061 | 0.000060 | 
0.000060 | 0.000058 | 0.000058 | 0.000061 | 0.000060 | 
0.000057 | 0.000058 | 0.000057 | 0.000060 | 0.000061 | 
0.000065 | 0.000060 | 0.000059 | 0.000057 | 0.000055 | 
0.000063 | 0.000062 | 0.000059 | 0.000059 | 0.000056 |  
```
Grahs generated:
![insertions](https://github.com/akhilmd/dynamic-table/raw/master/img/ins.png)
This graph shows the cumulative and no. of insertions. It can be noted that the vertical parts of the lines show the time taken to allocate and copy items.
![deletions](https://github.com/akhilmd/dynamic-table/raw/master/img/del.png)
This graph shows the same for deletions.

Use `$ make clean` to remove generated files.
