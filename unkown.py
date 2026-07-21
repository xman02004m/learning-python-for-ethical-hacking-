# 4. Your corrected Q4 function using proper boolean values
def is_common_port(port):
    if port == 22 or port == 80 or port == 443:
        return True
    else:
        return False


# 7. The range function that calls your Q4 function
# def check_port_range(start, end):
#     for port in range(start, end + 1):
#         if is_common_port(port):
#             print(f"{port} - common")
#         else:
#             print(f"{port} - uncommon")

def check_port_range(start,end):
    for port in range(start,end+1):
        if is_common_port(port):
            print(f"{port} is common")
        else:
            print(f"{port} is uncommom")
check_port_range(78,84)
# Test the range function
print("--- Running Range Check (78 to 82) ---")
check_port_range(78, 82)
