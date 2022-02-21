import numpy as np


class AHP:

    def __init__(self, array):
        self.array = array
        self.n = array.shape[0]
        # init the RI
        self.RI_list = [0, 0, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 1.58,
                        1.59]
        self.eig_val, self.eig_vector = np.linalg.eig(self.array)
        self.max_eig_val = np.max(self.eig_val)
        self.max_eig_vector = self.eig_vector[:, np.argmax(self.eig_val)].real
        # CI
        self.CI_val = (self.max_eig_val - self.n) / (self.n - 1)
        # CR
        self.CR_val = self.CI_val / (self.RI_list[self.n - 1])

    """
    Consistency judgment
    """

    def test_consist(self):
        print("CI:" + str(self.CI_val))
        print("CR:" + str(self.CR_val))
        if self.n == 2:  # only two indicator
            print("PASS")
        else:
            if self.CR_val < 0.1:  # CR<0.1
                print("CR:" + str(self.CR_val) + ",PASS")
                return True
            else:
                print("CR:" + str(self.CR_val) + "FAIL")
                return False

    """
    calculate weight
    """

    def cal_weight__by_eigenvalue_method(self):
        array_weight = self.max_eig_vector / np.sum(self.max_eig_vector)
        print("weight\n", array_weight)
        return array_weight


if __name__ == "__main__":
    b = np.array([[1, 1/3], [3, 1]])

    AHP(b).test_consist()
    weight3 = AHP(b).cal_weight__by_eigenvalue_method()