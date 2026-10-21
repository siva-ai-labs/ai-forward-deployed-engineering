
from datetime import datetime

# Sample application logs
logs = [
    "INFO Application started successfully",
    "INFO API request completed in 120ms",
    "ERROR HTTP 500 Internal Server Error",
    "WARN HTTP 429 Too Many Requests",
    "ERROR Database connection timeout",
    "ERROR gRPC INTERNAL failure",
    "INFO API request completed in 90ms",
]


def analyze_logs(log_entries):
    print("\n=== AI Incident Log Analyzer ===")
    print("Analysis Time:", datetime.now())

    errors = []
    warnings = []

    for log in log_entries:
        if "ERROR" in log:
            errors.append(log)
        elif "WARN" in log:
            warnings.append(log)

    print("\nTotal Logs:", len(log_entries))
    print("Errors:", len(errors))
    print("Warnings:", len(warnings))

    print("\nDetected Errors:")
    for error in errors:
        print("-", error)

    print("\nDetected Warnings:")
    for warning in warnings:
        print("-", warning)

    if errors:
        print("\nIncident Status: INVESTIGATION REQUIRED")
    else:
        print("\nIncident Status: HEALTHY")


if __name__ == "__main__":
    analyze_logs(logs)
