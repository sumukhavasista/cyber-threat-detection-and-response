# severity_mapper.py

def determine_severity(row):
    if 'cpu_usage' in row and row['cpu_usage'] > 90:
        return 'high'
    elif 'cpu_usage' in row and row['cpu_usage'] > 70:
        return 'medium'
    else:
        return 'low'
