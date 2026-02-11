# Import time module to measure execution time and create delays
import time

# Import threading module to run tasks concurrently
import threading


# -------------------------------------------------
# Function 1: Simulates a long-running task
# -------------------------------------------------
def long_task(name):  # Define a function that simulates a long-running task
    """
    Simulates a long task by sleeping for a very short
    amount of time inside a loop.
    
    Args:
        name (str): Name of the task
    """

    # Repeat the loop 100,000 times to simulate heavy work
    for _ in range(100_000):

        # Pause execution for 0.0001 seconds (simulates workload)
        time.sleep(0.0001)

    # Print a message when the task is finished
    print(f"{name}: Task completed.")


# -------------------------------------------------
# Function 2: Executes tasks sequentially
# -------------------------------------------------
def run_sequential(times):  # Define function to run tasks one by one
    """
    Runs the long_task function sequentially and
    measures how long it takes.
    
    Args:
        times (int): Number of times to execute the task
    """

    # Record the starting time before execution
    start_time = time.time()

    # Loop 'times' number of times
    for i in range(times):

        # Call long_task normally (one finishes before next starts)
        long_task(f"Sequential Task {i + 1}")

    # Record the ending time after execution
    end_time = time.time()

    # Calculate total execution time
    elapsed = end_time - start_time

    # Print how long sequential execution took
    print(f"\nSequential execution finished in {elapsed:.2f} seconds\n")


# -------------------------------------------------
# Function 3: Executes tasks using threads
# -------------------------------------------------
def run_threaded(times):  # Define function to run tasks in parallel using threads
    """
    Runs the long_task function using multiple threads
    and measures how long it takes.
    
    Args:
        times (int): Number of threads to execute
    """

    # Create an empty list to store thread objects
    threads = []

    # Record the starting time before execution
    start_time = time.time()

    # Loop 'times' number of times to create threads
    for i in range(times):

        # Create a new Thread object
        thread = threading.Thread(

            # The function each thread will execute
            target=long_task,

            # Arguments passed to long_task (must be tuple)
            args=(f"Threaded Task {i + 1}",)
        )

        # Add thread to the list
        threads.append(thread)

        # Start the thread (runs concurrently)
        thread.start()

    # Wait for all threads to finish execution
    for thread in threads:

        # join() blocks main thread until this thread finishes
        thread.join()

    # Record the ending time after all threads complete
    end_time = time.time()

    # Calculate total execution time
    elapsed = end_time - start_time

    # Print how long threaded execution took
    print(f"\nThreaded execution finished in {elapsed:.2f} seconds\n")


# -------------------------------------------------
# Main program execution
# -------------------------------------------------
if __name__ == "__main__":  # Ensures code runs only if file is executed directly

    # Print message before running sequential version
    print("Running sequential function 10 times:")

    # Execute sequential tasks 10 times
    run_sequential(10)

    # Print message before running threaded version
    print("Running threaded function 10 times:")

    # Execute threaded tasks using 10 threads
    run_threaded(10)
