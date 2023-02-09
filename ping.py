import ping3
import pandas as pd

ips = [
    '223.5.5.5','223.6.6.6','114.114.114.114'
]
delays = {}
for ip in ips:
    delay = ping3.ping(ip)
    delays[ip] = delay

df = pd.DataFrame({'IP': list(delays.keys()), 'Delay': list(delays.values())})
df.to_excel('ping_results.xlsx', index=False)
