# Geoip

Get ip related information and website.


## Website

Only use data that is updated in a timely manner and rich in data

| web              | example                                                      | data                   |
| ---------------- | ------------------------------------------------------------ | ---------------------- |
| ip.gs            | [ip-gs](https://ip.gs/json?ip=223.5.5.5)                     |                        |
| ip-api.com       | [ip-api_free](http://ip-api.com/json/1.1.1.1?fields=66846719&lang=en) / [pro](https://pro.ip-api.com/json/?fields=16985625&key=EEKS6bLi6D91G1p)(ip&domain) |                        |
| ipinfo.io        | [ipinfo](https://ipinfo.io/2.2.2.2/json)                     |                        |
| maxmind.com      | [maxmind](https://dev.maxmind.com/)                          | need key               |
| ip2location.com  | demo need verify                                             | need key               |
| ipgeolocation.io | [ipgeolocation](https://prox.zigou23.tk/https/api.ipgeolocation.io/ipgeo?include=hostname&ip=5.62.56.160)(ip&domain) 1k/d | need key()             |
| db-ip            | [db-ip](https://db-ip.com/demo/home.php?s=5.62.56.160)(ASN&ip) |                        |
| IPregistry.co    | [ipregistry](https://api.ipregistry.co/5.62.56.160?key=) only 100,000times/life | need key()             |
| ipapi.co         | [ipapi-co](https://ipapi.co/5.62.56.160/json/) 1k/d          |                        |
| ipapi.com        | [ipapi](https://ipapi.com/ip_api.php?ip=5.62.56.160) 1k/m    |                        |
| ipdata.co        | [ipdata](https://api.ipdata.co/5.62.56.160?api-key=) need key | need key, database old |
| ipleak.net       | [ipleak.net](https://ipleak.net/?mode=json&ip=5.62.56.160)   |                        |
| ipify.org        | [ipify.org](https://geo.ipify.org/api/v2/country?apiKey=&ipAddress=8.8.8.8) | need pro               |
|abstractapi.com|[abstractapi.com](https://app.abstractapi.com/api/ip-geolocation/pricing) 20k/m| need key |

china:

| web          | example                                                      | data |
| ------------ | ------------------------------------------------------------ | ---- |
| speedtest.cn | [speedtest-cn](https://forge.speedtest.cn/api/location/info?ip=1.1.1.1) |      |
| ip.sb        | [ip-sb](https://api.ip.sb/geoip/185.222.222.222)             |      |
| zxinc.org    | [zxinc](https://ip.zxinc.org/api.php?type=json&ip=1.1.1.1)   |      |
|              |                                                              |      |

### Other Data Interface Website

| web                | example                                                      | data                                       |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------ |
| skk.moe            | [ip.skk.moe](https://ip.skk.moe)                             |                                            |
| geoip.deno.dev(my) | [geoip.deno.dev](https://geoip.deno.dev) / [Api](https://geoip.deno.dev/ip?ip=223.5.5.5) | ipinfo&dbip                                |
| ipqi.co            | [ipqi](https://ipqi.co/?ip=5.62.56.160)                      |                                            |
| geoip.rs           | [geoip.rs](https://api.geoip.rs/?ip=5.62.56.160&lang=en&callback=my_en_function) / [GH](https://github.com/ffissore/geoip-rs) | 30k req/s                                  |
| iplocation.net     | [iplocation](https://www.iplocation.net/ip-lookup)           | ip2l&ipinfo&DB-IP&IPreg&IPgeo&IPapi&ipdata |
| ip111.cn           | other api                                                    |                                            |

## only query

| web           | example                                                    | data |
| ------------- | ---------------------------------------------------------- | ---- |
| bili          | http://api.bilibili.com/x/web-interface/zone               |      |
| upaiyun.com   | [又拍云](https://pubstatic.b0.upaiyun.com/?_upnode)        |      |
| ip138.com     | [ip138](https://2022.ip138.com/)                           |      |
| cf-ns.com     | [China CloudFlare](https://cf-ns.com/cdn-cgi/trace) no sql |      |
| wtfismyip.com | [wtfismyip](https://wtfismyip.com/json)                    |      |
