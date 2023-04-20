#!/usr/bin/python3
"""This module instantiates an object of class FileStorage.

If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
Otherwise, instantiates a file storage engine (FileStorage).
"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage_t == os.getenv('HBNB_TYPE_STORAGE')

if storage_t == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
