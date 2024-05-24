for _ in range(int(input())):
    n, idx = map(int, input().split())    # n: 프린트 수 m: 대상 인덱스
    printer = list(map(int, input().split()))   # 우선순위
    cnt = 0

    while len(printer) > 0:
        if idx > 0:
            if max(printer) == printer[0]:
                printer.pop(0)
                cnt += 1
                idx -= 1
            else:
                printer.append(printer.pop(0))
                idx -= 1
        else:
            if max(printer) == printer[0]:
                cnt += 1
                print(cnt)
                break
            else:
                printer.append(printer.pop(0))
                idx = len(printer) - 1