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