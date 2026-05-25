import heapq

def a_star(graph, start, goal, h):
    # لیست باز (Open List): گره‌هایی که باید بررسی شوند
    # ساختار: (f_score, current_node)
    open_list = [(h[start], start)]
    
    # برای نگهداری کمترین هزینه رسیدن به هر گره
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_list:
        print("open list:", open_list)
        # ۱. انتخاب گره با کمترین f_score (این همان جادوی A* است)
        current_f, current = heapq.heappop(open_list)
        print(f"Current {current} with f({current}) = {current_f}")
        
        # اگر به هدف رسیدیم، مسیر بهینه پیدا شده است
        if current == goal:
            # return f"مسیر بهینه به {goal} با هزینه {g_score[goal]} پیدا شد."
            return f"Found the optimal to {goal} with the cost of {g_score[goal]}"
        
        # ۲. بررسی همسایه‌ها
        for neighbor, weight in graph[current].items():
            tentative_g = g_score[current] + weight
            print(f"{neighbor} |> (current {current}: g({g_score[current]})) + ({neighbor}: {weight}) = tentative = {tentative_g}")
            
            print(f"{tentative_g} < {g_score[neighbor]}")
            # اگر این مسیر به همسایه، از مسیرهای قبلی بهتر است
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h[neighbor]
                print(f"f_score = {tentative_g} + {h[neighbor]}")
                heapq.heappush(open_list, (f_score, neighbor))
                # print(f"گره {neighbor} به لیست باز اضافه شد با f_score={f_score}")
                print(f"Node {neighbor} added to open list with f_score={f_score}")
        print("--- End of graph sub-items")

    return "Can't find the target"

# تعریف یک گراف ساده
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

# هیوریستیک (تخمین فاصله تا D)
h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

print(a_star(graph, 'A', 'D', h))
