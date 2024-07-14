threads = []  # 定义线程组

url = "https://x.com/home"
url2 = "https://discord.com/guild-discovery"

max_connections = int(input("请输入最大线程数:") or 3)  # 定义最大线程数
pool_sema = threading.BoundedSemaphore(max_connections)  # 或使用Semaphore方法

adsarr = input("请输入浏览器序号，连续格式：1-20,不连续使用逗号分开:") or "1-100"

open = int(input("请输入任务类型，【1】Twitter，【2】discord，【3】Twitter+discord:") or 3)  # 任务类型
start_time = datetime.datetime.now().replace(microsecond=0)
serial_number = []
type = "1"
