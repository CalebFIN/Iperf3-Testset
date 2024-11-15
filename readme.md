# Iperf3-Testset

This repository contains Python scripts designed to automate network performance testing using [iPerf3](https://iperf.fr/). The scripts compare IPv4 and IPv6 throughput across multiple servers with various test scenarios.

## Overview

- **`Long_Benchmark.py`**: A comprehensive benchmarking script that performs extensive tests. Ideal for in-depth analysis but takes longer to complete.
- **`Quick_Benchmark.py`**: A faster benchmarking script that runs a subset of tests for quicker results, suitable for rapid assessments.

## Features

- **Automated Testing**: Runs iPerf3 tests across multiple servers and configurations without manual intervention.
- **IPv4 vs. IPv6 Comparison**: Measures and compares the performance differences between IPv4 and IPv6 protocols.
- **Detailed Reporting**: Generates markdown reports summarizing test results, including bandwidth, jitter, and packet loss.
- **Customizable Parameters**: Easily adjust server lists, intervals, and parallel connections to suit your testing needs.

## Requirements

- **Python 3.x**
- **iPerf3** installed on your system
  - Installation instructions can be found [here](https://iperf.fr/iperf-download.php).
- **Access to Public iPerf3 Servers**
  - The scripts use [publicly available servers](https://iperf3serverlist.net/) listed in the `SERVERS` variable.

## Installation

Clone the repository to your local machine:

```shell
git clone https://github.com/CalebFIN/Iperf3-Testset.git
cd Iperf3-Testset
```

## Usage

### Running the Quick Benchmark

The quick benchmark script performs a faster set of tests suitable for quick assessments.

```shell
python3 Quick_Benchmark.py
```

- **Output Files**:
  - `Quick_Benchmark_results.txt`: Raw test results in JSON format.
  - `Quick_Benchmark_detailed_report.md`: A detailed markdown report of the test results.

### Running the Long Benchmark

The long benchmark script performs comprehensive tests and is ideal for in-depth analysis.

```shell
python3 Long_Benchmark.py
```

- **Output Files**:
  - `Long_Benchmark_results.txt`: Raw test results in JSON format.
  - `Long_Benchmark_detailed_report.md`: A detailed markdown report of the test results.

## Script Details

### Test Scenarios

Both scripts perform the following test scenarios:

- **Basic Tests**: Single connection tests for both download and upload (reverse mode).
- **Parallel Connections**: Tests with multiple parallel streams (from 2 up to a maximum specified by `MAX_PARALLEL`).
- **Multi-Port Tests**: Utilizes multiple ports to test simultaneous connections, enhancing the stress on the network.
- **Incremental Tests**: Gradually increases the number of parallel connections to observe performance scaling.

### Customization

- **Server List**: Modify the `SERVERS` list within the scripts to add or remove servers.
- **Test Parameters**:
  - `INTERVAL`: Adjust the interval between reports.
  - `MAX_PARALLEL`: Set the maximum number of parallel connections.
- **Output Files**: Change the `OUTPUT_FILE` and `REPORT_FILE` variables to customize output filenames.

## Sample Report

An example of the generated report can be found in [Quick_Benchmark_detailed_report.md](Quick_Benchmark_detailed_report.md). The report includes:

- **Introduction**: Overview of the tests conducted.
- **Methodology**: Detailed explanation of the testing procedures.
- **Summary of Results**: Average bandwidth comparisons between IPv4 and IPv6.
- **Detailed Test Results**: Per-server and per-test scenario results.
- **Conclusion**: Summary and insights from the test results.

## Example

Here's how you might run the quick benchmark and view the report:

```shell
python3 Quick_Benchmark.py
```

After the script completes, open `Quick_Benchmark_detailed_report.md` to view the results.

## Contributing

Contributions are welcome! If you'd like to add features or improve the scripts:

1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Submit a pull request.


## Acknowledgments

- **Public iPerf3 Servers**: Thanks to the maintainers of the public iPerf3 servers used in these tests.
- **Inspiration**: These scripts were developed as part of a study on IPv4 vs. IPv6 throughput testing.

## Related Blog Post

For a detailed explanation of the testing process and findings, refer to the blog post:

[IPv4 vs IPv6 Throughput Testing](https://cfinigan.com/posts/MOJO-Language-Learning/)

---
