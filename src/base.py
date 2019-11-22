#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import make_url
import logging

bd = os.environ['BD']
engine = create_engine(make_url(bd))
Session = sessionmaker(bind=engine)

Base = declarative_base()

# Parte de logs
logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(message)s')
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
