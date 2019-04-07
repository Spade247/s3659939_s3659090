import pygal                                                       # First import pygal
import leather
from datetime import datetime, timedelta
date_chart = pygal.Line(x_label_rotation=20)
date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
 datetime(2019, 4, 5),
 datetime(2019, 4, 6),
 datetime(2019, 4, 7)])
date_chart.add("Temperature in degrees", [28, 31, 29])
date_chart.add("Average Temperature", [24, 27, 22])
date_chart.render()
date_chart.render_to_file('/home/pi/Desktop/PIoT/s3659939_s3659090/dateChart.png')

data = [
    ('5/04/2019', 28),
    ('6/04/2019', 31),
    ('7/04/2019', 29)
]

chart = leather.Chart('Temperature')
chart.add_columns(data)
chart.to_svg('/home/pi/Desktop/PIoT/s3659939_s3659090/barChart.svg')