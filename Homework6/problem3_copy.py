# gale-shapley stable matching for dating web service
import sys 

def stable_matching(male_list, female_list):

    female_names = [row[0] for row in female_list]
    engaged = []
    engaged_female = [row[1] for row in engaged]
    active_males = [row for row in male_list]  # copy of male_list to keep track of active males
    maybe_males = []                           # list to keep track of males who made proposals in current iteration

    while active_males:
        man = active_males[0]               # man is a list; iterate when there are still active males
        made_proposal = False

        while len(man) > 1:        # propose to the man's first preference in his list while there are still females in the list
            male_name = man[0]
            female_name = man[1]

            # Case 1: Female not yet engaged
            if female_name not in engaged_female:
                maybe_pair =[male_name,female_name] # create a maybe pair where man[0] is the male name and man[i] is the female name
                engaged.append(maybe_pair)
                engaged_female.append(female_name)  # update engaged_female list

                man.pop(1)
                maybe_males.append(man)  # remove the female from the active male's preference list in case he needs to propose again later

                active_males.pop(0)         # remove the male from active males
                made_proposal = True
                break
            
            # Case 2: Female already engaged
            elif female_name in engaged_female:
                token_index = female_names.index(female_name)  # find the engaged female from the female_list
                female_pref = female_list[token_index]    # get her preference list
                current_partner_idx = engaged_female.index(female_name)  # find her current partner index from engaged_female list
                current_partner_name = engaged[current_partner_idx][0]  # get the name of her current male partner

                if female_pref[1:].index(male_name) < female_pref[1:].index(current_partner_name):  # add [1:] to avodi the case that female and male names are the same
                    # if she prefers the new man
                    engaged[current_partner_idx][0] = male_name  # update her partner to the new man
                    man.pop(1)
                    maybe_males.append(man)  # remove the female from the active male's preference list in case he needs to propose again later

                    maybe_males_names = [row[0] for row in maybe_males]
                    current_partner_row = maybe_males_names.index(current_partner_name)  # find the row of the current partner in the maybe_male list
                    active_males.append(maybe_males[current_partner_row])  # add the current partner back to active

                    active_males.pop(0)         # remove the new man from active

                    engaged_female = [row[1] for row in engaged]  # update engaged_female list
                    made_proposal = True
                    break

                else:
                    # if she prefers her current partner
                    man.pop(1)  # remove from the active male list and try next preference
                    
                    continue
        
        # Case 3: No more available females to propose to
        if not made_proposal:
            print('Warning: No more available females to propose to for male', man[0])

    return engaged



def main():

    # Read all input lines
    lines = sys.stdin.read().strip().splitlines()

    # First line: n
    n = int(lines[0])

    # Next n lines → male list
    male_lines = lines[1 : 1 + n]

    # Next n lines → female list
    female_lines = lines[1 + n : 1 + 2*n]

    # Convert each line into a list of names
    male = [line.split() for line in male_lines]
    female = [line.split() for line in female_lines]

    # Get the stable matching pairs
    pairs = stable_matching(male, female)
    for pair in pairs:
        print(pair[0], pair[1])
    # also print output to a file, with file name depending on the number of n
    output_filename = f'stable_matching_output_{n}.txt'
    with open(output_filename, 'w') as f:
        for pair in pairs:
            f.write(f'{pair[0]} {pair[1]}\n')

if __name__ == "__main__":
    main()  