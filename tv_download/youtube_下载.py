import yt_dlp

# 提示用户输入播放列表 URL
url = input("请输入播放列表网址：")

# 配置下载选项
ydl_opts = {
    'outtmpl': 'videos/%(title)s.%(ext)s',  # 下载的视频存储路径和命名规则
    'cookiefile': 'cookies.txt',           # 指定 Cookies 文件路径
    'sleep_interval': 5,                   # 每次请求之间最小间隔（秒）
    'max_sleep_interval': 10,              # 每次请求之间最大间隔（秒）
    'playliststart': 4,                    # 从播放列表的第 4 个视频开始下载
}

# 使用 yt-dlp 下载播放列表
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("播放列表下载成功！已保存在 videos 文件夹中")
except Exception as e:
    print(f"下载失败: {e}")






