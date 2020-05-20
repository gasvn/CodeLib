def get_entropy(x, dim = 2):  # https://www.cnblogs.com/loubin/p/11330576.html
    # n hw c
    res = F.softmax(x, dim=dim) * F.log_softmax(x, dim=dim)
    print(res.shape)
    res = -res.sum(dim=dim)
    return res
