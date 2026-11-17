# Lab 2 — Files and Directories

**Status:** Completed  
**Environment:** Kali Linux VM running in VMware Workstation  
**Date:** 17 November 2026

## Objective

Practice creating files and directories, writing and reading file content, copying, renaming, moving and deleting files, searching for files, and checking directory size.

## Commands performed

| Step | Command(s) | Purpose |
|---|---|---|
| Create the practice directory | `mkdir -p ~/lab2-practice` and `cd ~/lab2-practice` | Create and enter a dedicated practice area |
| Create three files | `touch file1.txt file2.txt file3.txt` and `ls -l` | Create empty files and list them |
| Write and read content | `echo "This is my first Linux practical lab." > file1.txt` and `cat file1.txt` | Write text to a file and display it |
| Copy a file | `cp file1.txt file1-copy.txt` | Create a copy of the original file |
| Rename a file | `mv file2.txt renamed-file.txt` | Rename a file |
| Create a subdirectory | `mkdir documents` | Create a directory inside the practice folder |
| Move a file | `mv file3.txt documents/` | Move a file into the subdirectory |
| Delete the copy | `rm file1-copy.txt` | Remove the copied file while keeping the original |
| Read with a pager | `less file1.txt`, then press `q` | View file content with the `less` pager |
| Search for text files | `find . -name "*.txt"` | Locate all matching text files under the current directory |
| Inspect final structure and size | `pwd`, `ls -R`, `du -sh .` | Show current path, recursive listing and total directory size |

## Expected final structure

Based on the operations performed, the practice directory should contain:

```text
lab2-practice/
├── file1.txt
├── renamed-file.txt
└── documents/
    └── file3.txt
```

The copied file `file1-copy.txt` was deleted. The original `file1.txt` was retained.

## Key concepts learned

1. `mkdir` creates directories; `mkdir -p` can create missing parent directories.
2. `touch` creates empty files or updates timestamps.
3. `>` redirects output into a file, replacing existing content.
4. `cat` displays file content.
5. `cp` copies files; `mv` renames or moves them.
6. `rm` deletes files, so its path should be checked before execution.
7. `less` provides page-by-page file viewing; press `q` to exit.
8. `find` searches directory trees using conditions such as a filename pattern.
9. `ls -R` lists directory contents recursively, while `du -sh .` reports the directory's total disk usage in a readable format.

## Evidence and limitations

The learner confirmed completing each command and the final verification commands during the guided practical. No screenshots were supplied for this lab, so this report records the commands and expected resulting structure rather than claiming screenshot evidence or independently verified terminal output.

## Security lesson

Practice file operations inside a dedicated working directory. Be especially careful with deletion commands and redirection because they can permanently remove or overwrite data. Avoid placing passwords, private keys or sensitive information in practice files.

## Completion

Lab 2 steps were completed by the learner and documented. No system configuration or security settings were changed.
