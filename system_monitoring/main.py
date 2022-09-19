import time
import psutil

"""CPU and Memory usage script with interactive output."""

def cpu_usage(cpu_usage, bars=50):
    
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = "█" * int(cpu_percent * bars) + "-" * (bars - int(cpu_percent * bars))

    print(f"\rCpu Usage: |{cpu_bar}| {cpu_usage: .2f}%  ", end="")


def mem_usage(mem_usage, bars=50):
    
    mem_percent = (mem_usage / 100.0)
    mem_bar = "█" * int(mem_percent * bars) + "-" * (bars - int(mem_percent * bars))
    
    print(f"Memory Usage: |{mem_bar}| {mem_usage: .2f}%  ", end="")


def main():
   
    while True:
        cpu_usage(psutil.cpu_percent(), 30)
        time.sleep(0.5)
        mem_usage(psutil.virtual_memory().percent, 30)

if __name__ == "__main__":
    main()

    