# 4chan media downloader

## Usage
### command line arguments

`$ ./autorun.sh -f {folder_path} -b {board_id} -t {threads}`

1. Add the `-f` or `--file` argument to define the path where the media will be stored.

2. Add the `-b` or `--board` argument to provide the board.

3. Add the `-t` or `--threads` argument to provide the threads ids.

## Example
```#!/bin/sh
    $ ./autorun.sh -f /dev/null -b b -t '111111 222222 333333'
```