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
$ ./tests/test.py 100000
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
0.008881 | 0.007052 | 0.007845 | 0.005838 | 0.008750 | 
0.009254 | 0.011372 | 0.008327 | 0.007960 | 0.011625 | 
0.008943 | 0.007338 | 0.016144 | 0.007940 | 0.008223 | 
0.008182 | 0.009535 | 0.008685 | 0.010207 | 0.008512 | 
0.011128 | 0.003540 | 0.004096 | 0.003738 | 0.057659 | 

statistic: mxd 	ratio: 1.5
0.019212 | 0.001732 | 0.002141 | 0.002466 | 0.001399 | 
0.019309 | 0.014702 | 0.002359 | 0.001981 | 0.002841 | 
0.009553 | 0.003182 | 0.004127 | 0.003086 | 0.001437 | 
0.003744 | 0.002743 | 0.001886 | 0.002570 | 0.002096 | 
0.001637 | 0.001949 | 0.011167 | 0.002622 | 0.004762 | 

statistic: avgop 	ratio: 1.5
0.000069 | 0.000063 | 0.000063 | 0.000061 | 0.000062 | 
0.000073 | 0.000063 | 0.000063 | 0.000062 | 0.000064 | 
0.000073 | 0.000067 | 0.000066 | 0.000064 | 0.000064 | 
0.000075 | 0.000071 | 0.000068 | 0.000064 | 0.000060 | 
0.000075 | 0.000070 | 0.000069 | 0.000067 | 0.000063 | 

statistic: avgi 	ratio: 1.5
0.000070 | 0.000063 | 0.000064 | 0.000060 | 0.000064 | 
0.000072 | 0.000060 | 0.000062 | 0.000062 | 0.000065 | 
0.000073 | 0.000067 | 0.000067 | 0.000065 | 0.000065 | 
0.000075 | 0.000071 | 0.000069 | 0.000063 | 0.000059 | 
0.000076 | 0.000071 | 0.000069 | 0.000068 | 0.000063 | 

statistic: avgd 	ratio: 1.5
0.000068 | 0.000062 | 0.000062 | 0.000061 | 0.000061 | 
0.000074 | 0.000067 | 0.000064 | 0.000063 | 0.000063 | 
0.000074 | 0.000068 | 0.000065 | 0.000062 | 0.000062 | 
0.000073 | 0.000072 | 0.000068 | 0.000066 | 0.000063 | 
0.000074 | 0.000068 | 0.000069 | 0.000067 | 0.000065 | 



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
0.046845 | 0.018271 | 0.017346 | 0.022684 | 0.024974 | 
0.014261 | 0.022810 | 0.022804 | 0.013854 | 0.015068 | 
0.017760 | 0.018115 | 0.014365 | 0.020468 | 0.010507 | 
0.022401 | 0.016124 | 0.023839 | 0.028685 | 0.020097 | 
0.010326 | 0.018289 | 0.043474 | 0.009903 | 0.012618 | 

statistic: mxd 	ratio: 2.0
0.024143 | 0.002405 | 0.002462 | 0.000922 | 0.001045 | 
0.023762 | 0.020864 | 0.005447 | 0.015092 | 0.001644 | 
0.040092 | 0.012624 | 0.007619 | 0.006110 | 0.002638 | 
0.010884 | 0.022703 | 0.006163 | 0.013749 | 0.001212 | 
0.013178 | 0.012475 | 0.006600 | 0.008154 | 0.003988 | 

statistic: avgop 	ratio: 2.0
0.000067 | 0.000065 | 0.000064 | 0.000065 | 0.000064 | 
0.000074 | 0.000067 | 0.000064 | 0.000064 | 0.000063 | 
0.000073 | 0.000070 | 0.000066 | 0.000064 | 0.000062 | 
0.000075 | 0.000070 | 0.000068 | 0.000065 | 0.000062 | 
0.000076 | 0.000071 | 0.000070 | 0.000066 | 0.000064 | 

statistic: avgi 	ratio: 2.0
0.000068 | 0.000066 | 0.000063 | 0.000066 | 0.000065 | 
0.000075 | 0.000067 | 0.000064 | 0.000064 | 0.000063 | 
0.000072 | 0.000069 | 0.000066 | 0.000064 | 0.000061 | 
0.000075 | 0.000070 | 0.000068 | 0.000066 | 0.000061 | 
0.000077 | 0.000071 | 0.000070 | 0.000065 | 0.000062 | 

statistic: avgd 	ratio: 2.0
0.000065 | 0.000062 | 0.000065 | 0.000063 | 0.000062 | 
0.000074 | 0.000069 | 0.000064 | 0.000063 | 0.000062 | 
0.000075 | 0.000072 | 0.000066 | 0.000064 | 0.000064 | 
0.000074 | 0.000070 | 0.000069 | 0.000065 | 0.000064 | 
0.000074 | 0.000071 | 0.000069 | 0.000069 | 0.000067 | 
```
Use `$ make clean` to remove generated files.
