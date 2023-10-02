"""Test"""
def test_set():
    """Test Set add by Loop"""
    test_1 = ["1", "2", "3", "4"]
    test_2 = ["0", "9", "8", "7"]
    out = set(
        [str(out_test_1)+out_test_2 for out_test_1 in test_1 for out_test_2 in test_2])
    out_2 = set(
        [str(out_test_1)+out_test_2 for out_test_1 in test_1 for out_test_2 in test_2])
    print(out.difference(out_2))
test_set()

def main():
    """Main Test"""
    out = []
    out.append("123456")
    out.append("09876")
    test = ""
    test_in = "12345"
    for i in reversed(test_in):
        test += i
    print(test)
main()
