from Util.Summarizer import summarize


def Summarizer_Summarize_Equal():
    array = [2, 4]

    summary = summarize(array)

    assert summary.mean == 0.75, 'the calculated normalized mean should be 0.75'
    # TODO: add more asserts
