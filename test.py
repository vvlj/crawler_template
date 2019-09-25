from crawler import Runner
# 价格
url = 'https://p.3.cn/prices/mgets'
# 10个为一批
params = {
    'skuIds': 'J_100003883459,J_100003883459,J_35654974941,J_100004460494,J_8736570,J_7343287,J_100006976216,J_6772447,J_7296288,J_1351158,J_4354506', }
runner = Runner()
test_url = ['https://item.jd.com/100006581142.html',
            'https://item.jd.com/43769837874.html',
            'https://item.jd.com/39869037975.html',
            'https://item.jd.com/39869037975.html',
            ]
runner.set_goods_name(test_url)