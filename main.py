#--------------------------------------------------
# python3 main.py file.txt example.com > result.txt
#--------------------------------------------------

import sys
import re

base_file = str(sys.argv[1])
Replacement = str(sys.argv[2])

def domain_replace(link, replacement):

    rg = r"\b([a-z0-9]+(-[a-z0-9]+)*\.)+(?!(cgi|html|js|php|pdf|jsp|txt|png|asp|aspx|css|rb|mp4|mpl|svg|log|xml|tar|zip|dat|db|csv|gif|rss|xhtml|ico|tmp|wmv))[a-z]{2,}\b"

    if "?" not in link:
        return False

    try:
        num = int(str(re.search(r"\b([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\b", link, re.M|re.I))[27:29])
    except:
        return False
    
    temp = re.sub(rg, replacement, link[num:])
    check = re.search(rg, temp, re.M|re.I)
    
    if check == None:
        return False
    
    return link[:num] + temp


def print_url(url, rpl):

    x = domain_replace(url, rpl)

    if x != False:
        print(x)
    

if __name__ == "__main__":
    with open(base_file) as f:
        for url in f:
            print_url(url.rstrip('\n'), Replacement)
