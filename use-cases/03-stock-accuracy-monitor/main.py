
from datetime import datetime, timezone

# Synthetic stock data from a source system
source_stock = {
    ("CA", "CA0007", "ART1001"): 15,
    ("CA", "CA0007", "ART1002"): 0,
    ("CA", "CA0008", "ART1003"): 25,
    ("SE", "SE0010", "ART1004"): 8,
    ("DE", "DE0020", "ART1005"): 50,
}

# Synthetic stock data returned by an availability API
api_stock = {
    ("CA", "CA0007", "ART1001"): 15,
    ("CA", "CA0007", "ART1002"): 5,
    ("CA", "CA0008", "ART1003"): 10,
    ("SE", "SE0010", "ART1004"): 8,
    ("DE", "DE0020", "ART1005"): 30,
}

WARNING_THRESHOLD = 5
CRITICAL_THRESHOLD = 15


def classify_severity(difference):
    if difference >= CRITICAL_THRESHOLD:
        return "CRITICAL"
    elif difference >= WARNING_THRESHOLD:
        return "WARNING"
    return "LOW"


def analyze_stock_accuracy(source, api):
    print("===== STOCK ACCURACY REPORT =====")
    print(
        "Generated:",
        datetime.now(timezone.utc).isoformat()
    )

    keys = set(source) | set(api)
    total = len(keys)
    accurate = 0
    mismatches = 0
    missing = 0

    for key in sorted(keys):
        market, store, article = key

        if key not in source or key not in api:
            missing += 1
            print(
                f"[MISSING] {market}/{store}/{article}: "
                "record missing from one system"
            )
            continue

        source_qty = source[key]
        api_qty = api[key]
        difference = abs(source_qty - api_qty)

        if difference == 0:
            accurate += 1
            continue

        mismatches += 1
        severity = classify_severity(difference)

        print(
            f"[{severity}] "
            f"{market}/{store}/{article} | "
            f"Source={source_qty} | "
            f"API={api_qty} | "
            f"Difference={difference}"
        )

    accuracy = (accurate / total * 100) if total else 100.0

    print("\n===== SUMMARY =====")
    print(f"Total Records: {total}")
    print(f"Accurate Records: {accurate}")
    print(f"Mismatched Records: {mismatches}")
    print(f"Missing Records: {missing}")
    print(f"Stock Accuracy: {accuracy:.2f}%")

    if mismatches or missing:
        print("\nACTION: Investigate stock inconsistencies.")
    else:
        print("\nSUCCESS: All stock records match.")


if __name__ == "__main__":
    analyze_stock_accuracy(source_stock, api_stock)
