import ifaddr
adapters = ifaddr.get_adapters()
for adapter in adapters:  #itiration starts
    print("IP'S of network adapter" + adapter.nice_name) #nice_name - fetches the name of the 'adaptor'
    for ip in adapter.ips:
        print(" %s/%s" %(ip.ip, ip.network_prefix))
print("***********************************************")
adapters = ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("IP'S of network adapter" + adapter.nice_name)
    if adapter.ips:
        for ip in adapter.ips:
            print(" %s/%s" %(ip.ip, ip.network_prefix))
    else:
        print(" no ip's configured")