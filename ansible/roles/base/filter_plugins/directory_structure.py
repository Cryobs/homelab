#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def dict_to_paths(structure, base_path='', current_path=''):
    """
    Nested dict to paths list
    
    Args:
        structure: dict
        base_path: str 
        current_path: str
    
    Returns:
        list - list dict with key 'path'
    
    Example:
        Input: {'data': {'forgejo': {}, 'photos': {'originals': {}}}}
        Output: [
            {'path': '/mnt/data'},
            {'path': '/mnt/data/forgejo'},
            {'path': '/mnt/data/photos'},
            {'path': '/mnt/data/photos/originals'}
        ]
    """
    paths = []
    
    if not isinstance(structure, dict):
        return paths
    
    for key, value in structure.items():
        # Build full path
        new_path = f"{base_path}/{current_path}/{key}".replace('//', '/').rstrip('/')
        
        # Add current path
        paths.append({'path': new_path})
        
        # Recursive processing of subdirs
        if isinstance(value, dict) and value:
            sub_current = f"{current_path}/{key}".strip('/')
            paths.extend(dict_to_paths(value, base_path, sub_current))
    
    return paths


class FilterModule(object):
    """Ansible filter plugin"""
    
    def filters(self):
        return {
            'dict_to_paths': dict_to_paths
        }

