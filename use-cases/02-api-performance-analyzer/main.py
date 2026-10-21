
from math import ceil

# Sample API response times in milliseconds
response_times = [
    120, 150, 180, 200, 250,
    300, 350, 400, 450, 500,
    550, 600, 750, 900, 1200
]

# Sample HTTP status codes
status_codes = [
    200, 200, 200, 200, 200,
    200, 200, 200, 200, 200,
    200, 200, 500, 200, 503
]

SLA_THRESHOLD_MS = 500


def percentile(values, percentage):
    sorted_values = sorted(values)
    index = ceil(len(sorted_values) * percentage / 100) - 1
    return sorted_values[max(0, index)]


def analyze_api_performance(times, statuses):
    if not times or len(times) != len(statuses):
        raise ValueError("Provide equal, nonempty lists of times and statuses")

    total = len(times)
    average = sum(times) / total
    errors = sum(1 for status in statuses if status >= 400)
    slow_requests = sum(1 for time in times if time > SLA_THRESHOLD_MS)

    print("===== API PERFORMANCE REPORT =====")
    print(f"Total Requests: {total}")
    print(f"Average Latency: {average:.2f} ms")
    print(f"P90 Latency: {percentile(times, 90)} ms")
    print(f"P95 Latency: {percentile(times, 95)} ms")
    print(f"P99 Latency: {percentile(times, 99)} ms")
    print(f"HTTP Error Rate: {errors / total * 100:.2f}%")
    print(f"Slow Requests: {slow_requests}")

    if percentile(times, 90) > SLA_THRESHOLD_MS:
        print("WARNING: P90 latency exceeds SLA!")
    else:
        print("SUCCESS: P90 latency is within SLA.")


if __name__ == "__main__":
    analyze_api_performance(response_times, status_codes)
