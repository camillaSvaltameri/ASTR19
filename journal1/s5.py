import math

def main():
    num_points = 1000
    start = 0
    end = 2 * math.pi
    step = (end - start) / (num_points - 1)  

    print(f"{'x':>10} {'sin(x)':>10}")

    for i in range(num_points):
        x = start + i * step
        y = math.sin(x)
        print(f"{x:10.4f} {y:10.4f}") #aesthetics ;)

if __name__ == "__main__":
    main()

