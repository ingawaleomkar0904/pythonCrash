batches = [
    [101, 102, 103, 101],
    [201, 202, 203, 204],
    [301, 301, 301, 302]
]
for batch in batches:
    duplicate_count = 0
    for i in range(len(batch)):
        for j in range(i + 1, len(batch)):
            if batch[i] == batch[j]:
                duplicate_count += 1
    print(f"Batch: {batch} | Duplicates: {duplicate_count}")

#---------------------------------------------------------------------------
ages = [25, -5, 130, None, "", 40, 0, 200]

for age in ages:
    if age is None or age == "":
        print(f"None or missing age : {age}")
    elif age < 0 or age > 120:
        print(f"Invalid age : {age}")
    else:
        print(f"Valid age : {age}")    

#---------------------------------------------------------------------------
file_sizes = [120, 45, -1, 300, 0, 500, 200]
sum_of_sizes = 0

for size in file_sizes:
    if size == -1:
        continue
    if size == 0:
        break
    sum_of_sizes += size
print(f"Total size of files is {sum_of_sizes}")  

#---------------------------------------------------------------------------
for i in range(1, 101):
    if i % 5 == 0 and i % 15 != 0:
        print(f"{i} is divisible by 5")
#---------------------------------------------------------------------------
logs = [
    "INFO: job started",
    "ERROR: connection timeout",
    "WARN: retry attempt 1",
    "ERROR: connection timeout",
    "INFO: job finished"
]

info_log_count = 0
error_log_count = 0
warn_log_count = 0

for log in logs:
    if log.upper().startswith("ERROR"):
        error_log_count += 1
    elif log.upper().startswith("INFO"):
        info_log_count += 1
    elif log.upper().startswith("WARN"):
        warn_log_count += 1

print(f"INFO logs: {info_log_count}")
print(f"ERROR logs: {error_log_count}")
print(f"WARN logs: {warn_log_count}")