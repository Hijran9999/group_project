import time
import threading

# -------------------------------------------------
# Function 1: Simulates a long-running task
# -------------------------------------------------
def long_task(name):
    """
    Simulates a long task by sleeping for a very short
    amount of time inside a loop.
    
    Args:
        name (str): Name of the task
    """
    # Loop 100,000 times
    for _ in range(100_000):
        # Pause execution for 0.0001 seconds
        time.sleep(0.0001)

    # Print message after the task completes
    print(f"{name}: Task completed.")


# -------------------------------------------------
# Function 2: Executes tasks sequentially
# -------------------------------------------------
def run_sequential(times):
    """
    Runs the long_task function sequentially and
    measures how long it takes.
    
    Args:
        times (int): Number of times to execute the task
    """
    # Record the start time
    start_time = time.time()

    # Call the long_task function one by one (sequentially)
    for i in range(times):
        long_task(f"Sequential Task {i + 1}")

    # Record the end time
    end_time = time.time()

    # Calculate elapsed time
    elapsed = end_time - start_time

    # Print execution time
    print(f"\nSequential execution finished in {elapsed:.2f} seconds\n")


# -------------------------------------------------
# Function 3: Executes tasks using threads
# -------------------------------------------------
def run_threaded(times):
    """
    Runs the long_task function using multiple threads
    and measures how long it takes.
    
    Args:
        times (int): Number of threads to execute
    """
    threads = []

    # Record the start time
    start_time = time.time()

    # Create and start threads
    for i in range(times):
        thread = threading.Thread(
            target=long_task,
            args=(f"Threaded Task {i + 1}",)
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Record the end time
    end_time = time.time()

    # Calculate elapsed time
    elapsed = end_time - start_time

    # Print execution time
    print(f"\nThreaded execution finished in {elapsed:.2f} seconds\n")


# -------------------------------------------------
# Main program execution
# -------------------------------------------------
if __name__ == "__main__":
    # Call the sequential function 10 times
    print("Running sequential function 10 times:")
    run_sequential(10)

    # Call the threaded function 10 times
    print("Running threaded function 10 times:")
    run_threaded(10)
