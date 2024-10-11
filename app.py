import html_download
import data_analyse
import transform
import schedule
import time

def job():
    html_download.html_save()
    data_analyse.main()
    transform.main()

if __name__ == '__main__':
    schedule.every(30).minutes.do(job)

    while True:
        # 检查是否有任务需要运行
        schedule.run_pending()
        # 休眠一会儿，避免CPU占用过高
        time.sleep(1)