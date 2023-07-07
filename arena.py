place_1 = 8
place_2 = 5
place_3 = 3
place_4 = 1


def luck_arena(current_points, tickets, next_rank):
    """fast heuristic to determine if i can rank up
    note: results until now are better than good luck (ex: good luck gave 156 points, I got 188)"""
    needed = next_rank - current_points
    print(f"Points needed to rank up: {needed}")
    good_luck = tickets * (1/2 * place_1 + 1/4 * place_2 + 1/4 * place_3)
    if good_luck >= needed:
        print(f"Rank up assuming good luck (50% wins, 25% 2nd and 25% 3rd): {good_luck}")
    else:
        print(f"No rank up with good luck, expected points: {good_luck}")
    mediocre_luck = tickets * (1/3 * place_1 + 1/3 * place_2 + 1/3 * place_3)
    if mediocre_luck >= needed:
        print(f"Rank up assuming mediocre luck (33% wins, 33% 2nd and 33% 3rd): {mediocre_luck}")
    else:
        print(f"No rank up with mediocre luck, expected points: {mediocre_luck}")

def minimum_arena(current_points, tickets, next_rank):
    """exhaustive calc to get worst case scenario that still ranks up with current tickets"""
    needed = next_rank - current_points
    if tickets * place_1 < needed:
        print(f"Impossible to rank up, need {needed} points, can do at most {tickets * place_1}")
        return
    for i in range(0, tickets + 1):
        for j in range(0, tickets + 1 - i):
            for k in range(0, tickets + 1 - i - j):
                for l in range(0, tickets + 1 - i - j - k):
                    score = l * place_4 + \
                            k * place_3 + \
                            j * place_2 + \
                            i * place_1
                    if score >= needed:
                        print(f"Rank up! Need {needed} points. Can be achieved with the worst luck of:")
                        print(f"{i} 1st places")
                        print(f"{j} 2nd places")
                        print(f"{k} 3rd places")
                        print(f"{l} 4th places")
                        return



if __name__ == "__main__":
    # Inputs
    current_points = 1501
    next_rank = 2000
    tix = 80
    luck_arena(current_points, tix, next_rank)
    print()
    print()
    minimum_arena(current_points, tix, next_rank)
