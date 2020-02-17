import requests
import argparse
import urllib3 #only disable SSL warnings

urllib3.disable_warnings()#only disable SSL warnings

#Get arguments

parser=argparse.ArgumentParser(description='API scanner for check available methods')
parser.add_argument("url", help="URL of scanning resource", action='store')
parser.add_argument("prefix", help="URL prefix", action='store')
parser.add_argument("--method", help="using HTTP method. Default GET.")
parser.add_argument("list", help="file with methods to check", action='store')
parser.add_argument("--user-agent", help="User-Agent header for HTTP requests")
args=parser.parse_args()

# For testing :)
# print(args.url)
# print(args.prefix)

#preparing the URL
url=args.url+"/"+args.prefix+"/"
# print(final_url) for testing :)

#Check existing file and build final URL. After that making request for check methods from list
try:
    f=open(args.list)
    for line in f:
        final_url=url+line
        print(final_url)
        if args.method == 'post':
            check_r=requests.post(final_url, verify=False)
            print(check_r.status_code)
        else:
            check_r=requests.get(final_url, verify=False)
            print(check_r.status_code)
except FileNotFoundError:
    print("File not Found!")
    # print(final_url) for testing
