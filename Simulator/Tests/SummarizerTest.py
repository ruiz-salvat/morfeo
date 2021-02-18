from Util.Summarizer import summarize


def Summarizer_Summarize_Equal():
    array = [2, 4]

    summary = summarize(array)

    assert summary.mean == 3, 'the calculated mean should be 3'
    # TODO: add more asserts
