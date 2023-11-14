import pandas as pd
import numpy as np
import os

start_date = '2023-01-01 00:00:00'
end_date = '2023-01-31 23:59:59'
date_index = pd.date_range(start=start_date, end=end_date, freq='S')

scale_parameter = 15

sensor_data = np.random.exponential(scale=scale_parameter, size=len(date_index))


sensor_data_rounded = np.round(sensor_data).astype(int)

data = {
    "Timestamp": date_index,
    "Sensor Data": sensor_data_rounded
}
df = pd.DataFrame(data)

output_dir = 'sensor_data_per_day'
os.makedirs(output_dir, exist_ok=True)

for day in pd.date_range(start='2023-01-01', end='2023-01-31'):
    day_data = df[df['Timestamp'].dt.date == day.date()].set_index('Timestamp')
    day_data.to_csv(os.path.join(output_dir, f'sensor_data_{day.strftime("%Y-%m-%d")}.csv'))
