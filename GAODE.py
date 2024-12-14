import requests

api_key = 	"db9ca7320d5d0b6c4f515e3dbd84f3ca"

# 起点和终点的经纬度
origin = '121.481578,31.14881'  # 上海纽约大学
destination = '121.478293,31.167869'  # 宿舍

driving_url = f'https://restapi.amap.com/v3/direction/driving?origin={origin}&destination={destination}&key={api_key}'
walking_url = f'https://restapi.amap.com/v3/direction/walking?origin={origin}&destination={destination}&key={api_key}'
transit_url = f'https://restapi.amap.com/v3/direction/transit/integrated?origin={origin}&destination={destination}&city=上海&key={api_key}'

# 驾车路径规划
def get_driving_route():
    response = requests.get(driving_url)
    data = response.json()
    if data['status'] == '1':
        route = data['route']
        paths = route['paths']
        for path in paths:
            print(f"驾车路径总距离：{path['distance']}米")
            print(f"驾车预估时间：{int(path['duration']) / 60}分钟")
    else:
        print("驾车路径规划请求失败")

# 步行路径规划
def get_walking_route():
    response = requests.get(walking_url)
    data = response.json()
    if data['status'] == '1':
        route = data['route']
        paths = route['paths']
        for path in paths:
            print(f"步行路径总距离：{path['distance']}米")
            print(f"步行预估时间：{int(path['duration']) / 60}分钟")
    else:
        print("步行路径规划请求失败")


# 获取公共交通路径规划
def get_transit_route():
    response = requests.get(transit_url)
    data = response.json()
    if data['status'] == '1':
        transits = data['route']['transits']
        for transit in transits:
            print(f"公共交通总时间：{int(transit['duration']) / 60}分钟")
            print(f"总步行距离：{transit['walking_distance']}米")
            for segment in transit['segments']:
                bus = segment['bus']
                if bus['buslines']:
                    for busline in bus['buslines']:
                        print(f"公交线路：{busline['name']}, 预计时间：{int(busline['duration']) / 60}分钟")
    else:
        print("公共交通路径规划请求失败")

# 调用函数获取不同交通方式的路径规划和预估时间
get_driving_route()
get_walking_route()
get_transit_route()
