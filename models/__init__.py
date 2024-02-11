#!/usr/bin/python3
"""Entry Point for Command Interpreter"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
