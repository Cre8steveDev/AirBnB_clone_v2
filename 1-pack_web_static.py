#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz 
archive from the contents of the web_static 
folder of your AirBnB Clone repo, using the 
function do_pack"""

from datetime import datetime
from fabric.api import local

def do_pack():
    """Make An Archive of the web_static folder on current directory"""
    
    curr_time = datetime.now()
    archive_name = "web_static_{}.tgz".format(curr_time.strftime("%Y%m%d%H%M%S"))
    create_archive = local('tar -cvzf versions/{} web_static'.format(archive_name))
    
    # Confirm if the created archive worked
    if create_archive:
        return create_archive
    else:
        return None
