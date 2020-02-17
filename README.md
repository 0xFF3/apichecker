# apichecker
API scanner for get available methods. Require Python3

Install:
git clone https://github.com/0xFF3/apichecker

Run:

python3 apichecker.py "API url" "URL preffix" "file with methods"

Example:

python3 apichecker.py https://api.domainsdb.info v1 methods.txt

Optional args:
--method - HTTP method (GET or POST)
--agent - HTTP user-agent(default use requests lib value)

