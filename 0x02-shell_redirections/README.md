# 0x02. Shell, I/O Redirections and Filters

## Description

This project is part of the ALX Software Engineering curriculum. It focuses on learning how to manipulate text files and streams using the command line in a Unix environment. The tasks in this project explore essential shell commands, input/output redirections, and the use of filters to process data.

## Learning Objectives

By completing the tasks in this project, I was able to understand and apply the following concepts:

- Shell I/O redirections:
  - Redirecting standard output to a file
  - Redirecting standard input from a file
  - Sending the output of one command as input to another
  - Combining commands with pipes and filters
- Shell special characters:
  - Whitespace, single/double quotes, backslash, comments, pipes, tilde
- Common command-line tools and filters:
  - `cat`, `head`, `tail`, `wc`, `sort`, `uniq`, `grep`, `tr`, `cut`, `rev`, `find`, `echo`
- Understanding the format and content of `/etc/passwd` and `/etc/shadow` files

## Requirements

- All scripts are written in Bash and are exactly two lines long.
- All scripts start with `#!/bin/bash` and end with a new line.
- No usage of `sed`, `awk`, backticks, `&&`, `||`, or `;`.
- Scripts are written and tested on Ubuntu 20.04 LTS.
- All files are executable.

## Files

Each script performs a specific task as outlined in the project requirements. Below is a list of the scripts and a brief description of what each does:

| File | Description |
|------|-------------|
| `0-hello_world` | Prints “Hello, World”, followed by a new line to the standard output |
| `1-confused_smiley` | Displays a confused smiley `"(Ôo)'` |
| `2-hellofile` | Displays the content of the `/etc/passwd` file |
| `3-twofiles` | Displays the contents of `/etc/passwd` and `/etc/hosts` |
| `4-lastlines` | Displays the last 10 lines of `/etc/passwd` |
| `5-firstlines` | Displays the first 10 lines of `/etc/passwd` |
| `6-third_line` | Displays the third line of the file `iacta` |
| `7-file` | Creates a file named exactly `\*\'"Best School"\'\*$\?\*\*\*\*\*:)` |
| `8-cwd_state` | Writes the result of the command `ls -la` into the file `ls_cwd_content` |
| `9-duplicate_last_line` | Duplicates the last line of the file `iacta` |
| `10-no_more_js` | Deletes all regular files with a `.js` extension in the current directory |
| `11-directories` | Counts the number of directories and sub-directories in the current directory |
| `12-newest_files` | Displays the 10 newest files in the current directory |
| `13-unique` | Takes a list of words and displays only those that appear once |
| `14-findthatword` | Displays lines containing the pattern “root” from the file `/etc/passwd` |
| `15-countthatword` | Displays the number of lines that contain the pattern “bin” in `/etc/passwd` |
| `16-whatsnext` | Displays lines containing “root” and 3 lines after them from `/etc/passwd` |
| `17-hidethisword` | Displays all lines in `/etc/passwd` that do not contain the pattern “bin” |
| `18-letteronly` | Displays all lines of a file starting with a letter |
| `19-AZ` | Replaces all characters `A` and `c` from input to `Z` and `e` respectively |
| `20-hiago` | Removes all letters `c` and `C` from input |
| `21-reverse` | Reverses input |
| `22-users_and_homes` | Displays all users and their home directories, sorted by users |

> 📁 Note: The `iacta` file used in some tasks should be created and filled with content beforehand for accurate testing.

## Author

Trevor Ndegwa  
[GitHub: @trevorndegwa](https://github.com/trevorndegwa)

---
