# Critical path metod

## Useage
    usage: main.py [-h] [-f FILE] [-n [NODES [NODES ...]]]
               [-e [EDGES [EDGES ...]]] [--example]

    optional arguments:
    -h, --help            show this help message and exit
    -f FILE, --file FILE  load data from file
    -n [NODES [NODES ...]], --nodes [NODES [NODES ...]]
                            load nodes with processing time
    -e [EDGES [EDGES ...]], --edges [EDGES [EDGES ...]]
                            load edges between nodes
    --example             show example

## Virtualenv

It's recommend to run this program in virtualenv - you don't need install dependencies system wide

### To create virtualenv:
    virtualenv .
    source bin/activate 
    pip install -r requirements.txt 

### Run program
    python main.py --nodes 1 3 2 2 3 2 4 1 5 4 6 1 7 2 --edges 1 3 3 5 5 7 2 4 4 5 4 6 6 7 --file test
    