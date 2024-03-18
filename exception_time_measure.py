import time
import platform
import builtins


def raise_exception(exception_type):
    for i in range(1000000):
        try:
            raise exception_type("Test exception")
        except Exception:
            pass


python_version = platform.python_version()

exceptions = [exc for exc in dir(builtins) if exc.endswith("Error")]

for exception_type in exceptions:
    filename = (
        f"exception_handling_time_log_python_{python_version}_{exception_type}.txt"
    )

    with open(filename, "w") as file:
        total_execution_time_ns = 0
        for i in range(50):
            start_time = time.perf_counter_ns()
            raise_exception(getattr(builtins, exception_type))
            end_time = time.perf_counter_ns()
            execution_time_ns = end_time - start_time
            file.write(f"Test {i+1}: Execution time: {execution_time_ns} ns\n")
            total_execution_time_ns += execution_time_ns

        average_execution_time_ns = total_execution_time_ns / 50
        file.write(f"Average execution time: {average_execution_time_ns} ns\n")
