months = ["January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
          ]
while True:
    user_input = input("Date:").strip()
    if '/' in user_input:
       parts = user_input.split('/')
       if len(parts) ==3:
        month,date,year = parts
        if month.isdigit() and date.isdigit() and year.isdigit():
            month = int(month)
            date =int(date)
            if 1<= month <= 12 and 1<= date <= 31:
                print(f"{year}-{month:02}-{date:02}")
                break
            else:
                continue
        else:
            continue
       else:
           continue
    elif " " in user_input:
        parts = user_input.split(' ')
        if len(parts) ==3:
         month,date,year = parts
         date = date[:-1]
         if month in months and date.isdigit() and year.isdigit():
            date =int(date)
            if 1<= date <= 31:
                month_index = months.index(month) + 1
                print(f"{year}-{month_index:02}-{date:02}")
                break
            else:
                continue
         else:
             continue
        else:
            continue
    else:
        continue    
