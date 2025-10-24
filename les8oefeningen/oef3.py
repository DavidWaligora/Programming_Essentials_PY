import csv

def stripdate(dt_str):
    return dt_str.split(' ')[0]

def find_index_by_date(result_list, date):
    for i in range(len(result_list)):
        if result_list[i][0] == date:
            return i
    return -1

if __name__ == "__main__":
    with open("oefdata/weather_2018 10.csv") as file:
        result_list_of_data = [["datum", "aantal", "som_temperatuur"]]

        header = file.readline()  # skip CSV header

        for line in file:
            if line.strip():
                parts = line.rstrip().split(';')
                if len(parts) < 2:
                    continue

                date_str = stripdate(parts[0])
                temp = float(parts[1])

                index = find_index_by_date(result_list_of_data, date_str)

                if index == -1:
                    # New date → add new entry
                    result_list_of_data.append([date_str, 1, temp])
                else:
                    # Update existing entry
                    result_list_of_data[index][1] += 1
                    result_list_of_data[index][2] += temp

    # Write averages to CSV
    with open('average.csv', "w", newline='') as out_file:
        out_file.writelines("datum,aantal,gemiddelde_temp")
        for i in result_list_of_data[1:]:
            avg_temp = round(i[2] / i[1], 2)
            out_file.write(i[0], i[1], avg_temp)
  # Write averages to CSV
        #  with open('average.csv', "w", newline='') as out_file:
        #     writer = writer(out_file, delimiter=';')
        #     writer.writerow(["datum", "aantal", "gemiddelde_temp"])
            #     for i in result_list_of_data[1:]:
            #         avg_temp = round(i[2] / i[1], 2)
        #        writer.writerow([i[0], i[1], avg_temp])
