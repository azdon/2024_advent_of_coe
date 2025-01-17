import re

with open('input/input.txt', 'r') as file:
    pattern = r"mul\([0-9]{1,3}[,][0-9]{1,3}\)"
    do_pattern = r"do\(\)"
    dont_do_pattern = r"don't\(\)"
    
    safe_chunks = []
    total_sum = 0
    mega_line = ""
    
    for line in file:
        mega_line += line
        
        
    # Find safe mul operations by finding chunks where dont() is
    line_chunks = mega_line.split("don't()")
    print(f"line after split on don't(): {line_chunks}")
    safe_chunks.append(line_chunks[0])
    
    # Next safe chunk could be within the rest of the split array
    for chunk in line_chunks[1:]:
        line = chunk.split("do()")
        # print(f"line split from within a dont() substring after splitting on do(): {line} from chunk: {chunk}")
        
        if len(line) > 1:
            for safe_chunk in line[1:]:
                # print(f"safe chunk to mul: {safe_chunk}")
                safe_chunks.append(safe_chunk)
                
        
    # print(f"safe chunks: {safe_chunks}")
    for chunk in safe_chunks:
        match = re.findall(re.compile(pattern), chunk)
    
        for match_subtr in match:
            print(f"Mul expression extracted: {match_subtr} from {line}")
            
            split = match_subtr.split(",")
            num1 = int(split[0].split("mul(")[1])
            num2 = int(split[1].split(")")[0])
            
            product = num1 * num2
            total_sum += product
            print(f"Parsed num1 {num1} * parsed num2 {num2} = sub product {product}")
        
    print(f"Total sum: {total_sum}")
    

