def find_number_pairs(numbers, N=10):
    solution_pairs = []
    for num in numbers:
        for partner in numbers:
            print(f"top of for: {num=} {partner=}")
            if partner == num:
                print(f"{num=} {partner=} continuing.")
                continue
            else:
                if num + partner == N:
                    pair = (num, partner)
                    rpair = (partner, num)
                    print(f"Adding {pair=} to {solution_pairs=}")
                    if pair not in solution_pairs or rpair not in solution_pairs:
                        solution_pairs.append(pair)

    return list(solution_pairs)

if __name__ == "__main__":
    find_number_pairs([3,4,1,2,9,5,6])
