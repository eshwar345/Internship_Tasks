# Task 3: Import and test all 15 functions.
from solutions import (
    word_frequency,
    character_frequency,
    first_non_repeating_character,
    are_anagrams,
    first_repeating_character,
    move_zeros_to_end,
    second_highest_distinct,
    remove_duplicates_preserve_order,
    find_missing_number,
    find_first_pair_sum,
    closest_to_zero,
    common_elements,
    rotate_right,
    max_consecutive_pair_sum,
    all_unique_pairs_sum,
)


def show_test(question, function, example_args, extra_args):
    print(f"\n{question}")
    print("Example:", function(*example_args))
    print("Additional test:", function(*extra_args))


if __name__ == "__main__":
    show_test("Q1", word_frequency,
              ("python is easy and python is powerful",),
              ("red blue red",))
    show_test("Q2", character_frequency,
              ("banana",),
              ("letter",))
    show_test("Q3", first_non_repeating_character,
              ("swiss",),
              ("aabb",))
    show_test("Q4", are_anagrams,
              ("listen", "silent"),
              ("Dormitory", "Dirty room"))
    show_test("Q5", first_repeating_character,
              ("programming",),
              ("abcdef",))
    show_test("Q6", move_zeros_to_end,
              ([0, 3, 0, 1, 2, 0, 4],),
              ([0, 0, 5, 0],))
    show_test("Q7", second_highest_distinct,
              ([10, 20, 40, 30, 40, 20],),
              ([5, 5, 5],))
    show_test("Q8", remove_duplicates_preserve_order,
              ([4, 2, 4, 5, 2, 7, 5],),
              ([1, 1, 2, 3, 2],))
    show_test("Q9", find_missing_number,
              ([1, 2, 4, 5, 6], 6),
              ([2, 3, 4, 5], 5))
    show_test("Q10", find_first_pair_sum,
              ([2, 7, 11, 15], 9),
              ([1, 4, 2, 3], 6))
    show_test("Q11", closest_to_zero,
              ([-8, -3, 2, 5, -2],),
              ([-4, -1, 1, 7],))
    show_test("Q12", common_elements,
              ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]),
              ([4, 4, 2, 1], [1, 4],))
    show_test("Q13", rotate_right,
              ([1, 2, 3, 4, 5], 2),
              ([1, 2, 3], 5))
    show_test("Q14", max_consecutive_pair_sum,
              ([4, 7, 2, 9, 5],),
              ([-5, -2, -8],))
    show_test("Q15", all_unique_pairs_sum,
              ([2, 4, 3, 5, 7, 8, 1], 9),
              ([1, 1, 2, 2, 3, 3], 4))
