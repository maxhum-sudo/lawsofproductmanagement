import http.server, os, sys
os.chdir("/Users/max/Documents/lawsofproductmanagement")
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8743, bind="127.0.0.1")
