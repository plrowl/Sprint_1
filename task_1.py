time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

for time_part in time_string.replace(' ', ',').split(','):
        if 'h' in time_part:
            total_minutes += int(time_part.replace('h', '')) * 60
        elif 'm' in time_part :
            total_minutes += int(time_part.replace('m', ''))
        elif 's' in time_part :
            total_minutes += int(time_part.replace('s', '')) // 60

print(total_minutes)