def LPT(machine_list, task_list, middle_bound, max_bound):
    task_list_copy = task_list.copy()
    task_list_copy.sort(reverse=True)
    machine_list_copy = machine_list.copy()

    for i in range(len(task_list_copy) - 1):
        min_machine_list = min(machine_list_copy)
        pos = machine_list_copy.index(min_machine_list)
        machine_list_copy[pos] += task_list_copy[i]

    max_ = max(machine_list_copy)
    max_bound_ = max(max_bound, middle_bound)
    ratio = max_ / max_bound_

    return max_, ratio


def LPT_I_r(L):
    L_copy = L.copy()
    out = 0
    for i in L_copy:
        tuplet = LPT(i[1], i[0], i[3], i[2])
        out += tuplet[1]

    return out / len(L)
