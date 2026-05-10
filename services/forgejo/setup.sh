#!/usr/bin/env bash

set -e

mkdir -p /mnt/cryobs/forgejo/.cache

chown -R 1001:1001 /mnt/cryobs/forgejo
chmod 775 /mnt/cryobs/forgejo/.cache
chmod g+s /mnt/cryobs/forgejo/.cache
