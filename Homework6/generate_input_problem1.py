import random

def generate_file(filename, n, low=1, high=10000):
    """Generate a list of n random integers and save to filename."""
    nums = [random.randint(low, high) for _ in range(n)]
    
    with open(filename, "w") as f:
        f.write(str(n) + "\n")
        f.write(" ".join(map(str, nums)))

# Create datasets
generate_file("small.txt", 15)
generate_file("medium.txt", 50)
generate_file("large.txt", 500)