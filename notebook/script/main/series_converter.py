import datetime


def convert_to_series(data, length=24):
    series = []
    hour = data["hour"].iloc[0]
    day = data["day"].iloc[0]
    isNew = True
    new_serie = []
    for index, row in data.iterrows():
        if isNew or (row["hour"] == hour + 1) or (
                row["hour"] == 0 and hour == 23 and row["day"] == day + datetime.timedelta(days=1)):
            hour = row["hour"]
            day = row["day"]
            row.drop(labels=["day", "hour"], inplace=True)
            new_serie.append(row.values)
            isNew = False
        else:
            if len(new_serie) >= length:
                series.append(new_serie)
            new_serie = []
            isNew = True
            hour = row["hour"]
            day = row["day"]
            row.drop(labels=["day", "hour"], inplace=True)
            new_serie.append(row.values)
    if len(new_serie) >= length:
        series.append(new_serie)

    time_series = convert_to_time_series(series, length)
    return time_series


def convert_to_time_series(series, length=24):
    result = []
    for serie in series:
        if len(serie) >= length:
            for i in range(len(serie) - (length - 1)):
               if i%13 ==0: result.append(serie[i:i + length])
    return result
