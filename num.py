def vietnamese_to_number(s):
    nums = {
        'không': 0, 'một': 1, 'hai': 2, 'ba': 3, 'bốn': 4,
        'năm': 5, 'sáu': 6, 'bảy': 7, 'tám': 8, 'chín': 9,
        'mười': 10, 'mươi': 10, 'lăm': 5, 'linh': 0, 'lẻ': 0,
        'tư': 4
    }
    
    muls = {'tỷ': 1000000000, 'triệu': 1000000, 'nghìn': 1000, 'trăm': 100, 'vạn': 10000}
    
    def process_small(w):
        res = 0
        i = 0
        while i < len(w):
            x = w[i]
            
            # special case lol
            if x == 'tư' and i > 0 and w[i-1] == 'hai':
                res = 24
                i += 1
                continue
                
            if x in nums:
                if x in ['mươi', 'mười']:
                    if i > 0 and w[i-1] in nums:
                        tmp = res - (res % 100) if res >= 100 else 0
                        res = tmp + (nums[w[i-1]] * 10)
                    else:
                        res = res - (res % 100) + 10 if res >= 100 else 10
                    
                    if i + 1 < len(w) and w[i + 1] in nums and w[i + 1] not in ['mươi', 'mười', 'trăm']:
                        res += nums[w[i + 1]]
                        i += 1
                elif x == 'lăm':
                    if i > 0 and w[i-1] in ['mươi', 'mười']:
                        res = (res - (res % 100) if res >= 100 else 0) + (res % 100 - 10) + 15
                    elif i > 0 and (w[i-1] == 'không' or w[i-1] == 'mười' or 
                                  (i > 1 and w[i-2] == 'không' and w[i-1] in ['mươi', 'mười'])):
                        res = (res - (res % 100) if res >= 100 else 0) + 15
                else:
                    if i + 1 < len(w) and w[i + 1] == 'trăm':
                        res += nums[x] * 100
                    elif i + 1 < len(w) and w[i + 1] in ['mươi', 'mười']:
                        pass  # skip 
                    else:
                        if not (i > 0 and (w[i-1] in ['mươi', 'mười'] or w[i-1] == 'trăm')):
                            res += nums[x]
            elif x == 'trăm':
                pass  # already handled
            elif x == 'linh' or x == 'lẻ':
                if i + 1 < len(w) and w[i + 1] in nums:
                    res += nums[w[i + 1]]
                    i += 1
            elif x == 'không':
                if i + 1 < len(w):
                    if w[i + 1] in ['mươi', 'mười']:
                        if i + 2 < len(w) and w[i + 2] == 'lăm':
                            res = (res - (res % 100) if res >= 100 else 0) + 15
                            i += 2
                        else:
                            i += 1
                elif w[i + 1] == 'mười' and i + 2 < len(w) and w[i + 2] == 'lăm':
                    res = (res - (res % 100) if res >= 100 else 0) + 15
                    i += 2
            i += 1
        return res

    def process_block(w):
        res = 0
        curr = []
        bil_bil = 0  # billion billion value
        sau_bb = False
        after_sum = 0
        last_mul = 0  
        
        i = 0
        while i < len(w):
            x = w[i]
            
            if x == 'tỷ':
                if curr:
                    n = process_small(curr)
                    if i + 1 < len(w) and w[i + 1] == 'tỷ':
                        bil_bil = n
                        sau_bb = True
                        i += 1  
                    elif sau_bb:
                        if last_mul:
                            after_sum += (n * last_mul) * 1000000000
                            last_mul = 0
                        else:
                            after_sum += n * 1000000000
                    else:
                        res += n * 1000000000
                else:
                    if i + 1 < len(w) and w[i + 1] == 'tỷ':
                        bil_bil = 1
                        sau_bb = True
                        i += 1
                    elif sau_bb:
                        if last_mul:
                            after_sum += last_mul * 1000000000
                            last_mul = 0
                        else:
                            after_sum += 1000000000
                    else:
                        res += 1000000000
                curr = []
            elif x in muls and x != 'trăm':
                if curr:
                    n = process_small(curr)
                    if sau_bb:
                        if x == 'nghìn':
                            last_mul = n * 1000
                        else:
                            after_sum += n * muls[x]
                    else:
                        res += n * muls[x]
                    curr = []
                elif res == 0 and not sau_bb:
                    res = muls[x]
            else:
                curr.append(x)
            i += 1
                
        if curr:
            n = process_small(curr)
            if sau_bb:
                after_sum += n
            else:
                res += n
        
        if sau_bb:
            return (bil_bil * (1000000000 ** 2)) + after_sum
        return res

    return process_block(s.lower().split())

def main():
    print("Enter Vietnamese number string:")
    try:
        s = input().strip()
        print(vietnamese_to_number(s))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()