import os, sys
from os import system as sm
from sys import platform as pf
import time
from time import sleep as sp
import random
import re
import httpx
import asyncio
import json
#sm('apt install espeak -y')
try:
    import requests, bs4, concurrent.futures, uuid, string, rich
    from rich import print as rprint
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as bsoup
    from uuid import uuid4 as uid4
except ModuleNotFoundError:
    print("Installing Missing Modules")
    sm("pip install requests bs4 futures")        
