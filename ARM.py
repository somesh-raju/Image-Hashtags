import pandas as pd

from collections import Counter

ar = pd.read_csv('IH_association_rules.csv')


def getConsecuents(common_preds):
    for i in range(len(common_preds), 0, -1):
        consequents = \
            ar[(ar['antecedents'] == {*common_preds[0:i]}) & (ar['confidence'] > 0.0)].sort_values('confidence',
                                                                                                   ascending=False)[
                'consequents'].apply(lambda x: list(x)[0]).to_list()
        if len(consequents) > 1:
            return consequents[:15]
    return common_preds


def getArmPreds(all_preds):
    pred_counts = Counter(all_preds)
    C1 = [pred for pred in pred_counts if pred_counts[pred] >= 2]
    C2 = [pred for pred in pred_counts if pred_counts[pred] == 1]

    C1_arm = getConsecuents(C1)

    C3 = list(set(C1_arm).intersection(set(C2)))
    final_pred = C3 + C1

    if len(final_pred) >= 1:
        if len(final_pred) < 5 and not final_pred.__contains__('instapic') \
                and not final_pred.__contains__('photooftheday'):
            final_pred.extend(['photooftheday', 'bestclick'])
        return final_pred
    else:
        if len(C2) < 5 and not C2.__contains__('instapic') \
                and not C2.__contains__('photooftheday'):
            C2.extend(['instapic', 'photooftheday', 'bestclick'])
        try:
            C2.remove('snow')
        except ValueError:
            pass
        return C2
