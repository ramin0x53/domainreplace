
import argparse
import re

# Processing command line arguments
parser = argparse.ArgumentParser()

parser.add_argument("-f", help="urls file", dest="file")
parser.add_argument("-d", help="domains file", dest="domains")
parser.add_argument("-r", help="replacement name", dest="rname")
parser.add_argument("-o", help="output file", dest="output")
parser.add_argument("-v", help="value for domains replace", dest="value")

args = parser.parse_args()

base_file = str(args.file)
Replacement = args.rname
domains = str(args.domains)
output = args.output
value = args.value

resultlist = []

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

#Save output
def save_output(list1):
    with open(output, "w") as f:
        for item in list1:
            f.write("%s\n" % item)

#Remove uplicates of list
def remove_dup(x):
  return list(dict.fromkeys(x))

#Remove duplicates from list and save it
def Save_r(list_r):
    save_output(remove_dup(list_r))

#Add url in list
def add_url(url, rpl):

    m = domain_replace(url, rpl)

    if m != False:
        resultlist.append(m)
    
def single_replace():
    with open(base_file) as f:
        for url in f:
            add_url(url.rstrip('\n'), Replacement)
    Save_r(resultlist)

    Save_r(resultlist)

def multi_replace():   
    with open(base_file) as f1, open(domains) as f2:
        for x, y in zip(f1, f2):
            resultlist.append(x.rstrip('\n').replace(value, y.rstrip('\n')))
    save_output(resultlist)

if __name__ == "__main__":

    if value is None:
        single_replace();
    else:
        multi_replace()