# Quick Benchmark Detailed Report

**Test Date:** 2024-11-15 00:47:03

## Introduction

This report summarizes the quick iPerf network performance tests conducted on selected servers. The tests measure bandwidth for IPv4 and IPv6 connections under various parallel connections.

## Methodology

The tests were performed using the iPerf3 tool with the following configurations:

- **Interval:** 0.3 seconds
- **Maximum Parallel Connections:** 6
- **Servers Tested:**
  - bhs.proof.ovh.ca -p 5201-5210
  - speedtest.nyc1.us.leaseweb.net -p 5201-5210
  - speedtest.chi11.us.leaseweb.net -p 5201-5210

Each server was tested under the following scenarios:

- Basic IPv4 and IPv6 tests
- Parallel connections with 2, 4, and 6 streams

## Summary of Results

| Server | IPv4 Average Bandwidth (Mbits/sec) | IPv6 Average Bandwidth (Mbits/sec) |
|--------|---------------------------|---------------------------|
| bhs.proof.ovh.ca | 14.10 | 13.50 |
| speedtest.nyc1.us.leaseweb.net | 14.78 | 12.14 |
| speedtest.chi11.us.leaseweb.net | 14.50 | 15.02 |

## Detailed Test Results

### Results for bhs.proof.ovh.ca

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 12.9 Mbits/sec | N/A | N/A |
| basic_ipv6 | 13.5 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | 15.3 Mbits/sec | N/A | N/A |
| parallel_ipv6_2 | N/A | N/A | N/A |
| parallel_ipv4_4 | N/A | N/A | N/A |
| parallel_ipv6_4 | N/A | N/A | N/A |
| parallel_ipv4_6 | N/A | N/A | N/A |
| parallel_ipv6_6 | N/A | N/A | N/A |

### Results for speedtest.nyc1.us.leaseweb.net

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 14.4 Mbits/sec | N/A | N/A |
| basic_ipv6 | 6.65 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | 15.3 Mbits/sec | N/A | N/A |
| parallel_ipv6_2 | 14.5 Mbits/sec | N/A | N/A |
| parallel_ipv4_4 | 14.5 Mbits/sec | N/A | N/A |
| parallel_ipv6_4 | 12.4 Mbits/sec | N/A | N/A |
| parallel_ipv4_6 | 14.9 Mbits/sec | N/A | N/A |
| parallel_ipv6_6 | 15.0 Mbits/sec | N/A | N/A |

### Results for speedtest.chi11.us.leaseweb.net

| Test | Bandwidth | Jitter | Packet Loss |
|------|-----------|--------|-------------|
| basic_ipv4 | 15.1 Mbits/sec | N/A | N/A |
| basic_ipv6 | 15.6 Mbits/sec | N/A | N/A |
| parallel_ipv4_2 | 15.2 Mbits/sec | N/A | N/A |
| parallel_ipv6_2 | 15.7 Mbits/sec | N/A | N/A |
| parallel_ipv4_4 | 14.3 Mbits/sec | N/A | N/A |
| parallel_ipv6_4 | 13.5 Mbits/sec | N/A | N/A |
| parallel_ipv4_6 | 13.4 Mbits/sec | N/A | N/A |
| parallel_ipv6_6 | 15.3 Mbits/sec | N/A | N/A |

## Conclusion

The quick benchmark tests provide a snapshot of the network performance across selected servers. The average bandwidths indicate the network capacity under different parallel connections.
