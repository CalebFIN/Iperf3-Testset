import subprocess
import json
import re
from datetime import datetime

# Constants
OUTPUT_FILE = "Quick_Benchmark_results.txt"
REPORT_FILE = "Quick_Benchmark_detailed_report.md"
INTERVAL = 0.3  # Reduced interval
MAX_PARALLEL = 6  # Fewer parallel tests

# Server list in "IP/HOST OPTIONS" format
SERVERS = [
    "bhs.proof.ovh.ca -p 5201-5210",
    "speedtest.nyc1.us.leaseweb.net -p 5201-5210",
    "speedtest.chi11.us.leaseweb.net -p 5201-5210"
]  # Reduced to 3 servers for speed

results = []

def run_command(command):
    try:
        print(f"Executing command: {command}")
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8') + result.stderr.decode('utf-8')
        return output
    except subprocess.CalledProcessError as e:
        error_output = e.stdout.decode('utf-8') + e.stderr.decode('utf-8')
        return f"[ERROR] {error_output}"

def extract_stats(result):
    stats = {}
    # Extract bandwidth
    bandwidth_match = re.findall(r'\[SUM\].*?([0-9\.]+\s[MKG]bits/sec)', result)
    if not bandwidth_match:
        bandwidth_match = re.findall(r'0\.00-.*?sec.*?([0-9\.]+\s[MKG]bits/sec)', result)
    if bandwidth_match:
        stats['bandwidth'] = bandwidth_match[-1]
    else:
        stats['bandwidth'] = "N/A"
    # Extract jitter and packet loss (for UDP tests if applicable)
    jitter_match = re.search(r'([0-9\.]+)\sms\s+jitter', result)
    packet_loss_match = re.search(r'([0-9\.]+)%\s+packet\s+loss', result)
    if jitter_match:
        stats['jitter'] = jitter_match.group(1) + " ms"
    if packet_loss_match:
        stats['packet_loss'] = packet_loss_match.group(1) + "%"
    return stats

def calculate_average_bandwidth(tests, ip_version):
    total_bandwidth = 0.0
    count = 0
    for test in tests:
        if ip_version in test["test"]:
            bandwidth_str = test["stats"].get("bandwidth", "N/A")
            if bandwidth_str != "N/A":
                bandwidth_value = float(bandwidth_str.split()[0])
                unit = bandwidth_str.split()[1]
                # Convert bandwidth to Mbits/sec
                if unit == "Kbits/sec":
                    bandwidth_value /= 1000
                elif unit == "Gbits/sec":
                    bandwidth_value *= 1000
                total_bandwidth += bandwidth_value
                count += 1
    return total_bandwidth / count if count > 0 else "N/A"

# Main execution
def main():
    # Loop through each server and perform tests
    for server in SERVERS:
        server_name = server.split()[0]
        server_results = {"server": server_name, "tests": []}
        print(f"\nRunning tests for {server_name}...")

        # Run basic IPv4 test
        print(f"Running basic IPv4 test for {server_name}")
        ipv4_result = run_command(f"iperf3 -4 -c {server} -P 1 -i {INTERVAL}")
        server_results["tests"].append({
            "test": "basic_ipv4",
            "result": ipv4_result,
            "stats": extract_stats(ipv4_result)
        })

        # Run basic IPv6 test
        print(f"Running basic IPv6 test for {server_name}")
        ipv6_result = run_command(f"iperf3 -6 -c {server} -P 1 -i {INTERVAL}")
        server_results["tests"].append({
            "test": "basic_ipv6",
            "result": ipv6_result,
            "stats": extract_stats(ipv6_result)
        })

        # Incremental Parallel Connections Test
        for parallel in [2, 4, MAX_PARALLEL]:  # Limited parallel tests
            print(f"Running IPv4 test with {parallel} parallel connections on {server_name}")
            parallel_ipv4_result = run_command(f"iperf3 -4 -c {server} -P {parallel} -i {INTERVAL}")
            server_results["tests"].append({
                "test": f"parallel_ipv4_{parallel}",
                "result": parallel_ipv4_result,
                "stats": extract_stats(parallel_ipv4_result)
            })

            print(f"Running IPv6 test with {parallel} parallel connections on {server_name}")
            parallel_ipv6_result = run_command(f"iperf3 -6 -c {server} -P {parallel} -i {INTERVAL}")
            server_results["tests"].append({
                "test": f"parallel_ipv6_{parallel}",
                "result": parallel_ipv6_result,
                "stats": extract_stats(parallel_ipv6_result)
            })

        print(f"Completed tests for {server_name}. Results stored in memory.")
        results.append(server_results)

    # Write results to the output file in JSON format
    with open(OUTPUT_FILE, "w") as f:
        f.write(json.dumps(results, indent=4))

    # Generate the detailed report
    generate_report(results)
    print(f"\nAll tests completed! Results are stored in {OUTPUT_FILE} and {REPORT_FILE}")

def generate_report(data):
    report_content = "# Quick Benchmark Detailed Report\n\n"
    report_content += f"**Test Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    # Introduction
    report_content += "## Introduction\n\n"
    report_content += "This report summarizes the quick iPerf network performance tests conducted on selected servers. The tests measure bandwidth for IPv4 and IPv6 connections under various parallel connections.\n\n"

    # Methodology
    report_content += "## Methodology\n\n"
    report_content += "The tests were performed using the iPerf3 tool with the following configurations:\n\n"
    report_content += f"- **Interval:** {INTERVAL} seconds\n"
    report_content += f"- **Maximum Parallel Connections:** {MAX_PARALLEL}\n"
    report_content += "- **Servers Tested:**\n"
    for server in SERVERS:
        report_content += f"  - {server}\n"
    report_content += "\nEach server was tested under the following scenarios:\n\n"
    report_content += "- Basic IPv4 and IPv6 tests\n"
    report_content += "- Parallel connections with 2, 4, and 6 streams\n\n"

    # Summary Table of Averages
    report_content += "## Summary of Results\n\n"
    report_content += "| Server | IPv4 Average Bandwidth (Mbits/sec) | IPv6 Average Bandwidth (Mbits/sec) |\n"
    report_content += "|--------|---------------------------|---------------------------|\n"

    # Calculate averages and add them to the summary table
    for server_result in data:
        server_name = server_result["server"]
        ipv4_avg = calculate_average_bandwidth(server_result["tests"], "ipv4")
        ipv6_avg = calculate_average_bandwidth(server_result["tests"], "ipv6")
        ipv4_avg_str = f"{ipv4_avg:.2f}" if isinstance(ipv4_avg, float) else "N/A"
        ipv6_avg_str = f"{ipv6_avg:.2f}" if isinstance(ipv6_avg, float) else "N/A"
        report_content += f"| {server_name} | {ipv4_avg_str} | {ipv6_avg_str} |\n"

    # Detailed Results for Each Server
    report_content += "\n## Detailed Test Results\n\n"
    for server_result in data:
        server_name = server_result["server"]
        report_content += f"### Results for {server_name}\n\n"
        report_content += "| Test | Bandwidth | Jitter | Packet Loss |\n"
        report_content += "|------|-----------|--------|-------------|\n"

        for test in server_result["tests"]:
            test_name = test["test"]
            stats = test["stats"]
            bandwidth = stats.get("bandwidth", "N/A")
            jitter = stats.get("jitter", "N/A")
            packet_loss = stats.get("packet_loss", "N/A")
            report_content += f"| {test_name} | {bandwidth} | {jitter} | {packet_loss} |\n"

        report_content += "\n"

    # Conclusion
    report_content += "## Conclusion\n\n"
    report_content += "The quick benchmark tests provide a snapshot of the network performance across selected servers. The average bandwidths indicate the network capacity under different parallel connections.\n"

    # Write the complete report to the markdown file
    with open(REPORT_FILE, "w") as f:
        f.write(report_content)

if __name__ == "__main__":
    main()
