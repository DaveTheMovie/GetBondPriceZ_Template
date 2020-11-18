
import GetBondPrice_Z

def test_getBondDuration():
    yc = [.010,.015,.020,.025,.030]
    times=[1,1.5,3,4,7]
    face = 2000000
    couponRate = .04
    x = GetBondPrice_Z.getBondPrice_Z(face, couponRate, times, yc)
    assert round(x) == 1996533