import numpy as np
import pandas as pd
from scipy import stats

p_mean = 35
p_var = 0.81

# 모분산 검정을 위한 단측 검정 함수를 작성하시오
def pvar_one_side_test(n, s_var, alpha, flag):
    # sample: sample data
    # s_var: 샘플 데이터의 분산
    # alpha: 유의수준
    # flag: 크다(True), 작다(False)를 구분하는 변수
    rv = stats.chi2(df=n - 1)

    # 유의수준 설정(단측검정)
    a = alpha

    # 검정통계량 계산
    x2 = ((n - 1) * s_var) / (p_var)
    print(x2)

    # 기각역 설정
    if flag:
        pointX2 = rv.isf(a)
        rejectArea = x2 > pointX2
    else:
        pointX2 = rv.isf(1-a)
        rejectArea = x2 < pointX2
    print(pointX2)

    print("귀무가설을 기각한다.") if rejectArea else print("귀무가설을 채택한다.")
    return

def main():
    #pmean_one_side_test(20, 33.1, 4.3*4.3, 0.025, False)
    #pmean_pmean_two_side_test(100, 10, 0.5, 0.01)
    #pmean_one_side_test_samplevar(20, 33.1, 4.3**2, 0.025, False)
    pvar_one_side_test(10, 1.44, 0.05, True)
    #pvar_two_side_test(8, 1.8**2, 0.05)
    a = 0.025
    nn = stats.norm()
    tt = stats.t(df=9)
    xx = stats.chi2(df=9)
    print(nn.isf([1-a, a]))
    print(tt.isf([1-a, a]))
    print(xx.isf([1-a, a]))

if __name__ == "__main__":
    main()