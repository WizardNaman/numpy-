from loader import load_csv
from analysis import basic_stats, normalize, correlation
from utils import handle_missing

def main():
    file_path = input("Enter CSV file path: ")
    data = load_csv(file_path)

    if data is None:
        return

    data = handle_missing(data)

    print("\nBasic Statistics:")
    stats = basic_stats(data)
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\nNormalized Data:")
    print(normalize(data))

    print("\nCorrelation Matrix:")
    print(correlation(data))

if __name__ == "__main__":
    main()
