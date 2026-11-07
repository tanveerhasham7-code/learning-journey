# 02 — Terminal Navigation and File Operations

## Command structure
A command commonly follows this pattern: command, options, then arguments.

Example: `ls -lah /var/log`
- ls is the command.
- -l, -a and -h are options.
- /var/log is the target path.

Linux is case-sensitive: File.txt and file.txt are different names.

## Navigation
```bash
pwd
ls
ls -lah
cd /var/log
cd ..
cd ~
cd -
```
pwd prints the current directory. cd changes directory. An absolute path starts at /; a relative path starts from the current directory.

## Create, copy, move and remove
```bash
mkdir practice
mkdir -p projects/linux/labs
touch notes.txt
cp notes.txt notes-backup.txt
mv notes-backup.txt archive.txt
rmdir empty-folder
rm archive.txt
```
Be careful with rm: it may permanently remove files. Before using recursive or force options, verify your current directory and target path.

## Read and search files
```bash
cat notes.txt
less /var/log/syslog
head -n 20 notes.txt
tail -n 20 notes.txt
tail -f /var/log/auth.log
grep "failed" sample.log
grep -in "error" sample.log
find ~/ -type f -name "*.txt"
```
less is useful for large files; press q to quit. tail -f follows new lines. grep searches text. find searches directory trees.

## Input, output and pipes
- stdin: standard input.
- stdout: normal command output.
- stderr: error output.

```bash
echo "Linux practice" > practice.txt
date >> practice.txt
cat practice.txt | grep Linux
ls /etc > etc-list.txt
command 2> errors.txt
```
> replaces a file; >> appends. Check the destination before redirecting.

## Help
```bash
man ls
ls --help
whatis chmod
apropos network
```

## Quoting and wildcards
- *.log matches names ending in .log.
- file?.txt matches one character in place of ?.
- Single quotes preserve literal characters.
- Double quotes allow variable expansion.

```bash
name="student"
echo "Hello $name"
echo 'Hello $name'
```

## Practical exercise
Create a directory named linux-lab. Add three text files, write sample lines, search for a word with grep, copy one file, move another, and list the final directory. Record each command and explain what it did.

## Security connection
Command-line skills are used by both administrators and attackers. File ownership, timestamps and logs can help explain system changes. Shell history alone is not a complete or tamper-proof audit log.
