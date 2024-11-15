# iPerf Test Detailed Report

**Test Date:** 2024-11-15 02:38:03

## Introduction

This report summarizes the iPerf network performance tests conducted on multiple servers. The tests measure bandwidth, jitter, and packet loss for IPv4 and IPv6 connections under various conditions.

## Methodology

The tests were performed using the iPerf3 tool with the following configurations:

- **Interval:** 0.5 seconds
- **Maximum Parallel Connections:** 8
- **Servers Tested:**
  - bhs.proof.ovh.ca -p 5201-5210
  - speedtest.mtl2.ca.leaseweb.net -p 5201-5210
  - speedtest.chi11.us.leaseweb.net -p 5201-5210
  - speedtest.dal13.us.leaseweb.net -p 5201-5210
  - speedtest.lax12.us.leaseweb.net -p 5201-5210
  - speedtest.mia11.us.leaseweb.net -p 5201-5210
  - speedtest.nyc1.us.leaseweb.net -p 5201-5210
  - speedtest.phx1.us.leaseweb.net -p 5201-5210
  - speedtest.sfo12.us.leaseweb.net -p 5201-5210
  - speedtest.sea11.us.leaseweb.net -p 5201-5210

Each server was tested under the following scenarios:

- Basic IPv4 and IPv6 tests
- Reverse mode tests
- Incremental parallel connections (2 to 8)
- Multi-port test with maximum parallel connections

## Summary of Results

| Server | IPv4 Average Bandwidth (Mbits/sec) | IPv6 Average Bandwidth (Mbits/sec) |
|--------|---------------------------|---------------------------|
| bhs.proof.ovh.ca | 46.54 | N/A |
| speedtest.mtl2.ca.leaseweb.net | 36.53 | 31.05 |
| speedtest.chi11.us.leaseweb.net | 30.82 | 34.09 |
| speedtest.dal13.us.leaseweb.net | 37.60 | 31.83 |
| speedtest.lax12.us.leaseweb.net | 36.04 | 32.73 |
| speedtest.mia11.us.leaseweb.net | 40.23 | 31.47 |
| speedtest.nyc1.us.leaseweb.net | 52.36 | 35.45 |
| speedtest.phx1.us.leaseweb.net | 39.05 | 31.16 |
| speedtest.sfo12.us.leaseweb.net | 28.99 | 38.08 |
| speedtest.sea11.us.leaseweb.net | 53.26 | 33.38 |

## Detailed Test Results

### Results for bhs.proof.ovh.ca

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 7.55 Mbits/sec | N/A | N/A |
| reverse_ipv4 | 124 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | 8.06 Mbits/sec | N/A | N/A |
| parallel_ipv4_3 | N/A | N/A | N/A |
| parallel_ipv4_4 | N/A | N/A | N/A |
| parallel_ipv4_5 | N/A | N/A | N/A |
| parallel_ipv4_6 | N/A | N/A | N/A |
| parallel_ipv4_7 | N/A | N/A | N/A |
| parallel_ipv4_8 | N/A | N/A | N/A |
| multi_port_ipv4 | N/A | N/A | N/A |
| basic_ipv6 | N/A | N/A | N/A |
| reverse_ipv6 | N/A | N/A | N/A |
| parallel_ipv6_2 | N/A | N/A | N/A |
| parallel_ipv6_3 | N/A | N/A | N/A |
| parallel_ipv6_4 | N/A | N/A | N/A |
| parallel_ipv6_5 | N/A | N/A | N/A |
| parallel_ipv6_6 | N/A | N/A | N/A |
| parallel_ipv6_7 | N/A | N/A | N/A |
| parallel_ipv6_8 | N/A | N/A | N/A |
| multi_port_ipv6 | N/A | N/A | N/A |

### Results for speedtest.mtl2.ca.leaseweb.net

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 6.28 Mbits/sec | N/A | N/A |
| reverse_ipv4 | 158 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | 5.69 Mbits/sec | N/A | N/A |
| parallel_ipv4_3 | 7.16 Mbits/sec | N/A | N/A |
| parallel_ipv4_4 | 7.25 Mbits/sec | N/A | N/A |
| parallel_ipv4_5 | 7.43 Mbits/sec | N/A | N/A |
| parallel_ipv4_6 | 7.59 Mbits/sec | N/A | N/A |
| parallel_ipv4_7 | 7.56 Mbits/sec | N/A | N/A |
| parallel_ipv4_8 | 7.37 Mbits/sec | N/A | N/A |
| multi_port_ipv4 | 151 Mbits/sec | N/A | N/A |
| basic_ipv6 | 7.45 Mbits/sec | N/A | N/A |
| reverse_ipv6 | 110 Mbits/sec | N/A | N/A |
| parallel_ipv6_2 | 7.51 Mbits/sec | N/A | N/A |
| parallel_ipv6_3 | 7.61 Mbits/sec | N/A | N/A |
| parallel_ipv6_4 | 7.42 Mbits/sec | N/A | N/A |
| parallel_ipv6_5 | 7.11 Mbits/sec | N/A | N/A |
| parallel_ipv6_6 | 7.19 Mbits/sec | N/A | N/A |
| parallel_ipv6_7 | 7.34 Mbits/sec | N/A | N/A |
| parallel_ipv6_8 | 6.87 Mbits/sec | N/A | N/A |
| multi_port_ipv6 | 142 Mbits/sec | N/A | N/A |

### Results for speedtest.chi11.us.leaseweb.net

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 7.16 Mbits/sec | N/A | N/A |
| reverse_ipv4 | 85.5 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | 7.55 Mbits/sec | N/A | N/A |
| parallel_ipv4_3 | 7.68 Mbits/sec | N/A | N/A |
| parallel_ipv4_4 | 7.83 Mbits/sec | N/A | N/A |
| parallel_ipv4_5 | 7.98 Mbits/sec | N/A | N/A |
| parallel_ipv4_6 | 8.01 Mbits/sec | N/A | N/A |
| parallel_ipv4_7 | 7.74 Mbits/sec | N/A | N/A |
| parallel_ipv4_8 | 7.77 Mbits/sec | N/A | N/A |
| multi_port_ipv4 | 161 Mbits/sec | N/A | N/A |
| basic_ipv6 | 7.71 Mbits/sec | N/A | N/A |
| reverse_ipv6 | 154 Mbits/sec | N/A | N/A |
| parallel_ipv6_2 | 7.58 Mbits/sec | N/A | N/A |
| parallel_ipv6_3 | 7.89 Mbits/sec | N/A | N/A |
| parallel_ipv6_4 | 7.59 Mbits/sec | N/A | N/A |
| parallel_ipv6_5 | 7.57 Mbits/sec | N/A | N/A |
| parallel_ipv6_6 | 7.59 Mbits/sec | N/A | N/A |
| parallel_ipv6_7 | 7.54 Mbits/sec | N/A | N/A |
| parallel_ipv6_8 | 7.45 Mbits/sec | N/A | N/A |
| multi_port_ipv6 | 126 Mbits/sec | N/A | N/A |

### Results for speedtest.dal13.us.leaseweb.net

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 7.52 Mbits/sec | N/A | N/A |
| reverse_ipv4 | 144 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | 7.68 Mbits/sec | N/A | N/A |
| parallel_ipv4_3 | 7.35 Mbits/sec | N/A | N/A |
| parallel_ipv4_4 | 7.61 Mbits/sec | N/A | N/A |
| parallel_ipv4_5 | 7.36 Mbits/sec | N/A | N/A |
| parallel_ipv4_6 | 7.59 Mbits/sec | N/A | N/A |
| parallel_ipv4_7 | 7.35 Mbits/sec | N/A | N/A |
| parallel_ipv4_8 | 7.53 Mbits/sec | N/A | N/A |
| multi_port_ipv4 | 172 Mbits/sec | N/A | N/A |
| basic_ipv6 | 7.18 Mbits/sec | N/A | N/A |
| reverse_ipv6 | 127 Mbits/sec | N/A | N/A |
| parallel_ipv6_2 | 6.94 Mbits/sec | N/A | N/A |
| parallel_ipv6_3 | 6.57 Mbits/sec | N/A | N/A |
| parallel_ipv6_4 | 6.66 Mbits/sec | N/A | N/A |
| parallel_ipv6_5 | 6.54 Mbits/sec | N/A | N/A |
| parallel_ipv6_6 | 6.65 Mbits/sec | N/A | N/A |
| parallel_ipv6_7 | 6.22 Mbits/sec | N/A | N/A |
| parallel_ipv6_8 | 6.58 Mbits/sec | N/A | N/A |
| multi_port_ipv6 | 138 Mbits/sec | N/A | N/A |

### Results for speedtest.lax12.us.leaseweb.net

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 6.51 Mbits/sec | N/A | N/A |
| reverse_ipv4 | 140 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | 6.66 Mbits/sec | N/A | N/A |
| parallel_ipv4_3 | 6.27 Mbits/sec | N/A | N/A |
| parallel_ipv4_4 | 7.42 Mbits/sec | N/A | N/A |
| parallel_ipv4_5 | 6.50 Mbits/sec | N/A | N/A |
| parallel_ipv4_6 | 6.06 Mbits/sec | N/A | N/A |
| parallel_ipv4_7 | 6.03 Mbits/sec | N/A | N/A |
| parallel_ipv4_8 | 5.92 Mbits/sec | N/A | N/A |
| multi_port_ipv4 | 169 Mbits/sec | N/A | N/A |
| basic_ipv6 | 5.82 Mbits/sec | N/A | N/A |
| reverse_ipv6 | 152 Mbits/sec | N/A | N/A |
| parallel_ipv6_2 | 6.48 Mbits/sec | N/A | N/A |
| parallel_ipv6_3 | 6.57 Mbits/sec | N/A | N/A |
| parallel_ipv6_4 | 6.42 Mbits/sec | N/A | N/A |
| parallel_ipv6_5 | 6.15 Mbits/sec | N/A | N/A |
| parallel_ipv6_6 | 5.88 Mbits/sec | N/A | N/A |
| parallel_ipv6_7 | 6.32 Mbits/sec | N/A | N/A |
| parallel_ipv6_8 | 6.65 Mbits/sec | N/A | N/A |
| multi_port_ipv6 | 125 Mbits/sec | N/A | N/A |

### Results for speedtest.mia11.us.leaseweb.net

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 6.92 Mbits/sec | N/A | N/A |
| reverse_ipv4 | 178 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | 7.04 Mbits/sec | N/A | N/A |
| parallel_ipv4_3 | 7.20 Mbits/sec | N/A | N/A |
| parallel_ipv4_4 | 7.56 Mbits/sec | N/A | N/A |
| parallel_ipv4_5 | 6.92 Mbits/sec | N/A | N/A |
| parallel_ipv4_6 | 6.61 Mbits/sec | N/A | N/A |
| parallel_ipv4_7 | 6.43 Mbits/sec | N/A | N/A |
| parallel_ipv4_8 | 5.59 Mbits/sec | N/A | N/A |
| multi_port_ipv4 | 170 Mbits/sec | N/A | N/A |
| basic_ipv6 | 5.65 Mbits/sec | N/A | N/A |
| reverse_ipv6 | 140 Mbits/sec | N/A | N/A |
| parallel_ipv6_2 | 6.36 Mbits/sec | N/A | N/A |
| parallel_ipv6_3 | 6.31 Mbits/sec | N/A | N/A |
| parallel_ipv6_4 | 6.34 Mbits/sec | N/A | N/A |
| parallel_ipv6_5 | 6.37 Mbits/sec | N/A | N/A |
| parallel_ipv6_6 | 6.63 Mbits/sec | N/A | N/A |
| parallel_ipv6_7 | 7.18 Mbits/sec | N/A | N/A |
| parallel_ipv6_8 | 10.9 Mbits/sec | N/A | N/A |
| multi_port_ipv6 | 119 Mbits/sec | N/A | N/A |

### Results for speedtest.nyc1.us.leaseweb.net

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 13.7 Mbits/sec | N/A | N/A |
| reverse_ipv4 | 193 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | 13.1 Mbits/sec | N/A | N/A |
| parallel_ipv4_3 | 14.0 Mbits/sec | N/A | N/A |
| parallel_ipv4_4 | 13.3 Mbits/sec | N/A | N/A |
| parallel_ipv4_5 | 13.1 Mbits/sec | N/A | N/A |
| parallel_ipv4_6 | 12.5 Mbits/sec | N/A | N/A |
| parallel_ipv4_7 | 13.0 Mbits/sec | N/A | N/A |
| parallel_ipv4_8 | 12.9 Mbits/sec | N/A | N/A |
| multi_port_ipv4 | 225 Mbits/sec | N/A | N/A |
| basic_ipv6 | 14.2 Mbits/sec | N/A | N/A |
| reverse_ipv6 | 124 Mbits/sec | N/A | N/A |
| parallel_ipv6_2 | 13.8 Mbits/sec | N/A | N/A |
| parallel_ipv6_3 | 14.3 Mbits/sec | N/A | N/A |
| parallel_ipv6_4 | 14.5 Mbits/sec | N/A | N/A |
| parallel_ipv6_5 | 14.0 Mbits/sec | N/A | N/A |
| parallel_ipv6_6 | 14.2 Mbits/sec | N/A | N/A |
| parallel_ipv6_7 | 14.6 Mbits/sec | N/A | N/A |
| parallel_ipv6_8 | 14.9 Mbits/sec | N/A | N/A |
| multi_port_ipv6 | 116 Mbits/sec | N/A | N/A |

### Results for speedtest.phx1.us.leaseweb.net

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 14.1 Mbits/sec | N/A | N/A |
| reverse_ipv4 | 103 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | 11.5 Mbits/sec | N/A | N/A |
| parallel_ipv4_3 | 11.1 Mbits/sec | N/A | N/A |
| parallel_ipv4_4 | 11.7 Mbits/sec | N/A | N/A |
| parallel_ipv4_5 | 12.7 Mbits/sec | N/A | N/A |
| parallel_ipv4_6 | 13.6 Mbits/sec | N/A | N/A |
| parallel_ipv4_7 | 13.3 Mbits/sec | N/A | N/A |
| parallel_ipv4_8 | 13.5 Mbits/sec | N/A | N/A |
| multi_port_ipv4 | 186 Mbits/sec | N/A | N/A |
| basic_ipv6 | 12.7 Mbits/sec | N/A | N/A |
| reverse_ipv6 | 95.7 Mbits/sec | N/A | N/A |
| parallel_ipv6_2 | 14.7 Mbits/sec | N/A | N/A |
| parallel_ipv6_3 | 13.2 Mbits/sec | N/A | N/A |
| parallel_ipv6_4 | 14.5 Mbits/sec | N/A | N/A |
| parallel_ipv6_5 | 14.9 Mbits/sec | N/A | N/A |
| parallel_ipv6_6 | 14.6 Mbits/sec | N/A | N/A |
| parallel_ipv6_7 | 15.1 Mbits/sec | N/A | N/A |
| parallel_ipv6_8 | 15.2 Mbits/sec | N/A | N/A |
| multi_port_ipv6 | 101 Mbits/sec | N/A | N/A |

### Results for speedtest.sfo12.us.leaseweb.net

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 14.2 Mbits/sec | N/A | N/A |
| reverse_ipv4 | 131 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | N/A | N/A | N/A |
| parallel_ipv4_3 | 14.2 Mbits/sec | N/A | N/A |
| parallel_ipv4_4 | 14.5 Mbits/sec | N/A | N/A |
| parallel_ipv4_5 | 14.3 Mbits/sec | N/A | N/A |
| parallel_ipv4_6 | 14.4 Mbits/sec | N/A | N/A |
| parallel_ipv4_7 | 14.5 Mbits/sec | N/A | N/A |
| parallel_ipv4_8 | 14.8 Mbits/sec | N/A | N/A |
| multi_port_ipv4 | N/A | N/A | N/A |
| basic_ipv6 | 14.6 Mbits/sec | N/A | N/A |
| reverse_ipv6 | 128 Mbits/sec | N/A | N/A |
| parallel_ipv6_2 | 14.5 Mbits/sec | N/A | N/A |
| parallel_ipv6_3 | 16.1 Mbits/sec | N/A | N/A |
| parallel_ipv6_4 | 15.7 Mbits/sec | N/A | N/A |
| parallel_ipv6_5 | 15.3 Mbits/sec | N/A | N/A |
| parallel_ipv6_6 | 15.1 Mbits/sec | N/A | N/A |
| parallel_ipv6_7 | 14.8 Mbits/sec | N/A | N/A |
| parallel_ipv6_8 | 14.7 Mbits/sec | N/A | N/A |
| multi_port_ipv6 | 132 Mbits/sec | N/A | N/A |

### Results for speedtest.sea11.us.leaseweb.net

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 14.6 Mbits/sec | N/A | N/A |
| reverse_ipv4 | 199 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | 15.2 Mbits/sec | N/A | N/A |
| parallel_ipv4_3 | 14.7 Mbits/sec | N/A | N/A |
| parallel_ipv4_4 | 15.0 Mbits/sec | N/A | N/A |
| parallel_ipv4_5 | 14.7 Mbits/sec | N/A | N/A |
| parallel_ipv4_6 | 14.5 Mbits/sec | N/A | N/A |
| parallel_ipv4_7 | 14.2 Mbits/sec | N/A | N/A |
| parallel_ipv4_8 | 14.7 Mbits/sec | N/A | N/A |
| multi_port_ipv4 | 216 Mbits/sec | N/A | N/A |
| basic_ipv6 | 14.3 Mbits/sec | N/A | N/A |
| reverse_ipv6 | 92.7 Mbits/sec | N/A | N/A |
| parallel_ipv6_2 | 14.0 Mbits/sec | N/A | N/A |
| parallel_ipv6_3 | 13.7 Mbits/sec | N/A | N/A |
| parallel_ipv6_4 | 13.7 Mbits/sec | N/A | N/A |
| parallel_ipv6_5 | 13.6 Mbits/sec | N/A | N/A |
| parallel_ipv6_6 | 14.0 Mbits/sec | N/A | N/A |
| parallel_ipv6_7 | 13.8 Mbits/sec | N/A | N/A |
| parallel_ipv6_8 | 14.0 Mbits/sec | N/A | N/A |
| multi_port_ipv6 | 130 Mbits/sec | N/A | N/A |

## Conclusion

The tests provide insight into the network performance across different servers and configurations. The average bandwidths indicate the overall network capacity, while the detailed results highlight performance under specific conditions.
