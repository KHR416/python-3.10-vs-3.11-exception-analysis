import builtins


def parse_execution_times(filename):
    execution_times = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Average execution time"):
                execution_time = round(float(line.split(":")[-1].strip().split()[0]))
                execution_times.append(execution_time)
    return execution_times


exceptions = [exc for exc in dir(builtins) if exc.endswith("Error")]

python_310_time = {}
python_311_time = {}

for exception_type in exceptions:
    filename_310 = (
        f"./log/exception_handling_time_log_python_3.10.0_{exception_type}.txt"
    )
    filename_311 = (
        f"./log/exception_handling_time_log_python_3.11.0_{exception_type}.txt"
    )

    python_310_time[exception_type] = parse_execution_times(filename_310)
    python_311_time[exception_type] = parse_execution_times(filename_311)

output_filename = "./analysis/execution_time_difference.txt"
with open(output_filename, "w") as output_file:
    for exception_type in exceptions:
        output_file.write(f"Exception Type: {exception_type}\n")
        for time_310, time_311 in zip(
            python_310_time[exception_type], python_311_time[exception_type]
        ):
            time_per_one_exception_310 = time_310 / 1000000
            time_per_one_exception_311 = time_311 / 1000000
            time_difference_per_one_exception = (
                time_per_one_exception_311 - time_per_one_exception_310
            )
            percentage = (
                time_difference_per_one_exception / time_per_one_exception_310
            ) * 100
            output_file.write(
                f"time per one exception of 3.10: {time_per_one_exception_310:.2f} ns\n"
            )
            output_file.write(
                f"time per one exception of 3.11: {time_per_one_exception_311:.2f} ns\n"
            )
            output_file.write(
                f"Time difference per one exception : {time_difference_per_one_exception:.2f} ns\n"
            )
            output_file.write(f"Percentage: {percentage:.2f} %\n")
            output_file.write("\n")
