def kira_purata(markah):
    return sum(markah) / len(markah)

def test_purata():
    assert kira_purata([80, 90]) == 85
    assert kira_purata([100]) == 100
    print("test_purata: lulus")

test_purata()
