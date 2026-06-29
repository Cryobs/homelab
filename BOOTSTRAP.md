### Finding Your Disk/Partition Identifiers

**Method 1: Partition ID (Recommended)**
```bash
ls -l /dev/disk/by-id/ | grep part
```

Example output:
```
lrwxrwxrwx 1 root root 10 May 11 12:00 ata-WDC_WD10EZEX-part1 -> ../../sda1
lrwxrwxrwx 1 root root 10 May 11 12:00 ata-WDC_WD10EZEX-part2 -> ../../sda2
lrwxrwxrwx 1 root root 10 May 11 12:00 usb-Samsung_SSD_T5-part1 -> ../../sdb1
```

**Method 2: UUID**
```bash
sudo blkid
```

Example output:
```
/dev/sda1: UUID="12345678-abcd-1234-abcd-123456789abc" TYPE="ext4"
/dev/sda2: UUID="87654321-dcba-4321-dcba-cba987654321" TYPE="ext4"
```

**Method 3: Detailed Info**
```bash
lsblk -o NAME,SIZE,FSTYPE,LABEL,UUID,MODEL
```

### Configuration Examples

#### Single disk with one partition:
```yaml
external_disks:
  - name: cryobs_main
    partition_id: "ata-WDC_WD10EZEX-part1"
    mount_point: /mnt/cryobs
    directory_structure:
      services: {}
      data: {}
      backups: {}
```

#### Multiple partitions on same disk:
```yaml
external_disks:
  - name: data_partition
    partition_id: "ata-SAMSUNG_SSD_870-part1"
    mount_point: /mnt/data
    directory_structure:
      services: {}
      data: {}
  
  - name: backup_partition
    partition_id: "ata-SAMSUNG_SSD_870-part2"
    mount_point: /mnt/backups
    mount_options: defaults,nofail,noauto  # Don't mount at boot
    directory_structure:
      daily: {}
      weekly: {}
```

#### Using UUID instead:
```yaml
external_disks:
  - name: cryobs_main
    uuid: "12345678-abcd-1234-abcd-123456789abc"
    mount_point: /mnt/cryobs
    directory_structure:
      services: {}
```

#### USB drive (auto-detect filesystem):
```yaml
external_disks:
  - name: usb_storage
    partition_id: "usb-Samsung_Portable_SSD_T5-part1"
    mount_point: /mnt/usb
    fstype: auto
    directory_structure:
      media: {}
```

### Why Partition ID is Recommended

1. **Readable** - Includes disk model and partition number
2. **Stable** - Doesn't change when disk order changes
3. **Specific** - Points to exact partition, not just disk
4. **Works with multiple partitions** - Each partition has unique ID

### Troubleshooting

**Partition not found:**
```bash
# List all available IDs
ls -l /dev/disk/by-id/

# Check if partition is visible
sudo fdisk -l

# Verify partition exists
lsblk
```

**Mount fails:**
```bash
# Check filesystem
sudo blkid /dev/sdXN

# Try manual mount
sudo mount /dev/sdXN /mnt/test

# Check dmesg for errors
sudo dmesg | tail
```
