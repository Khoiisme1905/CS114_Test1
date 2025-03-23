def main():
    x1, y1 = map(int, input().split())
    
    x2, y2 = map(int, input().split())
    
    dx = x2 - x1
    dy = y2 - y1
    
    C1 = (x1 - dy, y1 + dx)
    D1 = (x2 - dy, y2 + dx)
    
    C2 = (x1 + dy, y1 - dx)
    D2 = (x2 + dy, y2 - dx)
    
    print(f"({x1}, {y1}) ({C1[0]}, {C1[1]}) ({D1[0]}, {D1[1]}) ({x2}, {y2})")
    print(f"({x1}, {y1}) ({x2}, {y2}) ({D2[0]}, {D2[1]}) ({C2[0]}, {C2[1]})")

if __name__ == "__main__":
    main()