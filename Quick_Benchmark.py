import subprocess
import time
import json
import re

OUTPUT_FILE = "Quick_Benchmark_results.txt"
MARKDOWN_FILE = "Quick_Benchmark_results.md"
INTERVAL = 0.3  # Reduced interval
MAX_PARALLEL = 6  # Fewer parallel tests

# Clear the output file and write a header
results = []

# Server list in "IP/HOST OPTIONS" format
SERVERS = [
    "bhs.proof.ovh.ca -p 5201-5210",
    "speedtest.nyc1.us.leaseweb.net -p 5201-5210",
    "speedtest.chi11.us.leaseweb.net -p 5201-5210"
]  # Reduced to 3 servers for speed

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f"[ERROR] {e}"

def extract_stats(result):
    stats = {}
    bandwidth_match = re.search(r'([0-9\.]+\sMbits/sec)', result)
    if bandwidth_match:
        stats['bandwidth'] = bandwidth_match.group(1)
    return stats

# Loop through each server and perform tests
for server in SERVERS:
    server_name = server.split()[0]
    server_results = {"server": server_name, "tests": []}
    print(f"Running tests for {server_name}...")

    # Run basic IPv4 test
    print(f"Running basic IPv4 test for {server_name}")
    ipv4_result = run_command(f"iperf3 -4 -c {server} -P 1 -i {INTERVAL}")
    server_results["tests"].append({"test": "basic_ipv4", "result": ipv4_result, "stats": extract_stats(ipv4_result)})

    # Run basic IPv6 test
    print(f"Running basic IPv6 test for {server_name}")
    ipv6_result = run_command(f"iperf3 -6 -c {server} -P 1 -i {INTERVAL}")
    server_results["tests"].append({"test": "basic_ipv6", "result": ipv6_result, "stats": extract_stats(ipv6_result)})

    # Incremental Parallel Connections Test
    for parallel in [2, 4, MAX_PARALLEL]:  # Limited parallel tests
        print(f"Running test with {parallel} parallel connections on {server_name}")
        parallel_ipv4_result = run_command(f"iperf3 -4 -c {server} -P {parallel} -i {INTERVAL}")
        server_results["tests"].append({"test": f"parallel_ipv4_{parallel}", "result": parallel_ipv4_result, "stats": extract_stats(parallel_ipv4_result)})

        parallel_ipv6_result = run_command(f"iperf3 -6 -c {server} -P {parallel} -i {INTERVAL}")
        server_results["tests"].append({"test": f"parallel_ipv6_{parallel}", "result": parallel_ipv6_result, "stats": extract_stats(parallel_ipv6_result)})

    print(f"Completed tests for {server_name}. Results stored in memory.")
    results.append(server_results)

# Write results to the output file in a nicely formatted way
with open(OUTPUT_FILE, "w") as f:
    f.write(json.dumps(results, indent=4))

# Write results to the markdown file in a nicely formatted way
with open(MARKDOWN_FILE, "w") as f:
    f.write("# iPerf Test Results\n\n")
    for server_result in results:
        f.write(f"## Results for {server_result['server']}\n\n")
        for test in server_result["tests"]:
            f.write(f"### {test['test']}\n")
            f.write(f"""**Result:**\n```
{test['result']}\n```
""")
            f.write(f"**Stats:**\n")
            for stat_key, stat_value in test["stats"].items():
                f.write(f"- {stat_key}: {stat_value}\n")
            f.write("\n")

# Print results in a more readable format
for server_result in results:
    print(f"\nResults for {server_result['server']}: ")
    for test in server_result["tests"]:
        print(f"  {test['test']}:")
        print(f"    Result: {test['result']}")
        print(f"    Stats: {test['stats']}")

print("\nAll tests completed! Results are stored in", OUTPUT_FILE, "and", MARKDOWN_FILE)
