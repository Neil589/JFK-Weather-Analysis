"""Analysis of climate stats from Laguardia airport, New York City from 2020-05-10 to 16 provided by the NOAA."""

__author__ = "730363127"

import sys 
from typing import Dict, List
from csv import DictReader


def main():
    """Entrypoint to out program. Calls functions with arguements given."""
    args: Dict[str, str] = read_args()
    string_list: List[str] = get_list(args["file_path"], args["column"])
    dates_list: List[str] = list_dates(args["file_path"], args["column"])
    list_data: List[float] = str_to_flt(string_list)
    operation_value: str = args["operation"]
    if operation_value == "min":
        print(min(list_data))
    elif operation_value == "max":
        print(max(list_data))
    elif operation_value == "avg":
        print(sum(list_data) / (len(list_data)))
    elif operation_value == "list":
        print(list_data)
    elif operation_value == "chart":
        chart_data(list_data, args["column"], dates_list)
    else:
        print("Invalid operation: " + args["operation"])
        exit()

    print(args)


def read_args() -> Dict[str, str]: 
    """Reads arguements and allows input of arguements. If expected number of args are not provided exits."""
    if len(sys.argv) != 4:
        print("Usage: python -m projects.pj01.weather [FILE] [COLUMN] [OPERATION]")
        exit()
    return {
        "file_path": sys.argv[1],
        "column": sys.argv[2],
        "operation": sys.argv[3] 
    }


def get_list(file: str, col: str) -> List[str]:
    """Reads file and produces a list with all the values from given column when Report_Type is SOD."""
    file_handle = open(file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle, delimiter=',')
    temp_list = []
    for row in csv_reader:
        if row["REPORT_TYPE"] == 'SOD  ':
            temp_list.append(row[col])
        if col != "DailyAverageDryBulbTemperature" and col != "DailyAverageWindSpeed" and col != "DailyPrecipitation":
            print("Invalid column: " + col)
            exit()

    return temp_list


def list_dates(file: str, column: str) -> List[str]:
    """Creates a list of dates from a given column for charting of data."""
    file_handle = open(file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle, delimiter=',')
    date_list = []
    for row in csv_reader:
        if row["REPORT_TYPE"] == 'SOD  ':
            date_list.append(row["DATE"])
    return date_list


def str_to_flt(str_list: List[str]) -> List[float]:
    """Converts a list of string values to float values."""
    a: int = 0
    str_list_new = []
    while a < len(str_list):
        try:
            x: float = float(str_list[a])
            str_list_new.append(x)
        except ValueError:
            ...   
        a = a + 1
    return str_list_new


def chart_data(data: List[float], column: str, dates: List[str]) -> None:
    """Charts data with dates on x axis and data on y axis when given the data, column of interest and dates."""
    import matplotlib.pyplot as plt
    # plot the values of our data over time
    plt.plot(dates, data)
    # label the x-axis Date
    plt.xlabel("Date")
    # label the y-axis whatever column we are analyzing
    plt.ylabel(column)
    # plot!
    plt.show()


if __name__ == "__main__":
    main()