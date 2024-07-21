#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('2-hypermedia_pagination').Server
download_csv = __import__('1-simple_pagination').download_csv

csv_url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240721%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240721T103815Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b028f651ca8795f7ae37e4b13393dc795496032dbd7a5736be6eee7e17858d31"
download_csv(csv_url, "Popular_Baby_Names.csv")
server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))