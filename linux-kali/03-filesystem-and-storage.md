# 03 — Linux Filesystem Hierarchy and Storage

## Root directory
Linux uses one directory tree beginning at / (root). Other filesystems can be attached to directories called mount points.

| Directory | Purpose |
|---|---|
| / | Top of the filesystem tree |
| /home | Regular users' home directories |
| /root | Root user's home directory |
| /etc | System-wide configuration |
| /var | Variable data such as logs and caches |
| /var/log | System and service logs |
| /tmp | Temporary files |
| /usr | Programs, libraries and shared data |
| /bin and /sbin | Essential commands; often links into /usr |
| /opt | Optional third-party software |
| /dev | Device files |
| /proc | Virtual process and kernel information |
| /sys | Kernel and device information |
| /boot | Boot-related files |
| /mnt and /media | Common mount locations |

## File types
Linux supports regular files, directories, symbolic links, character devices, block devices, FIFOs and Unix domain sockets.

Use:
```bash
ls -l
file filename
stat filename
readlink -f /path/to/item
```

## Storage inspection
```bash
lsblk -f
df -h
du -sh ~/Downloads
mount
findmnt
blkid
```
- lsblk displays block devices and partitions.
- df displays filesystem space usage.
- du displays directory/file usage.
- findmnt shows mounted filesystems.

## Key concepts
- Partition: logical division of a storage device.
- Filesystem: structure used to store and retrieve files (e.g. ext4, XFS, Btrfs).
- Mount: attach a filesystem to the directory tree.
- Swap: disk space used as a memory-management supplement.
- Inode: metadata structure tracking file information and data-block references.

## Safe lab
1. Run lsblk -f and identify the VM disk.
2. Run df -h and note free space.
3. Create a folder and sample file in your home directory.
4. Run du -sh on the folder.
5. Inspect metadata with stat.
6. Explain why a full disk can affect logs and security monitoring.

Do not partition or format a real disk for this beginner lab. Formatting destroys data. Use a disposable virtual disk and a snapshot when learning partitioning later.
