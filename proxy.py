#! python3

import os, random

def get_random_proxy (): 
    """
    Return a random proxy from list
    """

    current_dir = os.path.dirname (__file__)
    proxy_file = open(os.path.join (current_dir, "proxy_list.txt"), "r")
    proxies = proxy_file.readlines()

    random_proxy = str(random.choices(proxies)[0]).replace("\n", "")
    return random_proxy


