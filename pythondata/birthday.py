from datetime import datetime

birthday = "2012-05-1"
date_format = "%Y-%m-%d"


parsed_date = datetime.strptime(birthday, date_format)
date_str = parsed_date.strftime("%m/%d/%y") # 01/11/17
print(date_str)

