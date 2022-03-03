# Collection of CollectD scripts to collect informatoin to push into influxDB


## LSOF for EOSIO

* lsofeosio.py

### 📌 Description

Using LSOF you can monitor the amount of P2P connections your EOSIO process has.

Plugin example

```
<Plugin python>
    ModulePath "/usr/share/collectd/plugins"
    Import "lsof_eosio"
    <Module lsof_eosio>
        http_port "8888"
    </Module>
</Plugin>
```

## haproxy module

* haproxy.py

### 📌 Description

It uses the UNIX Socket commands to monitor stats from the show info, show stat and show resolvers commands. This allows monitoring of haproxy status as well as frontends, backends, servers and resolvers configured.

This plugin was forked and modified from Signalfx's haproxy plugin in order to output non signalfx specific names and output resolver/nameserver information.

Plugin example:
- specify the frontend and backend names.

```
<Plugin python>
    ModulePath "/usr/share/collectd/plugins"

    Import "haproxy"

    <Module haproxy>
      Socket "/run/haproxy/admin.sock"
      # HAproxy backend for all requests
      ProxyMonitor "wax_nodes"
      ProxyMonitor "eoshttps"
    </Module>
</Plugin>
```
