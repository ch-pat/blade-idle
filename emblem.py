def emblems_needed(current: int, next: int, gain: int):
    need = next - current
    emblems_to_next = need // gain + 1
    print(f"Need {emblems_to_next} tickets for emblem up")


if __name__ == "__main__":
    current = 215_260
    next = 1_500_000
    gain = 6_773
    emblems_needed(current, next, gain)