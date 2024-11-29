# 网络性能测试
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# 配置测试参数
URL_FIRST_LEVEL = "http://127.0.0.1:5000/get_questions/first"
URL_SECOND_LEVEL = "http://127.0.0.1:5000/get_questions/second"
NUM_REQUESTS = 10000  # 发送请求的数量
CONCURRENCY = 20    # 并发请求数量

# 定义请求函数
def send_request(url):
    start_time = time.time()
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        elapsed_time = time.time() - start_time
        return elapsed_time
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

# 性能测试函数
def performance_test(url):
    times = []
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
        futures = [executor.submit(send_request, url) for _ in range(NUM_REQUESTS)]
        for future in as_completed(futures):
            elapsed_time = future.result()
            if elapsed时间 is not None:
                times.append(elapsed_time)

    # 计算并打印性能结果
    if times:
        print(f"总请求数: {len(times)}")
        print(f"平均响应时间: {sum(times) / len(times):.4f} 秒")
        print(f"最快响应时间: {min(times):.4f} 秒")
        print(f"最慢响应时间: {max(times):.4f} 秒")
    else:
        print("未成功发出任何请求。")

# 执行测试
print("测试一级问题 API")
performance_test(URL_FIRST_LEVEL)

print("\n测试二级问题 API")
performance_test(URL_SECOND_LEVEL)