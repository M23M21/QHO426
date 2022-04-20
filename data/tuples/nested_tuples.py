def steps():
    likelihoods = [("step1", 50), ("step2", 38), ("step3", 27), ("step4", 99), ("step5", 4)]
    return likelihoods

def run():
    probabilities = steps()
    good_steps = []
    bad_steps = list()
    for tuplex in probabilities:
        if tuplex[1] >= 50:
            bad_steps.append(tuplex)
        else:
            good_steps.append(tuplex)
    print("Good steps: {}, Bad steps: {}".format(len(good_steps), len(bad_steps)))
