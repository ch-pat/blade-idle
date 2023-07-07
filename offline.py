def should_i_push_next_stage(online_hours: int, 
                             current_fast_stage_exp: int, current_mid_stage_exp: int, current_clear_time: float,
                             next_fast_stage_exp: int, next_mid_stage_exp: int, next_clear_time: float):
    """
    online hours of play time expected
    current (lowest) fast stage exp yield
    current (offline) mid stage exp yield
    current clear time in seconds
    next (lowest after push) fast stage exp yield
    next (offline after push) mid stage exp yield
    next clear time in seconds
    """

    current_online_clears_in_a_day, current_offline_clears_in_a_day = get_clears_in_day(online_hours, current_clear_time)

    next_online_clears_in_a_day, next_offline_clears_in_a_day = get_clears_in_day(online_hours, next_clear_time)

    current_exp_gain = get_day_exp_gain(current_offline_clears_in_a_day, current_online_clears_in_a_day, current_mid_stage_exp, current_fast_stage_exp)
    next_exp_gain = get_day_exp_gain(next_offline_clears_in_a_day, next_online_clears_in_a_day, next_mid_stage_exp, next_fast_stage_exp)

    print("YES") if next_exp_gain >= current_exp_gain else print("NO")
    print()
    print("Detailed analysis:")
    print(f"Current exp gain in a day is {current_exp_gain}")
    print(f"Next stage exp gain would be {next_exp_gain}")
    print(f"For a percent increase of {(next_exp_gain/current_exp_gain - 1) * 100 :.2f} % (negative percent means a decrease)")




def get_clears_in_day(online_hours: int, clear_time: float) -> list[int, int]:
    SECONDS_PER_DAY = 86400
    OFFLINE_CLEAR_TIME = 26.0
    
    online_seconds = online_hours * 3600
    offline_seconds = (24 - online_hours) * 3600
    
    online_clears = online_seconds // clear_time
    offline_clears = offline_seconds // OFFLINE_CLEAR_TIME

    return [online_clears, offline_clears]

def get_day_exp_gain(offline_clears: int, online_clears: int, mid_stage_exp: int, fast_stage_exp: int) -> int:
    return offline_clears * mid_stage_exp + online_clears * fast_stage_exp

if __name__ == "__main__":
    online_hours = 6
    current_fast_exp = 632800
    current_mid_exp = 636700
    current_clear = 18.5
    next_fast_exp = 672630
    next_mid_exp = 676725
    next_clear = 23.5

    should_i_push_next_stage(online_hours, 
                             current_fast_exp, current_mid_exp, current_clear,
                             next_fast_exp, next_mid_exp, next_clear)